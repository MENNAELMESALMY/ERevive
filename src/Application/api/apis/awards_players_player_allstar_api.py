from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_players , player_allstar 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
awards_players_player_allstar_namespace = Namespace("awards_players_player_allstar", description="awards_players_player_allstar Api") 

@awards_players_player_allstar_namespace.route('/get_awards_players_player_allstar_groupedby_minutes', methods=['GET'])
class get_awards_players_player_allstar_groupedby_minutes_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(player_allstar, player_allstar.minutes, func.avg(player_allstar.minutes).label('avg_player_allstar.minutes'), func.sum(player_allstar.minutes).label('sum_player_allstar.minutes'), func.count().label('count_all'))\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.join(players, players.playerID == player_allstar.playerID)\
				.group_by(player_allstar.minutes).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_players_player_allstar_orderedby_minutes_parser = reqparse.RequestParser()
get_awards_players_player_allstar_orderedby_minutes_parser.add_argument('is_order_of_sum_minutes_desc', type=bool, required=True, location='args')

@awards_players_player_allstar_namespace.route('/get_awards_players_player_allstar_orderedby_minutes', methods=['GET'])
class get_awards_players_player_allstar_orderedby_minutes_resource(Resource):
    
    @awards_players_player_allstar_namespace.expect(get_awards_players_player_allstar_orderedby_minutes_parser)
    def get(self):
        args = get_awards_players_player_allstar_orderedby_minutes_parser.parse_args()
        minutes_direction = desc if args['is_order_of_sum_minutes_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_players, player_allstar)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.join(players, players.playerID == player_allstar.playerID)\
				.order_by(minutes_direction(func.sum(player_allstar.minutes))).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

