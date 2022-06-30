from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players_teams , teams 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
players_teams_teams_namespace = Namespace("players_teams_teams", description="players_teams_teams Api") 
get_players_teams_teams_filteredby_id_groupedby_all_parser = reqparse.RequestParser()
get_players_teams_teams_filteredby_id_groupedby_all_parser.add_argument('players_teams.id', type=int, required=True, location='args')

@players_teams_teams_namespace.route('/get_players_teams_teams_filteredby_id_groupedby_all', methods=['GET'])
class get_players_teams_teams_filteredby_id_groupedby_all_resource(Resource):
    
    @players_teams_teams_namespace.expect(get_players_teams_teams_filteredby_id_groupedby_all_parser)
    def get(self):
        args = get_players_teams_teams_filteredby_id_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(players_teams, teams, func.count().label('count_all'))\
				.join(teams, players_teams.tmID == teams.tmID)\
				.filter(players_teams.id == args['players_teams.id'])\
				.group_by(players_teams.threeMade, players_teams.tmID, players_teams.PostMinutes, players_teams.PostfgAttempted, players_teams.PostAssists, players_teams.fgMade, players_teams.fgAttempted, players_teams.ftAttempted, players_teams.id, players_teams.turnovers, players_teams.PostSteals, teams.franchID, teams.confID, teams.playoff, players_teams.points, players_teams.threeAttempted, teams.rank, players_teams.stint, players_teams.PostGP, teams.tmID, players_teams.PostoRebounds, players_teams.lgID, teams.divID, teams.confRank, players_teams.PostPF, players_teams.PostBlocks, players_teams.playerID, players_teams.GP, players_teams.note, players_teams.GS, players_teams.PostfgMade, players_teams.oRebounds, players_teams.year, players_teams.dRebounds, players_teams.PostftAttempted, players_teams.PostTurnovers, players_teams.PostRebounds, players_teams.rebounds, players_teams.PostftMade, players_teams.minutes, players_teams.PostGS, players_teams.PostthreeMade, players_teams.PF, players_teams.PostthreeAttempted, players_teams.PostdRebounds, players_teams.ftMade, teams.lgID, players_teams.assists, players_teams.blocks, teams.year, teams.name, players_teams.steals, players_teams.PostPoints).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_teams_teams_namespace.route('/get_players_teams_teams_groupedby_name_lgID', methods=['GET'])
class get_players_teams_teams_groupedby_name_lgID_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(teams, teams.lgID, teams.name, func.count(teams.lgID).label('count_teams.lgID'))\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.group_by(teams.lgID, teams.name).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_teams_teams_filteredby_name_parser = reqparse.RequestParser()
get_players_teams_teams_filteredby_name_parser.add_argument('teams.name', type=str, required=True, location='args')

@players_teams_teams_namespace.route('/get_players_teams_teams_filteredby_name', methods=['GET'])
class get_players_teams_teams_filteredby_name_resource(Resource):
    
    @players_teams_teams_namespace.expect(get_players_teams_teams_filteredby_name_parser)
    def get(self):
        args = get_players_teams_teams_filteredby_name_parser.parse_args()

        results = None
        try:
            results = db.session.query(players_teams, teams)\
				.join(teams, players_teams.tmID == teams.tmID)\
				.filter(teams.name.like(args['teams.name'])).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

