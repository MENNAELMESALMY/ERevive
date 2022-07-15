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
        crud_ui_out = {}
        for model in self.models.keys():
            crud_ui,api = self.create_api(model,self.models[model])
            crud_ui_out.update(crud_ui)
            Apis[model.lower()] = api
        self.api_files = Apis
        return Apis,crud_ui_out
        
    def create_api_header(self,models):
        model_import = ' , '.join(models)
        return '\
from datetime import datetime \n\
from flask.helpers import make_response \n\
from flask_restx import Resource, Namespace , reqparse \n\
from flask import jsonify, request \n\
from sqlalchemy import func,desc,asc \n\
from models import {0} \n\
from app import db \n\
from utils import convert_db_model_to_restx_model , serialize \n\
            '.format(model_import)

    def create_api(self,model,attributes): 
        model_create_string=''
        parser_create_string='{0}_id_parser = reqparse.RequestParser() \n'.format(model.lower())
        primary_keys = self.modelsObjects[model]['primaryKey']
        put_filter_primary_keys = ""
        delete_filter_primary_keys = ""
        get_check = ""
        body_params = []
        query_params = []
        ui_response_model = {}
        update_model = "data = request.json.copy()\n"
        self.crud_clusters.update({model.lower():[]})
        for attribute in attributes:
            terminal_command = ','
            type = self.modelsObjects[model]['attributes'][attribute]
            ui_response_model[attribute]=type
            if attribute == attributes[-1]:
                terminal_command = ''
            if attribute in primary_keys:
                parser_create_string+= "{0}_id_parser.add_argument('{1}',type={2},location = 'args')\n".format(model.lower(),attribute,type)
                query_params.append((attribute,type))
                update_model+="            data.pop('{0}',None)\n".format(attribute)
                put_filter_primary_keys+="{0}.{1}==request.json.get('{1}') and ".format(model,attribute)
                delete_filter_primary_keys+="{0}.{1}=={2}_id_parser.parse_args().get('{1}') and ".format(model,attribute,model.lower())
                get_check += "{0}_id_parser.parse_args().get('{1}') and ".format(model.lower(),attribute)
            body_params.append((attribute,type))
            model_create_string+='{0} = request.json.get("{0}")'.format(attribute)+terminal_command   
        endpoint_name,ui_name = model,model
        endpoint_url = '/'+model.lower()
        put_filter_primary_keys = put_filter_primary_keys[:-4]
        delete_filter_primary_keys = delete_filter_primary_keys[:-4]
        get_check = get_check[:-4]
        endpoint_object = [{
            "method": "get",
            "url": endpoint_url.lower(),
            "queryParams": [],
            "bodyParams": [],
            "response": ui_response_model,
            "ui_name": "get_"+ui_name.lower(),
            "cluster_name": model.lower(),
            "endpoint_name":"get_"+endpoint_name.lower(),
            "is_single_entity":True
        },
        {
            "method": "post",
            "url": endpoint_url.lower(),
            "queryParams": [],
            "bodyParams": body_params,
            "response": ui_response_model,
            "ui_name": "create_"+ui_name.lower(),
            "cluster_name": model.lower(),
            "endpoint_name":"create_"+endpoint_name.lower(),
            "is_single_entity":True
         },
        {
            "method": "put",
            "url": endpoint_url.lower(),
            "queryParams": [],
            "bodyParams": body_params,
            "response": ui_response_model,
            "ui_name": "update_"+ui_name.lower(),
            "cluster_name": model.lower(),
            "endpoint_name":"update_"+endpoint_name.lower(),
            "is_single_entity":True
        },
        {
            "method": "delete",
            "url": endpoint_url.lower(),
            "queryParams": query_params,
            "bodyParams": [],
            "response": ui_response_model,
            "ui_name": "delete_"+ui_name.lower(),
            "cluster_name": model.lower(),
            "endpoint_name":"delete_"+endpoint_name.lower(),
            "is_single_entity":True
        },
        ]
        crud_out = {
            model.lower():endpoint_object
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
    @{1}_namespace.expect({1}_id_parser) \n\
    def get(self):\n\
        try:\n\
            if {7}:\n\
                {1} = db.session.query({0}).filter({5}).first() \n\
                if not {1}: \n\
                    return "not found" , 404\n\
                return {1}.serialize() , 200 \n\
            else:\n\
                {1}s = db.session.query({0}).all()\n\
                if not {1}s: \n\
                    return "no data found" , 404\n\
                {1}s = [row.serialize() for row in {1}s]\n\
                return {1}s , 200 \n\
        except Exception as e:\n\
            print(e)\n\
            return str(e) , 400\n\
\n\
    @{1}_namespace.expect({1}_model) \n\
    def post(self):\n\
        try:\n\
            {1}s = {0}({2})\n\
            db.session.add({1}s)\n\
            db.session.commit()    \n\
            return {1}s.serialize() , 201 \n\
        except Exception as e:\n\
            print(e)\n\
            return str(e) , 400\n\
\n\
    @{1}_namespace.expect({1}_model) \n\
    def put(self):\n\
        try:\n\
            {6}\n\
            db.session.query({0}).filter({4}).update(data) \n\
            db.session.commit() \n\
            {1}s = db.session.query({0}).filter({4}).first() \n\
            return {1}s.serialize() , 200 \n\
        except Exception as e:\n\
            print(e)\n\
            return str(e) , 400\n\
\n\
    @{1}_namespace.expect({1}_id_parser) \n\
    def delete(self):\n\
        try:\n\
            {1}s = db.session.query({0}).filter({5}).first() \n\
            if not {1}s:\n\
                return "not found" , 404\n\
            db.session.query({0}).filter({5}).delete() \n\
            db.session.commit() \n\
            return {1}s.serialize() , 200 \n\
        except Exception as e:\n\
            print(e)\n\
            return str(e) , 400\n\
\n\
'.format(model,model.lower(),model_create_string,parser_create_string,put_filter_primary_keys,delete_filter_primary_keys,update_model,get_check)
    
        
    def create_api_namespaces(self):
        namespaces_imports=''
        namespaces_init=''  
        for model,namespace in self.namespaces.items():
            namespaces_imports+= 'from .{0}_api import {1} \n\
'.format(model.lower(),namespace)
            namespaces_init+='rest_plus_api.add_namespace({0},path="/{1}")\n\
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
from flask_cors import CORS \n\
from sqlalchemy_schemadisplay import create_schema_graph\n\
from sqlalchemy.sql import text\n\
import os\n\
\n\
user=config("user") \n\
password=config("password") \n\
database=config("database") \n\
db = SQLAlchemy() \n\
connection_string = "mysql+mysqlconnector://{0}:{1}@127.0.0.1:3306".format(user, password) \n\
def create_app(): \n\
    app = Flask(__name__) \n\
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})\n\
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
        graph = create_schema_graph(metadata= db.metadata,show_datatypes=False,show_indexes=False,rankdir="LR",concentrate=False)\n\
        graph.write_png("generated_schema.png")\n\
        return db \n\
\n\
def run_seeds():\n\
    seeds_folder = "seeds"\n\
    seeds_files = os.listdir(seeds_folder)\n\
    seeds_files.sort()\n\
    for seed_file in seeds_files:\n\
        seed_file_path = os.path.join(seeds_folder, seed_file)\n\
        with open(seed_file_path, "r") as f:\n\
            sql = f.read()\n\
        db.engine.execute(text(sql))\n\
        db.session.commit()\n\
\n\
'
    def create_app_init(self):
        return ' \n\
from flask import Blueprint , jsonify \n\
from flask_migrate import Migrate \n\
from app import create_app, create_db, db , run_seeds\n\
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
\n\
@app.get("/seeds")\n\
def seeds():\n\
    try:\n\
        run_seeds()\n\
        return jsonify({"status": "seeds runned"})\n\
    except Exception as e:\n\
        return jsonify({"status": "error", "error": str(e)})\n\
\n\
@app.route("/", methods=["OPTIONS"])\n\
def options():\n\
    return jsonify({"message": "options"})\n\
\n\
@app.errorhandler(500)\n\
def internal_error(error):\n\
    return jsonify({"message": "500 error"})\n\
\n\
if __name__ == "__main__":\n\
    app.run(debug=True, port=3000)@app.get("/seeds")\n\
\n\
'
    def create_app_requirements(self):
        return ' \n\
Flask==2.0.2 \n\
Flask_Migrate==3.1.0 \n\
flask_restx==0.5.1 \n\
Flask_SQLAlchemy==2.5.1 \n\
python-decouple==3.5 \n\
SQLAlchemy==1.4.27 \n\
mysql-connector-python \n\
sqlalchemy_schemadisplay\n\
flask-cors\n\
'
    def create_app_run(self):
        return ' \n\
. venv/bin/activate \n\
python __init__.py\n\
\n\
'
    def create_app_setup(self):
        return ' \n\
pip install virtualenv \n\
virtualenv venv \n\
. venv/bin/activate \n\
pip install -r requirements.txt \n\
'
    def create_app_utils(self):
        return ' \n\
from datetime import datetime \n\
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
\n\
def serialize_result(res):\n\
    res_dict = res._asdict() if hasattr(res, "_asdict") else res.__dict__ if hasattr(res, "__dict__") else res\n\
    table = None\n\
    if res_dict.get("_sa_instance_state"):\n\
        table = res_dict["_sa_instance_state"].class_.__table__.name+"."\n\
\n\
    res_dict.pop("_sa_instance_state", None)\n\
    serialized_result = res_dict.copy()\n\
    for attr_key, attr_value in res_dict.items():\n\
        print(attr_key, attr_value)\n\
        if isinstance(attr_value,datetime): \n\
            serialized_result[attr_key] = str(attr_value) \n\
            attr_value = str(attr_value) \n\
        if hasattr(attr_value, "__dict__"):\n\
            model_dict = attr_value.serialize()\n\
            model_dict_updated = {}\n\
            for key, value in model_dict.items():\n\
                model_dict_updated[attr_key + "." + key] = value\n\
            model_dict_updated = serialize_result(model_dict_updated)\n\
            serialized_result.pop(attr_key)\n\
            serialized_result.update(model_dict_updated)\n\
        elif table:\n\
            serialized_result[table+attr_key] = attr_value\n\
            serialized_result.pop(attr_key)\n\
\n\
    return serialized_result\n\
\n\
def serialize(results):\n\
\n\
    return [serialize_result(row) for row in results]\n\
\n\
'
    def create_api_structure(self,api_name,route_path,models):
        namespaces_imports = 'from .{0}_api import {0}_namespace \n\
'.format(api_name.lower())
        api_init_namespace = '\n\
    rest_plus_api.add_namespace({0}_namespace,path="/{1}")'.format(api_name.lower(),route_path.lower())
        api_namespace = self.create_api_header(models)+'\n\
{0}_namespace = Namespace("{0}", description="{0} Api") \n\
'.format(api_name)

        return api_init_namespace,api_namespace,namespaces_imports

