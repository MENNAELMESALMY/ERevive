from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import draft 
from app import db 
from utils import convert_db_model_to_restx_model 
            
draft_namespace = Namespace("draft", description="draft Api") 


draft_model =draft_namespace.model("draft",convert_db_model_to_restx_model(draft)) 
draft_id_parser = reqparse.RequestParser() 
draft_id_parser.add_argument('id',type=str)


@draft_namespace.route("/")
class draftApi(Resource):

    @draft_namespace.marshal_list_with(draft_model) 
    def get(self):
        try:
            drafts = db.session.query(draft).all()
        except Exception as e:
            return None , 500
        return drafts , 200  

    @draft_namespace.marshal_with(draft_model) 
    @draft_namespace.expect(draft_model) 
    def post(self):
        try:
            drafts = draft(id = request.json.get("id"),draftYear = request.json.get("draftYear"),draftRound = request.json.get("draftRound"),draftSelection = request.json.get("draftSelection"),draftOverall = request.json.get("draftOverall"),tmID = request.json.get("tmID"),firstName = request.json.get("firstName"),lastName = request.json.get("lastName"),suffixName = request.json.get("suffixName"),playerID = request.json.get("playerID"),draftForm = request.json.get("draftForm"),lgID = request.json.get("lgID"))
            db.session.add(drafts)
            db.session.commit()    
        except Exception as e:
            return None , 500
        return drafts , 201 

    @draft_namespace.marshal_with(draft_model) 
    @draft_namespace.expect(draft_model) 
    def put(self):
        try:
            db.session.query(draft).filter(draft.id==request.json.get('id') ).update(request.json) 
            db.session.commit() 
            drafts = db.session.query(draft).filter(draft.id==request.json.get('id') ).first() 
        except Exception as e:
            return None , 500
        return drafts , 200    

    @draft_namespace.marshal_with(draft_model) 
    @draft_namespace.expect(draft_id_parser) 
    def delete(self):
        try:
            drafts = db.session.query(draft).filter(draft.id==draft_id_parser.parse_args().get('id') ).first() 
            db.session.query(draft).filter(draft.id==draft_id_parser.parse_args().get('id') ).delete() 
            db.session.commit() 
        except Exception as e:
            return None , 500
        return drafts , 200    

