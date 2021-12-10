from flask.helpers import make_response 
from flask_restx import Resource, Namespace 
from flask import jsonify, request 
from models import EMPLOYEE 
from app import db 
from utils import convert_db_model_to_restx_model 
            
employees_namespace = Namespace("EMPLOYEE", description="EMPLOYEE Api") 


employee_model =employees_namespace.model("employee",convert_db_model_to_restx_model(EMPLOYEE)) 

@employees_namespace.route("/")
class EMPLOYEEApi(Resource):

    @employees_namespace.marshal_list_with(employee_model) 
    def get(self):
        employees = db.session.query(EMPLOYEE).all()
        return employees , 200  

    @employees_namespace.marshal_with(employee_model) 
    @employees_namespace.expect(employee_model) 
    def post(self):
        employee = EMPLOYEE(last_name = request.json.get("last_name"),middle_initis = request.json.get("middle_initis"),first_name = request.json.get("first_name"),address = request.json.get("address"),salary = request.json.get("salary"),sex = request.json.get("sex"),status = request.json.get("status"),birth_dat = request.json.get("birth_dat"),ssn = request.json.get("ssn"),start_date = request.json.get("start_date"),DEPARTMENT_Employed_name = request.json.get("DEPARTMENT_Employed_name"),EMPLOYEE_Supervision_ = request.json.get("EMPLOYEE_Supervision_"))
        db.session.add(employee)
        db.session.commit()    
        return employee , 201 


@employees_namespace.route("/<id>")
class EMPLOYEEsApi(Resource):

    @employees_namespace.marshal_with(employee_model) 
    def get(self, id):
        employee = db.session.query(EMPLOYEE).filter(EMPLOYEE.id==id).first() 
        return employee , 200    

    @employees_namespace.marshal_with(employee_model) 
    @employees_namespace.expect(employee_model) 
    def put(self, id):
        db.session.query(EMPLOYEE).filter(EMPLOYEE.id==id).update(request.json) 
        db.session.commit() 
        employee = db.session.query(EMPLOYEE).filter(EMPLOYEE.id==id).first() 
        return employee , 200    

    @employees_namespace.marshal_with(employee_model) 
    def delete(self,id):
        employee = db.session.query(EMPLOYEE).filter(EMPLOYEE.id==id).first() 
        db.session.query(EMPLOYEE).filter(EMPLOYEE.id==id).delete() 
        db.session.commit() 
        return employee , 200    
        