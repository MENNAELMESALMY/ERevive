from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_coaches 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
awards_coaches_namespace = Namespace("awards_coaches", description="awards_coaches Api") 


awards_coaches_model =awards_coaches_namespace.model("awards_coaches",convert_db_model_to_restx_model(awards_coaches)) 
awards_coaches_id_parser = reqparse.RequestParser() 
awards_coaches_id_parser.add_argument('id',type=str)


@awards_coaches_namespace.route("/")
class awards_coachesApi(Resource):

    def get(self):
        try:
            awards_coachess = db.session.query(awards_coaches).all()
            awards_coachess = [row.serialize() for row in awards_coachess]
            return awards_coachess , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @awards_coaches_namespace.expect(awards_coaches_model) 
    def post(self):
        try:
            awards_coachess = awards_coaches(id = request.json.get("id"),coachID = request.json.get("coachID"),award = request.json.get("award"),lgID = request.json.get("lgID"),note = request.json.get("note"))
            db.session.add(awards_coachess)
            db.session.commit()    
            return awards_coachess.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @awards_coaches_namespace.expect(awards_coaches_model) 
    def put(self):
        try:
            db.session.query(awards_coaches).filter(awards_coaches.id==request.json.get('id') ).update(request.json) 
            db.session.commit() 
            awards_coachess = db.session.query(awards_coaches).filter(awards_coaches.id==request.json.get('id') ).first() 
            return awards_coachess.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @awards_coaches_namespace.expect(awards_coaches_id_parser) 
    def delete(self):
        try:
            awards_coachess = db.session.query(awards_coaches).filter(awards_coaches.id==awards_coaches_id_parser.parse_args().get('id') ).first() 
            db.session.query(awards_coaches).filter(awards_coaches.id==awards_coaches_id_parser.parse_args().get('id') ).delete() 
            db.session.commit() 
            return awards_coachess.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400


@awards_coaches_namespace.route('/get_awards_coaches', methods=['GET'])
class get_awards_coaches_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(awards_coaches, awards_coaches.id.label('awards_coaches.id')).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@awards_coaches_namespace.route('/get_awards_coaches_filteredby_coachID_id', methods=['GET'])
class get_awards_coaches_filteredby_coachID_id_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(awards_coaches, awards_coaches.id.label('awards_coaches.id'))\
				.filter(awards_coaches.id == awards_coaches.coachID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

