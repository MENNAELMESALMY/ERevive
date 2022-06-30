from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_players , teams 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
awards_players_teams_namespace = Namespace("awards_players_teams", description="awards_players_teams Api") 
get_awards_players_teams_filteredby_name_groupedby_name_parser = reqparse.RequestParser()
get_awards_players_teams_filteredby_name_groupedby_name_parser.add_argument('teams.name', type=str, required=True, location='args')

@awards_players_teams_namespace.route('/get_awards_players_teams_filteredby_name_groupedby_name', methods=['GET'])
class get_awards_players_teams_filteredby_name_groupedby_name_resource(Resource):
    
    @awards_players_teams_namespace.expect(get_awards_players_teams_filteredby_name_groupedby_name_parser)
    def get(self):
        args = get_awards_players_teams_filteredby_name_groupedby_name_parser.parse_args()

        results = None
        try:
            results = db.session.query(teams, teams.name, func.sum(awards_players.playerID).label('sum_awards_players.playerID'))\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.filter(teams.name == args['teams.name'])\
				.group_by(teams.name).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@awards_players_teams_namespace.route('/get_awards_players_teams_groupedby_playerID', methods=['GET'])
class get_awards_players_teams_groupedby_playerID_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(teams, teams.lgID, teams.name, teams.rank)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.group_by(awards_players.playerID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@awards_players_teams_namespace.route('/get_awards_players_teams', methods=['GET'])
class get_awards_players_teams_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(teams, teams.name)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.join(awards_players, awards_players.playerID == players.playerID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_players_teams_filteredby_name_year_parser = reqparse.RequestParser()
get_awards_players_teams_filteredby_name_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')
get_awards_players_teams_filteredby_name_year_parser.add_argument('teams.name', type=str, required=True, location='args')

@awards_players_teams_namespace.route('/get_awards_players_teams_filteredby_name_year', methods=['GET'])
class get_awards_players_teams_filteredby_name_year_resource(Resource):
    
    @awards_players_teams_namespace.expect(get_awards_players_teams_filteredby_name_year_parser)
    def get(self):
        args = get_awards_players_teams_filteredby_name_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(func.sum(awards_players.playerID).label('sum_awards_players.playerID'))\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.filter(awards_players.year == args['awards_players.year'], teams.name == args['teams.name']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_players_teams_filteredby_year_parser = reqparse.RequestParser()
get_awards_players_teams_filteredby_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')

@awards_players_teams_namespace.route('/get_awards_players_teams_filteredby_year', methods=['GET'])
class get_awards_players_teams_filteredby_year_resource(Resource):
    
    @awards_players_teams_namespace.expect(get_awards_players_teams_filteredby_year_parser)
    def get(self):
        args = get_awards_players_teams_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(awards_players, teams)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.filter(awards_players.year == args['awards_players.year']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

