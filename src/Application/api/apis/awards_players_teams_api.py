from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_players , teams 
from app import db 
from utils import convert_db_model_to_restx_model 
            
awards_players_teams_namespace = Namespace("awards_players_teams", description="awards_players_teams Api") 
get_awards_players_teams_filteredby_name_year_model = awards_players_teams_namespace.model('get_awards_players_teams_filteredby_name_year_model',{ 'sum_awards_players.playerID' : fields.String })
get_awards_players_teams_filteredby_name_year_parser = reqparse.RequestParser()
get_awards_players_teams_filteredby_name_year_parser.add_argument('teams.name', type=str, required=True, location='args')
get_awards_players_teams_filteredby_name_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')

@awards_players_teams_namespace.route('/get_awards_players_teams_filteredby_name_year', methods=['GET'])
class get_awards_players_teams_filteredby_name_year_resource(Resource):
    @awards_players_teams_namespace.marshal_list_with(get_awards_players_teams_filteredby_name_year_model)
    @awards_players_teams_namespace.expect(get_awards_players_teams_filteredby_name_year_parser)

    def get(self):
        args = get_awards_players_teams_filteredby_name_year_parser.parse_args()

        results = db.session.query(func.sum(awards_players.playerID).label('sum_awards_players.playerID'))\
			.join(players_teams, players_teams.tmID == teams.tmID)\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.join(players, players.playerID == players_teams.playerID)\
			.filter(teams.name == args['teams.name'], awards_players.year between args['awards_players.year'])
        return results

get_awards_players_teams_filteredby_name_model = awards_players_teams_namespace.model('get_awards_players_teams_filteredby_name_model',{ 'teams.name' : fields.String,'sum_awards_players.playerID' : fields.String })
get_awards_players_teams_filteredby_name_parser = reqparse.RequestParser()
get_awards_players_teams_filteredby_name_parser.add_argument('teams.name', type=str, required=True, location='args')

@awards_players_teams_namespace.route('/get_awards_players_teams_filteredby_name', methods=['GET'])
class get_awards_players_teams_filteredby_name_resource(Resource):
    @awards_players_teams_namespace.marshal_list_with(get_awards_players_teams_filteredby_name_model)
    @awards_players_teams_namespace.expect(get_awards_players_teams_filteredby_name_parser)

    def get(self):
        args = get_awards_players_teams_filteredby_name_parser.parse_args()

        results = db.session.query(teams.name, func.sum(awards_players.playerID).label('sum_awards_players.playerID'))\
			.join(players_teams, players_teams.tmID == teams.tmID)\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.join(players, players.playerID == players_teams.playerID)\
			.filter(teams.name == args['teams.name'])\
			.group_by(teams.name)
        return results

get_awards_players_teams_groupedby_playerID_model = awards_players_teams_namespace.model('get_awards_players_teams_groupedby_playerID_model',{ 'teams.name' : fields.String,'teams.lgID' : fields.String,'teams.rank' : fields.Integer })

@awards_players_teams_namespace.route('/get_awards_players_teams_groupedby_playerID', methods=['GET'])
class get_awards_players_teams_groupedby_playerID_resource(Resource):
    @awards_players_teams_namespace.marshal_list_with(get_awards_players_teams_groupedby_playerID_model)
    
    def get(self):
        
        results = db.session.query(teams.name, teams.lgID, teams.rank)\
			.join(players_teams, players_teams.tmID == teams.tmID)\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.join(players, players.playerID == players_teams.playerID)\
			.group_by(awards_players.playerID)
        return results

get_awards_players_teams_filteredby_year_model = awards_players_teams_namespace.model('get_awards_players_teams_filteredby_year_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'teams.year' : fields.Integer,'teams.lgID' : fields.String,'teams.tmID' : fields.String,'teams.franchID' : fields.String,'teams.confID' : fields.String,'teams.divID' : fields.String,'teams.rank' : fields.Integer,'teams.confRank' : fields.Integer,'teams.playoff' : fields.String,'teams.name' : fields.Strin })
get_awards_players_teams_filteredby_year_parser = reqparse.RequestParser()
get_awards_players_teams_filteredby_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')

@awards_players_teams_namespace.route('/get_awards_players_teams_filteredby_year', methods=['GET'])
class get_awards_players_teams_filteredby_year_resource(Resource):
    @awards_players_teams_namespace.marshal_list_with(get_awards_players_teams_filteredby_year_model)
    @awards_players_teams_namespace.expect(get_awards_players_teams_filteredby_year_parser)

    def get(self):
        args = get_awards_players_teams_filteredby_year_parser.parse_args()

        results = db.session.query(awards_players, teams)\
			.join(players_teams, players_teams.tmID == teams.tmID)\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.join(players, players.playerID == players_teams.playerID)\
			.filter(awards_players.year == args['awards_players.year'])
        return results

get_awards_players_teams_model = awards_players_teams_namespace.model('get_awards_players_teams_model',{ 'teams.name' : fields.String })

@awards_players_teams_namespace.route('/get_awards_players_teams', methods=['GET'])
class get_awards_players_teams_resource(Resource):
    @awards_players_teams_namespace.marshal_list_with(get_awards_players_teams_model)
    
    def get(self):
        
        results = db.session.query(teams.name)\
			.join(players_teams, players_teams.tmID == teams.tmID)\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.join(players, players.playerID == players_teams.playerID)
        return results

