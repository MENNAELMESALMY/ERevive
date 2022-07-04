from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Department 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
department_namespace = Namespace("Department", description="Department Api") 


department_model =department_namespace.model("department",convert_db_model_to_restx_model(Department)) 
department_id_parser = reqparse.RequestParser() 
department_id_parser.add_argument('name',type=str)


@department_namespace.route("/")
class DepartmentApi(Resource):

    def get(self):
        try:
            departments = db.session.query(Department).all()
            departments = [row.serialize() for row in departments]
            return departments , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @department_namespace.expect(department_model) 
    def post(self):
        try:
            departments = Department(description = request.json.get("description"),name = request.json.get("name"))
            db.session.add(departments)
            db.session.commit()    
            return departments.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @department_namespace.expect(department_model) 
    def put(self):
        try:
            db.session.query(Department).filter(Department.name==request.json.get('name') ).update(request.json) 
            db.session.commit() 
            departments = db.session.query(Department).filter(Department.name==request.json.get('name') ).first() 
            return departments.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @department_namespace.expect(department_id_parser) 
    def delete(self):
        try:
            departments = db.session.query(Department).filter(Department.name==department_id_parser.parse_args().get('name') ).first() 
            db.session.query(Department).filter(Department.name==department_id_parser.parse_args().get('name') ).delete() 
            db.session.commit() 
            return departments.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

