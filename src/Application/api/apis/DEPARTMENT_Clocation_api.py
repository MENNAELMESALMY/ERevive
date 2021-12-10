from flask.helpers import make_response 
from flask_restx import Resource, Namespace 
from flask import jsonify, request 
from models import DEPARTMENT_Clocation 
from app import db 
from utils import convert_db_model_to_restx_model 
            
department_clocations_namespace = Namespace("DEPARTMENT_Clocation", description="DEPARTMENT_Clocation Api") 


department_clocation_model =department_clocations_namespace.model("department_clocation",convert_db_model_to_restx_model(DEPARTMENT_Clocation)) 

@department_clocations_namespace.route("/")
class DEPARTMENT_ClocationApi(Resource):

    @department_clocations_namespace.marshal_list_with(department_clocation_model) 
    def get(self):
        department_clocations = db.session.query(DEPARTMENT_Clocation).all()
        return department_clocations , 200  

    @department_clocations_namespace.marshal_with(department_clocation_model) 
    @department_clocations_namespace.expect(department_clocation_model) 
    def post(self):
        department_clocation = DEPARTMENT_Clocation(Clocation = request.json.get("Clocation"),DEPARTMENT_name = request.json.get("DEPARTMENT_name"))
        db.session.add(department_clocation)
        db.session.commit()    
        return department_clocation , 201 


@department_clocations_namespace.route("/<id>")
class DEPARTMENT_ClocationsApi(Resource):

    @department_clocations_namespace.marshal_with(department_clocation_model) 
    def get(self, id):
        department_clocation = db.session.query(DEPARTMENT_Clocation).filter(DEPARTMENT_Clocation.id==id).first() 
        return department_clocation , 200    

    @department_clocations_namespace.marshal_with(department_clocation_model) 
    @department_clocations_namespace.expect(department_clocation_model) 
    def put(self, id):
        db.session.query(DEPARTMENT_Clocation).filter(DEPARTMENT_Clocation.id==id).update(request.json) 
        db.session.commit() 
        department_clocation = db.session.query(DEPARTMENT_Clocation).filter(DEPARTMENT_Clocation.id==id).first() 
        return department_clocation , 200    

    @department_clocations_namespace.marshal_with(department_clocation_model) 
    def delete(self,id):
        department_clocation = db.session.query(DEPARTMENT_Clocation).filter(DEPARTMENT_Clocation.id==id).first() 
        db.session.query(DEPARTMENT_Clocation).filter(DEPARTMENT_Clocation.id==id).delete() 
        db.session.commit() 
        return department_clocation , 200    
        