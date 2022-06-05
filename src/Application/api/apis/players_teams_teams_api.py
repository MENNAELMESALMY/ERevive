from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players_teams , teams 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_teams_teams_namespace = Namespace("players_teams_teams", description="players_teams_teams Api") 
get_players_teams_teams_filteredby_id_model = players_teams_teams_namespace.model('get_players_teams_teams_filteredby_id_model',{ 'players_teams.id' : fields.Integer,'players_teams.playerID' : fields.String,'players_teams.year' : fields.Integer,'players_teams.stint' : fields.Integer,'players_teams.tmID' : fields.String,'players_teams.lgID' : fields.String,'players_teams.GP' : fields.Integer,'players_teams.GS' : fields.Integer,'players_teams.minutes' : fields.Integer,'players_teams.points' : fields.Integer,'players_teams.oRebounds' : fields.Integer,'players_teams.dRebounds' : fields.Integer,'players_teams.rebounds' : fields.Integer,'players_teams.assists' : fields.Integer,'players_teams.steals' : fields.Integer,'players_teams.blocks' : fields.Integer,'players_teams.turnovers' : fields.Integer,'players_teams.PF' : fields.Integer,'players_teams.fgAttempted' : fields.Integer,'players_teams.fgMade' : fields.Integer,'players_teams.ftAttempted' : fields.Integer,'players_teams.ftMade' : fields.Integer,'players_teams.threeAttempted' : fields.Integer,'players_teams.threeMade' : fields.Integer,'players_teams.PostGP' : fields.Integer,'players_teams.PostGS' : fields.Integer,'players_teams.PostMinutes' : fields.Integer,'players_teams.PostPoints' : fields.Integer,'players_teams.PostoRebounds' : fields.Integer,'players_teams.PostdRebounds' : fields.Integer,'players_teams.PostRebounds' : fields.Integer,'players_teams.PostAssists' : fields.Integer,'players_teams.PostSteals' : fields.Integer,'players_teams.PostBlocks' : fields.Integer,'players_teams.PostTurnovers' : fields.Integer,'players_teams.PostPF' : fields.Integer,'players_teams.PostfgAttempted' : fields.Integer,'players_teams.PostfgMade' : fields.Integer,'players_teams.PostftAttempted' : fields.Integer,'players_teams.PostftMade' : fields.Integer,'players_teams.PostthreeAttempted' : fields.Integer,'players_teams.PostthreeMade' : fields.Integer,'players_teams.note' : fields.String,'teams.year' : fields.Integer,'teams.lgID' : fields.String,'teams.tmID' : fields.String,'teams.franchID' : fields.String,'teams.confID' : fields.String,'teams.divID' : fields.String,'teams.rank' : fields.Integer,'teams.confRank' : fields.Integer,'teams.playoff' : fields.String,'teams.name' : fields.String })
get_players_teams_teams_filteredby_id_parser = reqparse.RequestParser()
get_players_teams_teams_filteredby_id_parser.add_argument('players_teams.id', type=int, required=True, location='args')

@players_teams_teams_namespace.route('/get_players_teams_teams_filteredby_id', methods=['GET'])
class get_players_teams_teams_filteredby_id_resource(Resource):
    @players_teams_teams_namespace.marshal_list_with(get_players_teams_teams_filteredby_id_model)
    @players_teams_teams_namespace.expect(get_players_teams_teams_filteredby_id_parser)

    def get(self):
        args = get_players_teams_teams_filteredby_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(players_teams, teams)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.filter(players_teams.id == args['players_teams.id']).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_teams_filteredby_name_model = players_teams_teams_namespace.model('get_players_teams_filteredby_name_model',{ 'players.playerID' : fields.String,'teams.year' : fields.Integer,'teams.name' : fields.String,'count_all' : fields.Integer })
get_players_teams_filteredby_name_parser = reqparse.RequestParser()
get_players_teams_filteredby_name_parser.add_argument('teams.name', type=str, required=True, location='args')

@players_teams_teams_namespace.route('/get_players_teams_filteredby_name', methods=['GET'])
class get_players_teams_filteredby_name_resource(Resource):
    @players_teams_teams_namespace.marshal_list_with(get_players_teams_filteredby_name_model)
    @players_teams_teams_namespace.expect(get_players_teams_filteredby_name_parser)

    def get(self):
        args = get_players_teams_filteredby_name_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.playerID, teams.year, teams.name, func.count().label('count_all'))\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.filter(teams.name == args['teams.name'])\
				.group_by(teams.name, teams.year, players.playerID).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_teams_teams_model = players_teams_teams_namespace.model('get_players_teams_teams_model',{ 'teams.name' : fields.String,'teams.lgID' : fields.String,'count_teams.lgID' : fields.String })

@players_teams_teams_namespace.route('/get_players_teams_teams', methods=['GET'])
class get_players_teams_teams_resource(Resource):
    @players_teams_teams_namespace.marshal_list_with(get_players_teams_teams_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(teams.name, teams.lgID, func.count(teams.lgID).label('count_teams.lgID'))\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.group_by(teams.lgID, teams.name).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_teams_filteredby_year_name_model = players_teams_teams_namespace.model('get_players_teams_filteredby_year_name_model',{ 'players.lastName' : fields.String,'players.middleName' : fields.String,'players.firstName' : fields.String })
get_players_teams_filteredby_year_name_parser = reqparse.RequestParser()
get_players_teams_filteredby_year_name_parser.add_argument('teams.name', type=str, required=True, location='args')
get_players_teams_filteredby_year_name_parser.add_argument('teams.year', type=int, required=True, location='args')

@players_teams_teams_namespace.route('/get_players_teams_filteredby_year_name', methods=['GET'])
class get_players_teams_filteredby_year_name_resource(Resource):
    @players_teams_teams_namespace.marshal_list_with(get_players_teams_filteredby_year_name_model)
    @players_teams_teams_namespace.expect(get_players_teams_filteredby_year_name_parser)

    def get(self):
        args = get_players_teams_filteredby_year_name_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.lastName, players.middleName, players.firstName)\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.filter(teams.name == args['teams.name'], teams.year == args['teams.year']).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_teams_teams_filteredby_tmID_model = players_teams_teams_namespace.model('get_players_teams_teams_filteredby_tmID_model',{ 'players.firstName' : fields.String,'players.middleName' : fields.String,'teams.lgID' : fields.String,'count_all' : fields.Integer })
get_players_teams_teams_filteredby_tmID_parser = reqparse.RequestParser()
get_players_teams_teams_filteredby_tmID_parser.add_argument('teams.tmID', type=str, required=True, location='args')

@players_teams_teams_namespace.route('/get_players_teams_teams_filteredby_tmID', methods=['GET'])
class get_players_teams_teams_filteredby_tmID_resource(Resource):
    @players_teams_teams_namespace.marshal_list_with(get_players_teams_teams_filteredby_tmID_model)
    @players_teams_teams_namespace.expect(get_players_teams_teams_filteredby_tmID_parser)

    def get(self):
        args = get_players_teams_teams_filteredby_tmID_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.firstName, players.middleName, teams.lgID, func.count().label('count_all'))\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.filter(teams.tmID == args['teams.tmID'])\
				.group_by(players.middleName, players.firstName, teams.lgID).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_teams_filteredby_year_model = players_teams_teams_namespace.model('get_players_teams_filteredby_year_model',{ 'players.firstName' : fields.String,'players.middleName' : fields.String,'teams.year' : fields.Integer,'count_teams.year' : fields.Integer })
get_players_teams_filteredby_year_parser = reqparse.RequestParser()
get_players_teams_filteredby_year_parser.add_argument('teams.year', type=int, required=True, location='args')
get_players_teams_filteredby_year_parser.add_argument('teams.year', type=int, required=True, location='args')

@players_teams_teams_namespace.route('/get_players_teams_filteredby_year', methods=['GET'])
class get_players_teams_filteredby_year_resource(Resource):
    @players_teams_teams_namespace.marshal_list_with(get_players_teams_filteredby_year_model)
    @players_teams_teams_namespace.expect(get_players_teams_filteredby_year_parser)

    def get(self):
        args = get_players_teams_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.firstName, players.middleName, teams.year, func.count(teams.year).label('count_teams.year'))\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.filter(teams.year == args['teams.year'])\
				.group_by(players.middleName, players.firstName, teams.year).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_teams_groupedby_year_model = players_teams_teams_namespace.model('get_players_teams_groupedby_year_model',{ 'teams.year' : fields.Integer,'count_teams.year' : fields.Integer })

@players_teams_teams_namespace.route('/get_players_teams_groupedby_year', methods=['GET'])
class get_players_teams_groupedby_year_resource(Resource):
    @players_teams_teams_namespace.marshal_list_with(get_players_teams_groupedby_year_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(teams.year, func.count(teams.year).label('count_teams.year'))\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.group_by(teams.year).all()

        except Exception as e:
            return None , 400

        return results , 200

