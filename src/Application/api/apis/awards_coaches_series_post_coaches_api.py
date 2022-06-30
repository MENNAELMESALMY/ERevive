from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_coaches , series_post , coaches 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
awards_coaches_series_post_coaches_namespace = Namespace("awards_coaches_series_post_coaches", description="awards_coaches_series_post_coaches Api") 
get_awards_coaches_series_post_coaches_filteredby_id_parser = reqparse.RequestParser()
get_awards_coaches_series_post_coaches_filteredby_id_parser.add_argument('awards_coaches.id', type=str, required=True, location='args')

@awards_coaches_series_post_coaches_namespace.route('/get_awards_coaches_series_post_coaches_filteredby_id', methods=['GET'])
class get_awards_coaches_series_post_coaches_filteredby_id_resource(Resource):
    
    @awards_coaches_series_post_coaches_namespace.expect(get_awards_coaches_series_post_coaches_filteredby_id_parser)
    def get(self):
        args = get_awards_coaches_series_post_coaches_filteredby_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(awards_coaches, series_post, coaches)\
				.join(coaches, awards_coaches.coachID == coaches.coachID)\
				.filter(awards_coaches.id == args['awards_coaches.id']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@awards_coaches_series_post_coaches_namespace.route('/get_awards_coaches_series_post_coaches', methods=['GET'])
class get_awards_coaches_series_post_coaches_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(awards_coaches, awards_coaches.id)\
				.join(coaches, awards_coaches.coachID == coaches.coachID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

