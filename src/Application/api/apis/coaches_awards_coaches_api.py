from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import coaches , awards_coaches 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
coaches_awards_coaches_namespace = Namespace("coaches_awards_coaches", description="coaches_awards_coaches Api") 
get_coaches_awards_coaches_filteredby_year_parser = reqparse.RequestParser()
get_coaches_awards_coaches_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@coaches_awards_coaches_namespace.route('/get_coaches_awards_coaches_filteredby_year', methods=['GET'])
class get_coaches_awards_coaches_filteredby_year_resource(Resource):
    
    @coaches_awards_coaches_namespace.expect(get_coaches_awards_coaches_filteredby_year_parser)
    def get(self):
        args = get_coaches_awards_coaches_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID)\
				.join(awards_coaches, coaches.coachID == awards_coaches.coachID)\
				.filter(coaches.year == args['coaches.year']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@coaches_awards_coaches_namespace.route('/get_awards_coaches_coaches_groupedby_coachID', methods=['GET'])
class get_awards_coaches_coaches_groupedby_coachID_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, func.count().label('count_all'))\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
				.group_by(coaches.coachID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_coaches_coaches_orderedby_all_parser = reqparse.RequestParser()
get_awards_coaches_coaches_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_awards_coaches_namespace.route('/get_awards_coaches_coaches_orderedby_all', methods=['GET'])
class get_awards_coaches_coaches_orderedby_all_resource(Resource):
    
    @coaches_awards_coaches_namespace.expect(get_awards_coaches_coaches_orderedby_all_parser)
    def get(self):
        args = get_awards_coaches_coaches_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(func.count().label('count_all'))\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

