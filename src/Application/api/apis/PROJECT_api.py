from flask.helpers import make_response 
from flask_restx import Resource, Namespace 
from flask import jsonify, request 
from models import PROJECT 
from app import db 
from utils import convert_db_model_to_restx_model 
            
projects_namespace = Namespace("PROJECT", description="PROJECT Api") 


project_model =projects_namespace.model("project",convert_db_model_to_restx_model(PROJECT)) 

@projects_namespace.route("/")
class PROJECTApi(Resource):

    @projects_namespace.marshal_list_with(project_model) 
    def get(self):
        projects = db.session.query(PROJECT).all()
        return projects , 200  

    @projects_namespace.marshal_with(project_model) 
    @projects_namespace.expect(project_model) 
    def post(self):
        project = PROJECT(location = request.json.get("location"),name = request.json.get("name"),budget = request.json.get("budget"),DEPARTMENT_Assigned_name = request.json.get("DEPARTMENT_Assigned_name"))
        db.session.add(project)
        db.session.commit()    
        return project , 201 


@projects_namespace.route("/<id>")
class PROJECTsApi(Resource):

    @projects_namespace.marshal_with(project_model) 
    def get(self, id):
        project = db.session.query(PROJECT).filter(PROJECT.id==id).first() 
        return project , 200    

    @projects_namespace.marshal_with(project_model) 
    @projects_namespace.expect(project_model) 
    def put(self, id):
        db.session.query(PROJECT).filter(PROJECT.id==id).update(request.json) 
        db.session.commit() 
        project = db.session.query(PROJECT).filter(PROJECT.id==id).first() 
        return project , 200    

    @projects_namespace.marshal_with(project_model) 
    def delete(self,id):
        project = db.session.query(PROJECT).filter(PROJECT.id==id).first() 
        db.session.query(PROJECT).filter(PROJECT.id==id).delete() 
        db.session.commit() 
        return project , 200    
        