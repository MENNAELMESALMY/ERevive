from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_coaches , coaches , players 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
awards_coaches_coaches_players_namespace = Namespace("awards_coaches_coaches_players", description="awards_coaches_coaches_players Api") 

@awards_coaches_coaches_players_namespace.route('/get_awards_coaches_coaches_players', methods=['GET'])
class get_awards_coaches_coaches_players_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, players, players.playerID, players.firstName, coaches.year)\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_coaches_coaches_players_filteredby_year_parser = reqparse.RequestParser()
get_awards_coaches_coaches_players_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@awards_coaches_coaches_players_namespace.route('/get_awards_coaches_coaches_players_filteredby_year', methods=['GET'])
class get_awards_coaches_coaches_players_filteredby_year_resource(Resource):
    
    @awards_coaches_coaches_players_namespace.expect(get_awards_coaches_coaches_players_filteredby_year_parser)
    def get(self):
        args = get_awards_coaches_coaches_players_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, players, players.playerID)\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
				.filter(coaches.year < args['coaches.year']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_coaches_coaches_players_filteredby_playerID_parser = reqparse.RequestParser()
get_awards_coaches_coaches_players_filteredby_playerID_parser.add_argument('players.playerID', type=str, required=True, location='args')

@awards_coaches_coaches_players_namespace.route('/get_awards_coaches_coaches_players_filteredby_playerID', methods=['GET'])
class get_awards_coaches_coaches_players_filteredby_playerID_resource(Resource):
    
    @awards_coaches_coaches_players_namespace.expect(get_awards_coaches_coaches_players_filteredby_playerID_parser)
    def get(self):
        args = get_awards_coaches_coaches_players_filteredby_playerID_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, players, players.playerID)\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
				.filter(players.playerID == args['players.playerID']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

