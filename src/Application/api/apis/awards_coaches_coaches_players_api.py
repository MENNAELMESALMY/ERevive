from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_coaches , coaches , players 
from app import db 
from utils import convert_db_model_to_restx_model 
            
awards_coaches_coaches_players_namespace = Namespace("awards_coaches_coaches_players", description="awards_coaches_coaches_players Api") 
get_awards_coaches_coaches_players_model = awards_coaches_coaches_players_namespace.model('get_awards_coaches_coaches_players_model',{ 'players.firstName' : fields.String,'players.playerID' : fields.String,'coaches.year' : fields.Integer,'coaches.coachID' : fields.String })

@awards_coaches_coaches_players_namespace.route('/get_awards_coaches_coaches_players', methods=['GET'])
class get_awards_coaches_coaches_players_resource(Resource):
    @awards_coaches_coaches_players_namespace.marshal_list_with(get_awards_coaches_coaches_players_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players.firstName, players.playerID, coaches.year, coaches.coachID)\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_coaches_coaches_players_filteredby_year_model = awards_coaches_coaches_players_namespace.model('get_awards_coaches_coaches_players_filteredby_year_model',{ 'players.playerID' : fields.String,'coaches.coachID' : fields.String })
get_awards_coaches_coaches_players_filteredby_year_parser = reqparse.RequestParser()
get_awards_coaches_coaches_players_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@awards_coaches_coaches_players_namespace.route('/get_awards_coaches_coaches_players_filteredby_year', methods=['GET'])
class get_awards_coaches_coaches_players_filteredby_year_resource(Resource):
    @awards_coaches_coaches_players_namespace.marshal_list_with(get_awards_coaches_coaches_players_filteredby_year_model)
    @awards_coaches_coaches_players_namespace.expect(get_awards_coaches_coaches_players_filteredby_year_parser)

    def get(self):
        args = get_awards_coaches_coaches_players_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.playerID, coaches.coachID)\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
				.filter(coaches.year < args['coaches.year']).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_coaches_coaches_players_filteredby_coachID_model = awards_coaches_coaches_players_namespace.model('get_awards_coaches_coaches_players_filteredby_coachID_model',{ 'players.playerID' : fields.String,'coaches.coachID' : fields.String })
get_awards_coaches_coaches_players_filteredby_coachID_parser = reqparse.RequestParser()
get_awards_coaches_coaches_players_filteredby_coachID_parser.add_argument('coaches.coachID', type=str, required=True, location='args')

@awards_coaches_coaches_players_namespace.route('/get_awards_coaches_coaches_players_filteredby_coachID', methods=['GET'])
class get_awards_coaches_coaches_players_filteredby_coachID_resource(Resource):
    @awards_coaches_coaches_players_namespace.marshal_list_with(get_awards_coaches_coaches_players_filteredby_coachID_model)
    @awards_coaches_coaches_players_namespace.expect(get_awards_coaches_coaches_players_filteredby_coachID_parser)

    def get(self):
        args = get_awards_coaches_coaches_players_filteredby_coachID_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.playerID, coaches.coachID)\
				.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
				.filter(coaches.coachID == args['coaches.coachID']).all()

        except Exception as e:
            return None , 400

        return results , 200

