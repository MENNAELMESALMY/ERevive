from flask.helpers import make_response 
from flask_restx import Resource, Namespace 
from flask import jsonify, request 
from models import DEPENDENT 
from app import db 
from utils import convert_db_model_to_restx_model 
            
dependents_namespace = Namespace("DEPENDENT", description="DEPENDENT Api") 


dependent_model =dependents_namespace.model("dependent",convert_db_model_to_restx_model(DEPENDENT)) 

@dependents_namespace.route("/")
class DEPENDENTApi(Resource):

    @dependents_namespace.marshal_list_with(dependent_model) 
    def get(self):
        dependents = db.session.query(DEPENDENT).all()
        return dependents , 200  

    @dependents_namespace.marshal_with(dependent_model) 
    @dependents_namespace.expect(dependent_model) 
    def post(self):
        dependent = DEPENDENT(sex = request.json.get("sex"),relatlonship = request.json.get("relatlonship"),name = request.json.get("name"),birth_date = request.json.get("birth_date"),Dependents_EMPLOYEE_ = request.json.get("Dependents_EMPLOYEE_"))
        db.session.add(dependent)
        db.session.commit()    
        return dependent , 201 


@dependents_namespace.route("/<id>")
class DEPENDENTsApi(Resource):

    @dependents_namespace.marshal_with(dependent_model) 
    def get(self, id):
        dependent = db.session.query(DEPENDENT).filter(DEPENDENT.id==id).first() 
        return dependent , 200    

    @dependents_namespace.marshal_with(dependent_model) 
    @dependents_namespace.expect(dependent_model) 
    def put(self, id):
        db.session.query(DEPENDENT).filter(DEPENDENT.id==id).update(request.json) 
        db.session.commit() 
        dependent = db.session.query(DEPENDENT).filter(DEPENDENT.id==id).first() 
        return dependent , 200    

    @dependents_namespace.marshal_with(dependent_model) 
    def delete(self,id):
        dependent = db.session.query(DEPENDENT).filter(DEPENDENT.id==id).first() 
        db.session.query(DEPENDENT).filter(DEPENDENT.id==id).delete() 
        db.session.commit() 
        return dependent , 200    
        