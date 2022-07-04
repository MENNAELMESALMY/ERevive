from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Role 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
role_namespace = Namespace("Role", description="Role Api") 


role_model =role_namespace.model("role",convert_db_model_to_restx_model(Role)) 
role_id_parser = reqparse.RequestParser() 
role_id_parser.add_argument('name',type=str)


@role_namespace.route("/")
class RoleApi(Resource):

    def get(self):
        try:
            roles = db.session.query(Role).all()
            roles = [row.serialize() for row in roles]
            return roles , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @role_namespace.expect(role_model) 
    def post(self):
        try:
            roles = Role(description = request.json.get("description"),name = request.json.get("name"))
            db.session.add(roles)
            db.session.commit()    
            return roles.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @role_namespace.expect(role_model) 
    def put(self):
        try:
            db.session.query(Role).filter(Role.name==request.json.get('name') ).update(request.json) 
            db.session.commit() 
            roles = db.session.query(Role).filter(Role.name==request.json.get('name') ).first() 
            return roles.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @role_namespace.expect(role_id_parser) 
    def delete(self):
        try:
            roles = db.session.query(Role).filter(Role.name==role_id_parser.parse_args().get('name') ).first() 
            db.session.query(Role).filter(Role.name==role_id_parser.parse_args().get('name') ).delete() 
            db.session.commit() 
            return roles.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

