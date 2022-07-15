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
export PYTHONPATH=$PWD \n\
export FLASK_APP=__init__.py \n\
export FLASK_DEBUG=0 \n\
. venv/bin/activate \n\
\n\
python -m flask run --host=localhost --port=3000 \n\
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

    def create_generate_data(self):
        return ' \n\
import difflib \n\
import random \n\
import json \n\
import re \n\
import datetime \n\
import itertools \n\
import timeit \n\
import os \n\
import shutil \n\
from nltk.stem import PorterStemmer \n\
from nltk.corpus import stopwords \n\
from sqlalchemy import create_engine \n\
from faker_classes import faker_classes_mapper , pk_faker_classes \n\n\n\
def clean_word(colName , stopwords): \n\
    if len(colName) <= 1: \n\
        return colName \n\n\
    result = re.search("^[ 0-9]+$", colName) \n\
    if result is not None: \n\
        return colName \n\n\
    colName = re.sub("[0-9]+$", "", colName) \n\n\
    colName = colName.replace("_"," ") \n\n\
    colName = colName.replace("-"," ") \n\n\
    if colName.isupper() == True or len(colName.split()) > 1: \n\
        colName = colName.lower() \n\n\
    if re.search("^[a-z]+[A-Z]+", colName) is not None: \n\
        words = re.findall("[A-Z][^A-Z]*", colName) \n\
        if len(words) > 1 and len(words[0]) == 1 and len(words[1]) == 1: \n\
            result = "".join(words) \n\
        else: \n\
            result = " ".join(words) \n\
        colName = colName.split(re.findall("[A-Z][^A-Z]*", colName)[0])[0]+" " + result \n\
        colName = colName.lower() \n\n\
    if len(re.findall("[A-Z][^A-Z]*", colName)) >0: \n\
        words = re.findall("[A-Z][^A-Z]*", colName) \n\
        newWords = []  \n\
        i = 0 \n\
        while i<len(words): \n\
            if i+1<len(words) and len(words[i])==1 and len(words[i+1])==1: \n\
                newWords.append(words[i]+words[i+1]) \n\
                i+=1 \n\
            else: \n\
                newWords.append(words[i]) \n\
            i+=1 \n\
        colName = " ".join(newWords) \n\n\
    colName = " ".join(colName.split()) \n\
    colName = colName.lower() \n\n\
    colName = colName.split(" ") \n\n\
    porter = PorterStemmer() \n\
    colName = [porter.stem(word) for word in colName if word not in stopwords] \n\n\
    return colName \n\n\n\
def match(attr,faker_class): \n\
    max_len = max(len(attr),len(faker_class)) \n\
    score = 0 \n\
    if max_len == 0: \n\
        return score \n\
    for word in attr: \n\
        if word in faker_class: \n\
            score += 1 \n\
    return score/max_len \n\n\n\
def get_keys_attrs(model): \n\
    pk_is_a_fk = False \n\
    attributes = model["attributes"].copy() \n\
    primary_keys = {2} \n\
    foriegn_keys = {2} \n\
    for fk in model["ForgeinKey"]: \n\
        foriegn_keys[fk["attributeName"]] = fk \n\
        del attributes[fk["attributeName"]] \n\
    for pk in model["primaryKey"]: \n\
        if pk in attributes.keys(): \n\
            primary_keys[pk] = attributes[pk] \n\
            del attributes[pk] \n\
        else: \n\
            pk_is_a_fk = True \n\n\
    return attributes, primary_keys, foriegn_keys, pk_is_a_fk \n\n\n\
def mapping_model_to_faker(stop_words, classes, attributes, primary_keys): \n\
    attr_pk = (attributes.copy()) \n\
    attr_pk.update(primary_keys) \n\
    attr_pk_mapping= {2} \n\n\
    for attr , datatype in attr_pk.items(): \n\
        attr_cleaned = clean_word(attr,stop_words) \n\
        max_score,best_match = 0,None \n\n\
        for faker_class in faker_classes_mapper.keys(): \n\
            faker_class_cleaned = clean_word(faker_class,stop_words) \n\
            score = match(attr_cleaned,faker_class_cleaned) \n\n\
            value = faker_classes_mapper[faker_class]() \n\
            same_type = isinstance(value,classes[datatype]) \n\n\
            if score > max_score and same_type: \n\
                max_score = score \n\
                best_match = faker_class \n\n\
        if not best_match: \n\
            best_match = datatype \n\n\
        attr_pk_mapping[attr] = best_match \n\n\
    return attr_pk_mapping \n\n\n\
def fill_model_statment(num_of_records, attr_pk_mapping, primary_keys): \n\
    pk = primary_keys \n\
    values = [] \n\
    i = 0 \n\
    stmt = "" \n\
    for attr,faker_class in attr_pk_mapping.items(): \n\
        if attr in pk: \n\
            continue \n\n\
        stmt += attr +", " \n\
        values.append([]) \n\
        for _ in range(num_of_records): \n\
            value = faker_classes_mapper[faker_class]() \n\n\
            if isinstance(value,str) or isinstance(value,datetime.datetime): \n\
                values[i].append(str(value)) \n\
            else: \n\
                values[i].append(value) \n\n\
        i+=1 \n\n\
    stmt = stmt[:-2] if len(stmt) else stmt \n\n\
    return values,stmt \n\n\n\
def get_pk_data(primary_keys,attr_pk_mapping,num_of_records): \n\
    values = {2} \n\
    for i,pk in enumerate(primary_keys): \n\
        values[pk] = [] \n\
        faker_class = attr_pk_mapping[pk] \n\
        for _ in range(num_of_records): \n\
            value = pk_faker_classes[faker_class]() \n\
            if isinstance(value,str) or isinstance(value,datetime.datetime): \n\
                values[pk].append(str(value)) \n\
            else: \n\
                values[pk].append(value) \n\
    return values \n\
def get_fk_data(model,pks_data,num_of_records,is_pk_and_fk): \n\
    stmt = "" \n\
    values = [] \n\
    for fk in model: \n\
        stmt += fk["attributeName"] + ", " \n\
        table = fk["ForignKeyTable"] \n\
        attr = fk["ForignKeyTableAttributeName"] \n\
        pk = pks_data[table][attr] \n\
        if is_pk_and_fk: \n\
            pk = random.sample(pk, k = num_of_records) \n\
            print(pk) \n\
        else: \n\
            pk = random.choices(pk , k = num_of_records) \n\
        values.append(pk) \n\
    return values,stmt[:-2] \n\n\n\
def get_insert_stmt(num_of_records,model_mapping,primary_keys,model_name,database,pks_data): \n\
    attr_data, attr_stmt = fill_model_statment(num_of_records, model_mapping, primary_keys) \n\
    #fk_data,fk_stmt = get_fk_data(model["ForgeinKey"],pks_data,num_of_records) \n\
    row_values = list(pks_data[model_name].values()) \n\n\
    if len(attr_data): row_values.extend(attr_data) \n\
    #if len(fk_data): row_values.extend(fk_data) \n\
    row_values = list(zip(*row_values)) \n\n\
    insert_stmt = "INSERT INTO {3}.{4} (".format(database,model_name) \n\
    for pk in primary_keys: \n\
        insert_stmt +=  pk + ", " \n\n\
    insert_stmt = insert_stmt[:-2] \n\
    if attr_stmt: insert_stmt += ", " + attr_stmt \n\
    insert_stmt += ") VALUES {3};".format(str(row_values)[1:-1]) \n\n\
    return insert_stmt \n\n\n\
def __main__(database): \n\
    with open("./modelsObjects.json","r") as file: \n\
        models = json.load(file) \n\n\
    classes = {5} \n\
        "str":str, \n\
        "int":int, \n\
        "float":float, \n\
        "bool":bool, \n\
        "datetime":datetime.datetime \n\
    {6} \n\n\
    stop_words = stopwords.words("english") \n\
    attr_pk_mapping = {2} \n\
    models_fk = {2} \n\
    models_pk = {2} \n\
    num_of_records = 100 \n\n\n\
    pks_data = {2} \n\
    weak_pk = [] \n\
    stmts = [] \n\n\
    for model_name , model in models.items(): \n\
        attributes, primary_keys, foriegn_keys, pk_is_a_fk = get_keys_attrs(model) \n\n\
        if pk_is_a_fk: \n\
            weak_pk.append(model_name) \n\
            print(attributes, primary_keys, foriegn_keys) \n\n\
        models_fk[model_name] = foriegn_keys \n\
        models_pk[model_name] = list(primary_keys.keys()) \n\
        attr_pk_mapping[model_name] = mapping_model_to_faker(stop_words, classes, attributes, primary_keys) \n\
        pks_data[model_name] = get_pk_data(primary_keys,attr_pk_mapping[model_name],num_of_records) \n\n\
    weak_entites = [] \n\
    for model_name,model in models.items(): \n\
        if model_name in weak_pk: \n\
            print(model_name) \n\
            continue \n\n\
        insert_stmt = get_insert_stmt(num_of_records, attr_pk_mapping[model_name],models_pk[model_name],model_name,database,pks_data) \n\
        stmts.append(insert_stmt.replace("),","),").replace("VALUES","VALUES")) \n\n\
    for model_name,model in models.items(): \n\
        if  len(model["ForgeinKey"]) == 0: continue \n\
        fk_data,fk_stmt = get_fk_data(model["ForgeinKey"],pks_data,num_of_records,(model_name in weak_pk)) \n\
        row_values = list(pks_data[model_name].values()) \n\n\
        if len(fk_data): row_values.extend(fk_data) \n\n\
        attr_stmt = "" \n\
        if model_name in weak_pk: \n\
            attr_data, attr_stmt = fill_model_statment(num_of_records, attr_pk_mapping[model_name], models_pk[model_name]) \n\
            if len(attr_stmt): \n\
                row_values.extend(attr_data) \n\n\
        row_values = list(zip(*row_values)) \n\
        insert_stmt = "INSERT INTO "+database+"."+model_name+" (".format(database,model_name) \n\
        for pk in models_pk[model_name]: \n\
            insert_stmt +=  pk + ", " \n\n\
        insert_stmt = insert_stmt[:-2] if len(models_pk[model_name]) else insert_stmt \n\
        if fk_stmt: insert_stmt += ", " + fk_stmt if len(models_pk[model_name]) else fk_stmt  \n\
        if attr_stmt: insert_stmt += ", " + attr_stmt \n\n\
        insert_stmt += ") VALUES "+str(row_values)[1:-1].replace("),","),")+" " \n\
        if model_name in weak_pk: \n\
            insert_stmt += ";" \n\
        else: \n\
            insert_stmt += " ON DUPLICATE KEY UPDATE " \n\
            fks_names = fk_stmt.split(", ") \n\
            for name in fks_names: \n\
                insert_stmt +=  " "+name+" = VALUES("+name+"), " .format(name) \n\
            insert_stmt = insert_stmt[:-2] +";" \n\n\
        stmts.append(insert_stmt) \n\n\
    currentPath = os.getcwd()  \n\
    seedspath = os.path.join(currentPath, "api/seeds") \n\
    if not os.path.exists(seedspath): \n\
        os.makedirs(seedspath) \n\
    else: \n\
        shutil.rmtree(seedspath, ignore_errors=True) \n\
        os.makedirs(seedspath) \n\n\
    count = 0 \n\
    for stmt in stmts: \n\
        path = seedspath +"/"+ str(count)+".sql" \n\n\
        with open(path,"w+") as file:  \n\
            file.write(stmt) \n\
        count += 1 \n\
__main__("{1}") \n\
'.format("" , self.db, "{"+"}" , "{"+"0}" , "{"+"1}" , "{","}")
