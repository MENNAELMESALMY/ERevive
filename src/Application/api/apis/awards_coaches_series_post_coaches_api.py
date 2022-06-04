from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_coaches , series_post , coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
awards_coaches_series_post_coaches_namespace = Namespace("awards_coaches_series_post_coaches", description="awards_coaches_series_post_coaches Api") 
get_awards_coaches_series_post_coaches_filteredby_id_model = awards_coaches_series_post_coaches_namespace.model('get_awards_coaches_series_post_coaches_filteredby_id_model',{ 'awards_coaches.id' : fields.String,'awards_coaches.coachID' : fields.DateTime,'awards_coaches.award' : fields.String,'awards_coaches.lgID' : fields.String,'awards_coaches.note' : fields.String,'series_post.id' : fields.String,'series_post.year' : fields.String,'series_post.round' : fields.String,'series_post.series' : fields.String,'series_post.tmIDWinner' : fields.String,'series_post.lgIDWinner' : fields.String,'series_post.tmIDLoser' : fields.String,'series_post.lgIDLoser' : fields.String,'series_post.w' : fields.String,'series_post.L' : fields.String,'coaches.coachID' : fields.String,'coaches.year' : fields.Integer,'coaches.tmID' : fields.String,'coaches.lgID' : fields.String,'coaches.stint' : fields.Integer,'coaches.won' : fields.Integer,'coaches.lost' : fields.Integer,'coaches.post_wins' : fields.Integer,'coaches.post_losses' : fields.Integer,'count_all' : fields.Integer })
get_awards_coaches_series_post_coaches_filteredby_id_parser = reqparse.RequestParser()
get_awards_coaches_series_post_coaches_filteredby_id_parser.add_argument('awards_coaches.id', type=str, required=True, location='args')

@awards_coaches_series_post_coaches_namespace.route('/get_awards_coaches_series_post_coaches_filteredby_id', methods=['GET'])
class get_awards_coaches_series_post_coaches_filteredby_id_resource(Resource):
    @awards_coaches_series_post_coaches_namespace.marshal_list_with(get_awards_coaches_series_post_coaches_filteredby_id_model)
    @awards_coaches_series_post_coaches_namespace.expect(get_awards_coaches_series_post_coaches_filteredby_id_parser)

    def get(self):
        args = get_awards_coaches_series_post_coaches_filteredby_id_parser.parse_args()

        results = db.session.query(awards_coaches, series_post, coaches, func.count().label('count_all'))\
			.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
			.filter(awards_coaches.id == args['awards_coaches.id'])
        return results

get_awards_coaches_series_post_coaches_model = awards_coaches_series_post_coaches_namespace.model('get_awards_coaches_series_post_coaches_model',{ 'series_post.id' : fields.String,'awards_coaches.id' : fields.String })

@awards_coaches_series_post_coaches_namespace.route('/get_awards_coaches_series_post_coaches', methods=['GET'])
class get_awards_coaches_series_post_coaches_resource(Resource):
    @awards_coaches_series_post_coaches_namespace.marshal_list_with(get_awards_coaches_series_post_coaches_model)
    
    def get(self):
        
        results = db.session.query(series_post.id, awards_coaches.id)\
			.join(awards_coaches, awards_coaches.coachID == coaches.coachID)
        return results

get_awards_coaches_series_post_groupedby_id_model = awards_coaches_series_post_coaches_namespace.model('get_awards_coaches_series_post_groupedby_id_model',{ 'awards_coaches.id' : fields.String,'awards_coaches.coachID' : fields.DateTime,'awards_coaches.award' : fields.String,'awards_coaches.lgID' : fields.String,'awards_coaches.note' : fields.String,'series_post.id' : fields.String,'series_post.year' : fields.String,'series_post.round' : fields.String,'series_post.series' : fields.String,'series_post.tmIDWinner' : fields.String,'series_post.lgIDWinner' : fields.String,'series_post.tmIDLoser' : fields.String,'series_post.lgIDLoser' : fields.String,'series_post.w' : fields.String,'series_post.L' : fields.Strin })
get_awards_coaches_series_post_groupedby_id_parser = reqparse.RequestParser()
get_awards_coaches_series_post_groupedby_id_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@awards_coaches_series_post_coaches_namespace.route('/get_awards_coaches_series_post_groupedby_id', methods=['GET'])
class get_awards_coaches_series_post_groupedby_id_resource(Resource):
    @awards_coaches_series_post_coaches_namespace.marshal_list_with(get_awards_coaches_series_post_groupedby_id_model)
    @awards_coaches_series_post_coaches_namespace.expect(get_awards_coaches_series_post_groupedby_id_parser)

    def get(self):
        args = get_awards_coaches_series_post_groupedby_id_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(awards_coaches, series_post)\
			.join(awards_coaches)\
			.join(series_post)\
			.group_by(awards_coaches.id)\
			.order_by(direction(func.count()))
        return results

