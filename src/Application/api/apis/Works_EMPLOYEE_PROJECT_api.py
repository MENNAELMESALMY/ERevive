from flask.helpers import make_response 
from flask_restx import Resource, Namespace 
from flask import jsonify, request 
from models import Works_EMPLOYEE_PROJECT 
from app import db 
from utils import convert_db_model_to_restx_model 
            
works_employee_projects_namespace = Namespace("Works_EMPLOYEE_PROJECT", description="Works_EMPLOYEE_PROJECT Api") 


works_employee_project_model =works_employee_projects_namespace.model("works_employee_project",convert_db_model_to_restx_model(Works_EMPLOYEE_PROJECT)) 

@works_employee_projects_namespace.route("/")
class Works_EMPLOYEE_PROJECTApi(Resource):

    @works_employee_projects_namespace.marshal_list_with(works_employee_project_model) 
    def get(self):
        works_employee_projects = db.session.query(Works_EMPLOYEE_PROJECT).all()
        return works_employee_projects , 200  

    @works_employee_projects_namespace.marshal_with(works_employee_project_model) 
    @works_employee_projects_namespace.expect(works_employee_project_model) 
    def post(self):
        works_employee_project = Works_EMPLOYEE_PROJECT(start_date = request.json.get("start_date"),hours = request.json.get("hours"),EMPLOYEE_ = request.json.get("EMPLOYEE_"),PROJECT_ = request.json.get("PROJECT_"))
        db.session.add(works_employee_project)
        db.session.commit()    
        return works_employee_project , 201 


@works_employee_projects_namespace.route("/<id>")
class Works_EMPLOYEE_PROJECTsApi(Resource):

    @works_employee_projects_namespace.marshal_with(works_employee_project_model) 
    def get(self, id):
        works_employee_project = db.session.query(Works_EMPLOYEE_PROJECT).filter(Works_EMPLOYEE_PROJECT.id==id).first() 
        return works_employee_project , 200    

    @works_employee_projects_namespace.marshal_with(works_employee_project_model) 
    @works_employee_projects_namespace.expect(works_employee_project_model) 
    def put(self, id):
        db.session.query(Works_EMPLOYEE_PROJECT).filter(Works_EMPLOYEE_PROJECT.id==id).update(request.json) 
        db.session.commit() 
        works_employee_project = db.session.query(Works_EMPLOYEE_PROJECT).filter(Works_EMPLOYEE_PROJECT.id==id).first() 
        return works_employee_project , 200    

    @works_employee_projects_namespace.marshal_with(works_employee_project_model) 
    def delete(self,id):
        works_employee_project = db.session.query(Works_EMPLOYEE_PROJECT).filter(Works_EMPLOYEE_PROJECT.id==id).first() 
        db.session.query(Works_EMPLOYEE_PROJECT).filter(Works_EMPLOYEE_PROJECT.id==id).delete() 
        db.session.commit() 
        return works_employee_project , 200    
        