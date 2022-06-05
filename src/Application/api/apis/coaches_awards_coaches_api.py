from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import coaches , awards_coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
coaches_awards_coaches_namespace = Namespace("coaches_awards_coaches", description="coaches_awards_coaches Api") 
get_coaches_awards_coaches_filteredby_year_model = coaches_awards_coaches_namespace.model('get_coaches_awards_coaches_filteredby_year_model',{ 'coaches.coachID' : fields.String })
get_coaches_awards_coaches_filteredby_year_parser = reqparse.RequestParser()
get_coaches_awards_coaches_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@coaches_awards_coaches_namespace.route('/get_coaches_awards_coaches_filteredby_year', methods=['GET'])
class get_coaches_awards_coaches_filteredby_year_resource(Resource):
    @coaches_awards_coaches_namespace.marshal_list_with(get_coaches_awards_coaches_filteredby_year_model)
    @coaches_awards_coaches_namespace.expect(get_coaches_awards_coaches_filteredby_year_parser)

    def get(self):
        args = get_coaches_awards_coaches_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches.coachID)\
				.join(coaches, coaches.coachID == awards_coaches.coachID)\
				.filter(coaches.year == args['coaches.year']).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_coaches_coaches_model = coaches_awards_coaches_namespace.model('get_awards_coaches_coaches_model',{ 'coaches.coachID' : fields.String,'count_all' : fields.Integer })

@coaches_awards_coaches_namespace.route('/get_awards_coaches_coaches', methods=['GET'])
class get_awards_coaches_coaches_resource(Resource):
    @coaches_awards_coaches_namespace.marshal_list_with(get_awards_coaches_coaches_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(coaches.coachID, func.count().label('count_all'))\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
				.group_by(coaches.coachID).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_coaches_coaches_model = coaches_awards_coaches_namespace.model('get_awards_coaches_coaches_model',{ 'count_all' : fields.Integer })
get_awards_coaches_coaches_parser = reqparse.RequestParser()
get_awards_coaches_coaches_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_awards_coaches_namespace.route('/get_awards_coaches_coaches', methods=['GET'])
class get_awards_coaches_coaches_resource(Resource):
    @coaches_awards_coaches_namespace.marshal_list_with(get_awards_coaches_coaches_model)
    @coaches_awards_coaches_namespace.expect(get_awards_coaches_coaches_parser)

    def get(self):
        args = get_awards_coaches_coaches_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(func.count().label('count_all'))\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
				.order_by(direction(func.count())).all()

        except Exception as e:
            return None , 400

        return results , 200

