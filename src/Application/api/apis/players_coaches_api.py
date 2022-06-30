from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , coaches 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
players_coaches_namespace = Namespace("players_coaches", description="players_coaches Api") 
get_players_coaches_groupedby_playerID_parser = reqparse.RequestParser()
get_players_coaches_groupedby_playerID_parser.add_argument('having_value', type=int, required=True, location='args')

@players_coaches_namespace.route('/get_players_coaches_groupedby_playerID', methods=['GET'])
class get_players_coaches_groupedby_playerID_resource(Resource):
    
    @players_coaches_namespace.expect(get_players_coaches_groupedby_playerID_parser)
    def get(self):
        args = get_players_coaches_groupedby_playerID_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, players)\
				.group_by(players.playerID)\
				.having(func.count() > args['having_value']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_coaches_groupedby_coachID_playerID_orderedby_all_parser = reqparse.RequestParser()
get_players_coaches_groupedby_coachID_playerID_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_coaches_namespace.route('/get_players_coaches_groupedby_coachID_playerID_orderedby_all', methods=['GET'])
class get_players_coaches_groupedby_coachID_playerID_orderedby_all_resource(Resource):
    
    @players_coaches_namespace.expect(get_players_coaches_groupedby_coachID_playerID_orderedby_all_parser)
    def get(self):
        args = get_players_coaches_groupedby_coachID_playerID_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, players)\
				.group_by(players.playerID, coaches.coachID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_coaches_namespace.route('/get_players_coaches', methods=['GET'])
class get_players_coaches_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(coaches, coaches.post_wins, players).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_coaches_groupedby_playerID_orderedby_all_parser = reqparse.RequestParser()
get_players_coaches_groupedby_playerID_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_coaches_namespace.route('/get_players_coaches_groupedby_playerID_orderedby_all', methods=['GET'])
class get_players_coaches_groupedby_playerID_orderedby_all_resource(Resource):
    
    @players_coaches_namespace.expect(get_players_coaches_groupedby_playerID_orderedby_all_parser)
    def get(self):
        args = get_players_coaches_groupedby_playerID_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(players, coaches)\
				.group_by(players.playerID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

