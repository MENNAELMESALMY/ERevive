from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_coaches , series_post 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
awards_coaches_series_post_namespace = Namespace("awards_coaches_series_post", description="awards_coaches_series_post Api") 
get_awards_coaches_series_post_groupedby_all_orderedby_all_parser = reqparse.RequestParser()
get_awards_coaches_series_post_groupedby_all_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@awards_coaches_series_post_namespace.route('/get_awards_coaches_series_post_groupedby_all_orderedby_all', methods=['GET'])
class get_awards_coaches_series_post_groupedby_all_orderedby_all_resource(Resource):
    
    @awards_coaches_series_post_namespace.expect(get_awards_coaches_series_post_groupedby_all_orderedby_all_parser)
    def get(self):
        args = get_awards_coaches_series_post_groupedby_all_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_coaches, series_post)\
				.group_by(series_post.lgIDWinner, series_post.L, awards_coaches.coachID, series_post.id, series_post.w, awards_coaches.id, series_post.round, awards_coaches.note, series_post.tmIDLoser, series_post.tmIDWinner, series_post.lgIDLoser, series_post.series, awards_coaches.lgID, awards_coaches.award, series_post.year)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@awards_coaches_series_post_namespace.route('/get_awards_coaches_series_post', methods=['GET'])
class get_awards_coaches_series_post_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(series_post, series_post.id, awards_coaches).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all_parser = reqparse.RequestParser()
get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@awards_coaches_series_post_namespace.route('/get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all', methods=['GET'])
class get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all_resource(Resource):
    
    @awards_coaches_series_post_namespace.expect(get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all_parser)
    def get(self):
        args = get_awards_coaches_series_post_groupedby_coachID_id_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(series_post, series_post.id, awards_coaches)\
				.group_by(series_post.id, awards_coaches.coachID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_coaches_series_post_groupedby_id_parser = reqparse.RequestParser()
get_awards_coaches_series_post_groupedby_id_parser.add_argument('having_value', type=int, required=True, location='args')

@awards_coaches_series_post_namespace.route('/get_awards_coaches_series_post_groupedby_id', methods=['GET'])
class get_awards_coaches_series_post_groupedby_id_resource(Resource):
    
    @awards_coaches_series_post_namespace.expect(get_awards_coaches_series_post_groupedby_id_parser)
    def get(self):
        args = get_awards_coaches_series_post_groupedby_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(func.count().label('count_all'), awards_coaches, series_post)\
				.group_by(awards_coaches.id)\
				.having(func.count() >= args['having_value']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_coaches_series_post_groupedby_id_orderedby_all_parser = reqparse.RequestParser()
get_awards_coaches_series_post_groupedby_id_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@awards_coaches_series_post_namespace.route('/get_awards_coaches_series_post_groupedby_id_orderedby_all', methods=['GET'])
class get_awards_coaches_series_post_groupedby_id_orderedby_all_resource(Resource):
    
    @awards_coaches_series_post_namespace.expect(get_awards_coaches_series_post_groupedby_id_orderedby_all_parser)
    def get(self):
        args = get_awards_coaches_series_post_groupedby_id_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_coaches, series_post)\
				.group_by(awards_coaches.id)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

