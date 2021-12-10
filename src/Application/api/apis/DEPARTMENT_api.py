from flask.helpers import make_response 
from flask_restx import Resource, Namespace 
from flask import jsonify, request 
from models import DEPARTMENT 
from app import db 
from utils import convert_db_model_to_restx_model 
            
departments_namespace = Namespace("DEPARTMENT", description="DEPARTMENT Api") 


department_model =departments_namespace.model("department",convert_db_model_to_restx_model(DEPARTMENT)) 

@departments_namespace.route("/")
class DEPARTMENTApi(Resource):

    @departments_namespace.marshal_list_with(department_model) 
    def get(self):
        departments = db.session.query(DEPARTMENT).all()
        return departments , 200  

    @departments_namespace.marshal_with(department_model) 
    @departments_namespace.expect(department_model) 
    def post(self):
        department = DEPARTMENT(name = request.json.get("name"),start_date = request.json.get("start_date"),EMPLOYEE_Manages = request.json.get("EMPLOYEE_Manages"))
        db.session.add(department)
        db.session.commit()    
        return department , 201 


@departments_namespace.route("/<id>")
class DEPARTMENTsApi(Resource):

    @departments_namespace.marshal_with(department_model) 
    def get(self, id):
        department = db.session.query(DEPARTMENT).filter(DEPARTMENT.id==id).first() 
        return department , 200    

    @departments_namespace.marshal_with(department_model) 
    @departments_namespace.expect(department_model) 
    def put(self, id):
        db.session.query(DEPARTMENT).filter(DEPARTMENT.id==id).update(request.json) 
        db.session.commit() 
        department = db.session.query(DEPARTMENT).filter(DEPARTMENT.id==id).first() 
        return department , 200    

    @departments_namespace.marshal_with(department_model) 
    def delete(self,id):
        department = db.session.query(DEPARTMENT).filter(DEPARTMENT.id==id).first() 
        db.session.query(DEPARTMENT).filter(DEPARTMENT.id==id).delete() 
        db.session.commit() 
        return department , 200    
        