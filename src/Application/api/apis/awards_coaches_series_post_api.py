from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_coaches , series_post 
from app import db 
from utils import convert_db_model_to_restx_model 
            
awards_coaches_series_post_namespace = Namespace("awards_coaches_series_post", description="awards_coaches_series_post Api") 
get_awards_coaches_series_post_groupedby_id_model = awards_coaches_series_post_namespace.model('get_awards_coaches_series_post_groupedby_id_model',{ 'awards_coaches.id' : fields.String,'awards_coaches.coachID' : fields.String,'awards_coaches.award' : fields.String,'awards_coaches.lgID' : fields.String,'awards_coaches.note' : fields.String,'series_post.id' : fields.String,'series_post.year' : fields.Integer,'series_post.round' : fields.String,'series_post.series' : fields.String,'series_post.tmIDWinner' : fields.String,'series_post.lgIDWinner' : fields.String,'series_post.tmIDLoser' : fields.String,'series_post.lgIDLoser' : fields.String,'series_post.w' : fields.String,'series_post.L' : fields.String })
get_awards_coaches_series_post_groupedby_id_parser = reqparse.RequestParser()
get_awards_coaches_series_post_groupedby_id_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@awards_coaches_series_post_namespace.route('/get_awards_coaches_series_post_groupedby_id', methods=['GET'])
class get_awards_coaches_series_post_groupedby_id_resource(Resource):
    @awards_coaches_series_post_namespace.marshal_list_with(get_awards_coaches_series_post_groupedby_id_model)
    @awards_coaches_series_post_namespace.expect(get_awards_coaches_series_post_groupedby_id_parser)

    def get(self):
        args = get_awards_coaches_series_post_groupedby_id_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_coaches, series_post)\
				.group_by(series_post.series, awards_coaches.award, series_post.year, series_post.id, awards_coaches.lgID, series_post.tmIDWinner, series_post.tmIDLoser, awards_coaches.id, series_post.lgIDWinner, awards_coaches.coachID, series_post.lgIDLoser, series_post.w, series_post.round, awards_coaches.note, series_post.L)\
				.order_by(direction(func.count())).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_awards_coaches_series_post_model = awards_coaches_series_post_namespace.model('get_awards_coaches_series_post_model',{ 'series_post.id' : fields.String })

@awards_coaches_series_post_namespace.route('/get_awards_coaches_series_post', methods=['GET'])
class get_awards_coaches_series_post_resource(Resource):
    @awards_coaches_series_post_namespace.marshal_list_with(get_awards_coaches_series_post_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(series_post, series_post.id, awards_coaches).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_awards_coaches_series_post_groupedby_id_model = awards_coaches_series_post_namespace.model('get_awards_coaches_series_post_groupedby_id_model',{ 'count_all' : fields.Integer })

@awards_coaches_series_post_namespace.route('/get_awards_coaches_series_post_groupedby_id', methods=['GET'])
class get_awards_coaches_series_post_groupedby_id_resource(Resource):
    @awards_coaches_series_post_namespace.marshal_list_with(get_awards_coaches_series_post_groupedby_id_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(func.count().label('count_all'), awards_coaches, series_post)\
				.group_by(awards_coaches.id).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

