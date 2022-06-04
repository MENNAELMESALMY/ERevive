from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_coaches_namespace = Namespace("players_coaches", description="players_coaches Api") 
get_players_coaches_groupedby_playerID_model = players_coaches_namespace.model('get_players_coaches_groupedby_playerID_model',{ 'coaches.coachID' : fields.String })
get_players_coaches_groupedby_playerID_parser = reqparse.RequestParser()
get_players_coaches_groupedby_playerID_parser.add_argument('having_value', type=int, required=True, location='args')

@players_coaches_namespace.route('/get_players_coaches_groupedby_playerID', methods=['GET'])
class get_players_coaches_groupedby_playerID_resource(Resource):
    @players_coaches_namespace.marshal_list_with(get_players_coaches_groupedby_playerID_model)
    @players_coaches_namespace.expect(get_players_coaches_groupedby_playerID_parser)

    def get(self):
        args = get_players_coaches_groupedby_playerID_parser.parse_args()

        results = db.session.query(coaches.coachID)\
			.join(players)\
			.join(coaches)\
			.group_by(players.playerID)\
			.having(func.count() > args['having_value'])
        return results

get_players_coaches_groupedby_playerID_model = players_coaches_namespace.model('get_players_coaches_groupedby_playerID_model',{ 'coaches.coachID' : fields.String })
get_players_coaches_groupedby_playerID_parser = reqparse.RequestParser()
get_players_coaches_groupedby_playerID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_coaches_namespace.route('/get_players_coaches_groupedby_playerID', methods=['GET'])
class get_players_coaches_groupedby_playerID_resource(Resource):
    @players_coaches_namespace.marshal_list_with(get_players_coaches_groupedby_playerID_model)
    @players_coaches_namespace.expect(get_players_coaches_groupedby_playerID_parser)

    def get(self):
        args = get_players_coaches_groupedby_playerID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(coaches.coachID)\
			.join(players)\
			.join(coaches)\
			.group_by(players.playerID)\
			.order_by(direction(func.count()))
        return results

get_players_coaches_model = players_coaches_namespace.model('get_players_coaches_model',{ 'coaches.post_wins' : fields.Integer })

@players_coaches_namespace.route('/get_players_coaches', methods=['GET'])
class get_players_coaches_resource(Resource):
    @players_coaches_namespace.marshal_list_with(get_players_coaches_model)
    
    def get(self):
        
        results = db.session.query(coaches.post_wins)\
			.join(players)\
			.join(coaches)
        return results

