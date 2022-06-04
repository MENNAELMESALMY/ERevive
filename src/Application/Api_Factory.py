from os import name


class ApiFactory(object):
    namespaces={}
    def __init__(self, models,user,password,db,modelsObjects):
        self.models = models
        self.user = user
        self.password=password
        self.db = db
        self.api_files = None
        self.modelsObjects=modelsObjects
        self.crud_clusters = {}


    def create_app_env(self):
        return ' \n\
user="{0}" \n\
password="{1}" \n\
database="{2}" \n\
'.format(self.user,self.password,self.db)

    def create_models_apis(self):
        Apis={}
        for model in self.models.keys():
            crud_ui_out,api = self.create_api(model,self.models[model])
            Apis[model.lower()] = api
        self.api_files = Apis
        return Apis,crud_ui_out
        
    def create_api_header(self,models):
        model_import = ' , '.join(models)
        return '\
from flask.helpers import make_response \n\
from flask_restx import Resource, Namespace , fields , reqparse \n\
from flask import jsonify, request \n\
from models import {0} \n\
from app import db \n\
from utils import convert_db_model_to_restx_model \n\
            '.format(model_import)

    def create_api(self,model,attributes): 
        model_create_string=''
        parser_create_string='{0}_id_parser = reqparse.RequestParser() \n'.format(model)
        primary_keys = self.modelsObjects[model]['primaryKey']
        body_params = []
        query_params = []
        ui_response_model = []
        self.crud_clusters.update({model:[]})
        for attribute in attributes:
            terminal_command = ','
            type = self.modelsObjects[model]['attributes'][attribute]
            ui_response_model.append((attribute,type))
            if attribute == attributes[-1]:
                terminal_command = ''
            if attribute in primary_keys:
                parser_create_string+= "{0}_id_parser.add_argument('{1}',type={2})\n".format(model,attribute,type)
                query_params.append((attribute,type))
            body_params.append((attribute,type))

            model_create_string+='{0} = request.json.get("{0}")'.format(attribute)+terminal_command   
        endpoint_name,ui_name = model,model
        endpoint_url = '/'+model.lower()
        
        endpoint_object = [{
            "method": "get",
            "url": endpoint_url,
            "queryParams": [],
            "bodyParams": [],
            "response": ui_response_model,
            "ui_name": ui_name,
            "cluster_name": model,
            "endpoint_name":endpoint_name,
            "is_single_entity":True
        },
        {
            "method": "post",
            "url": endpoint_url,
            "queryParams": [],
            "bodyParams": body_params,
            "response": ui_response_model,
            "ui_name": ui_name,
            "cluster_name": model,
            "endpoint_name":endpoint_name,
            "is_single_entity":True
        },
        {
            "method": "put",
            "url": endpoint_url,
            "queryParams": [],
            "bodyParams": body_params,
            "response": ui_response_model,
            "ui_name": ui_name,
            "cluster_name": model,
            "endpoint_name":endpoint_name,
            "is_single_entity":True
        },
        {
            "method": "delete",
            "url": endpoint_url,
            "queryParams": query_params,
            "bodyParams": [],
            "response": ui_response_model,
            "ui_name": ui_name,
            "cluster_name": model,
            "endpoint_name":endpoint_name,
            "is_single_entity":True
        },
        ]
        crud_out = {
            model:endpoint_object
        }
        self.namespaces[model] = '{0}_namespace'.format(model.lower())
        return crud_out,self.create_api_header([model])+'\n\
{1}_namespace = Namespace("{0}", description="{0} Api") \n\
\n\
\n\
{1}_model ={1}_namespace.model("{1}",convert_db_model_to_restx_model({0})) \n\
{3}\n\
\n\
@{1}_namespace.route("/")\n\
class {0}Api(Resource):\n\
\n\
    @{1}_namespace.marshal_list_with({1}_model) \n\
    def get(self):\n\
        {1}s = db.session.query({0}).all()\n\
        return {1}s , 200  \n\
\n\
    @{1}_namespace.marshal_with({1}_model) \n\
    @{1}_namespace.expect({1}_model) \n\
    def post(self):\n\
        {1} = {0}({2})\n\
        db.session.add({1})\n\
        db.session.commit()    \n\
        return {1} , 201 \n\
\n\
    @{1}_namespace.marshal_with({1}_model) \n\
    @{1}_namespace.expect({1}_model) \n\
    def put(self):\n\
        db.session.query({0}).filter({0}.id==id).update(request.json) \n\
        db.session.commit() \n\
        {1} = db.session.query({0}).filter({0}.id==id).first() \n\
        return {1} , 200    \n\
\n\
    @{1}_namespace.marshal_with({1}_model) \n\
    @{1}_namespace.expect({1}_id_parser) \n\
    def delete(self):\n\
        {1} = db.session.query({0}).filter({0}.id==id).first() \n\
        db.session.query({0}).filter({0}.id==id).delete() \n\
        db.session.commit() \n\
        return {1} , 200    \n\
\n\
'.format(model,model.lower(),model_create_string,parser_create_string)
    
        
    def create_api_namespaces(self):
        namespaces_imports=''
        namespaces_init=''  
        for model,namespace in self.namespaces.items():
            namespaces_imports+= 'from .{0}_api import {1} \n\
'.format(model,namespace)
            namespaces_init+='rest_plus_api.add_namespace({0},path="/{1}s")\n\
    '.format(namespace,model.lower())

        return namespaces_imports,namespaces_init
    
    def create_api_init(self):
        namespaces_imports,namespaces_init=self.create_api_namespaces()
        api = '\
from flask_restx import Api \n\
\n\
\n\
def api_namespaces(blueprint,url_prefix,title): \n\
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) \n\
    {0}\
\
'.format(namespaces_init)
        return api ,namespaces_imports
    def create_app(self):
        return '\n\
from flask import Flask \n\
from flask_sqlalchemy import SQLAlchemy \n\
from sqlalchemy import create_engine \n\
from decouple import config \n\
\n\
user=config("user") \n\
password=config("password") \n\
database=config("database") \n\
db = SQLAlchemy() \n\
connection_string = "mysql+mysqlconnector://{0}:{1}@127.0.0.1:3306".format(user, password) \n\
def create_app(): \n\
    app = Flask(__name__) \n\
    settings = dict() \n\
    settings["SQLALCHEMY_DATABASE_URI"] = connection_string+"/{0}".format(database) \n\
    settings["SQLALCHEMY_TRACK_MODIFICATIONS"] = False \n\
    app.config.update(settings) \n\
    return app \n\
\n\
def create_db(app): \n\
    with app.app_context(): \n\
        db.init_app(app) \n\
        engine = create_engine(connection_string) \n\
        create_str = "CREATE DATABASE IF NOT EXISTS `{0}` ;".format(database) \n\
        engine.execute(create_str) \n\
        engine.execute("USE `{0}`;".format(database)) \n\
        db.create_all(bind="__all__", app=app) \n\
        db.session.commit() \n\
        return db \n\
\n\
'
    def create_app_init(self):
        return ' \n\
from flask import Blueprint \n\
from flask_migrate import Migrate \n\
from app import create_app, create_db, db \n\
from apis import api_namespaces \n\
app = create_app() \n\
from models import * \n\
db = create_db(app) \n\
migrate = Migrate(app, db) \n\
\n\
\n\
prefix = "/api" \n\
API = Blueprint("api", __name__, url_prefix=prefix) \n\
rest_api= api_namespaces(blueprint=API, url_prefix=prefix,title="Main Api") \n\
app.register_blueprint(API, url_prefix=prefix) \n\
'
    def create_app_requirements(self):
        return ' \n\
Flask==2.0.2 \n\
Flask_Migrate==3.1.0 \n\
flask_restx==0.5.1 \n\
Flask_SQLAlchemy==2.5.1 \n\
python-decouple==3.5 \n\
SQLAlchemy==1.4.27 \n\
mysql-connector \n\
'
    def create_app_run(self):
        return ' \n\
export PYTHONPATH=$PWD \n\
export FLASK_APP=__init__.py \n\
export FLASK_DEBUG=1 \n\
source venv/bin/activate \n\
\n\
python -m flask run --host=localhost --port=3000 \n\
'
    def create_app_setup(self):
        return ' \n\
pip install virtualenv \n\
virtualenv venv \n\
source venv/bin/activate \n\
pip install -r requirements.txt \n\
'
    def create_app_utils(self):
        return ' \n\
from flask_restx import fields \n\
def convert_db_model_to_restx_model(model): \n\
\n\
    fields_dict = {} \n\
    for column in model.__table__.columns: \n\
        if column.type.python_type == int: \n\
            fields_dict[column.name] = fields.Integer() \n\
        elif column.type.python_type == str: \n\
            fields_dict[column.name] = fields.String() \n\
        elif column.type.python_type == float: \n\
            fields_dict[column.name] = fields.Float() \n\
        elif column.type.python_type == bool: \n\
            fields_dict[column.name] = fields.Boolean() \n\
        elif column.type.python_type == list: \n\
            fields_dict[column.name] = fields.List(fields.String()) \n\
        elif column.type.python_type == dict: \n\
            fields_dict[column.name] = fields.String() \n\
        else: \n\
            fields_dict[column.name] = fields.String() \n\
    return fields_dict \n\
'
    def create_api_structure(self,api_name,route_path,models):
        namespaces_imports = 'from .{0}_api import {0}_namespace \n\
'.format(api_name)
        api_init_namespace = '\n\
    rest_plus_api.add_namespace({0}_namespace,path="/{1}s")'.format(api_name,route_path)
        api_namespace = self.create_api_header(models)+'\n\
{0}_namespace = Namespace("{0}", description="{0} Api") \n\
'.format(api_name)

        return api_init_namespace,api_namespace,namespaces_imports
