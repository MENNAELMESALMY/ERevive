from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players_teams 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
players_teams_namespace = Namespace("players_teams", description="players_teams Api") 


players_teams_model =players_teams_namespace.model("players_teams",convert_db_model_to_restx_model(players_teams)) 
players_teams_id_parser = reqparse.RequestParser() 
players_teams_id_parser.add_argument('id',type=int)


@players_teams_namespace.route("/")
class players_teamsApi(Resource):

    def get(self):
        try:
            players_teamss = db.session.query(players_teams).all()
            players_teamss = [row.serialize() for row in players_teamss]
            return players_teamss , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @players_teams_namespace.expect(players_teams_model) 
    def post(self):
        try:
            players_teamss = players_teams(id = request.json.get("id"),playerID = request.json.get("playerID"),year = request.json.get("year"),stint = request.json.get("stint"),tmID = request.json.get("tmID"),lgID = request.json.get("lgID"),GP = request.json.get("GP"),GS = request.json.get("GS"),minutes = request.json.get("minutes"),points = request.json.get("points"),oRebounds = request.json.get("oRebounds"),dRebounds = request.json.get("dRebounds"),rebounds = request.json.get("rebounds"),assists = request.json.get("assists"),steals = request.json.get("steals"),blocks = request.json.get("blocks"),turnovers = request.json.get("turnovers"),PF = request.json.get("PF"),fgAttempted = request.json.get("fgAttempted"),fgMade = request.json.get("fgMade"),ftAttempted = request.json.get("ftAttempted"),ftMade = request.json.get("ftMade"),threeAttempted = request.json.get("threeAttempted"),threeMade = request.json.get("threeMade"),PostGP = request.json.get("PostGP"),PostGS = request.json.get("PostGS"),PostMinutes = request.json.get("PostMinutes"),PostPoints = request.json.get("PostPoints"),PostoRebounds = request.json.get("PostoRebounds"),PostdRebounds = request.json.get("PostdRebounds"),PostRebounds = request.json.get("PostRebounds"),PostAssists = request.json.get("PostAssists"),PostSteals = request.json.get("PostSteals"),PostBlocks = request.json.get("PostBlocks"),PostTurnovers = request.json.get("PostTurnovers"),PostPF = request.json.get("PostPF"),PostfgAttempted = request.json.get("PostfgAttempted"),PostfgMade = request.json.get("PostfgMade"),PostftAttempted = request.json.get("PostftAttempted"),PostftMade = request.json.get("PostftMade"),PostthreeAttempted = request.json.get("PostthreeAttempted"),PostthreeMade = request.json.get("PostthreeMade"),note = request.json.get("note"))
            db.session.add(players_teamss)
            db.session.commit()    
            return players_teamss.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @players_teams_namespace.expect(players_teams_model) 
    def put(self):
        try:
            db.session.query(players_teams).filter(players_teams.id==request.json.get('id') ).update(request.json) 
            db.session.commit() 
            players_teamss = db.session.query(players_teams).filter(players_teams.id==request.json.get('id') ).first() 
            return players_teamss.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @players_teams_namespace.expect(players_teams_id_parser) 
    def delete(self):
        try:
            players_teamss = db.session.query(players_teams).filter(players_teams.id==players_teams_id_parser.parse_args().get('id') ).first() 
            db.session.query(players_teams).filter(players_teams.id==players_teams_id_parser.parse_args().get('id') ).delete() 
            db.session.commit() 
            return players_teamss.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_teams_filteredby_name_year_parser = reqparse.RequestParser()
get_players_teams_filteredby_name_year_parser.add_argument('teams.year', type=int, required=True, location='args')
get_players_teams_filteredby_name_year_parser.add_argument('teams.name', type=str, required=True, location='args')

@players_teams_namespace.route('/get_players_teams_filteredby_name_year', methods=['GET'])
class get_players_teams_filteredby_name_year_resource(Resource):
    
    @players_teams_namespace.expect(get_players_teams_filteredby_name_year_parser)
    def get(self):
        args = get_players_teams_filteredby_name_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.lastName, players.firstName, players.middleName)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.filter(teams.year == args['teams.year'], teams.name == args['teams.name']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_teams_filteredby_name_groupedby_name_playerID_year_parser = reqparse.RequestParser()
get_players_teams_filteredby_name_groupedby_name_playerID_year_parser.add_argument('teams.name', type=str, required=True, location='args')

@players_teams_namespace.route('/get_players_teams_filteredby_name_groupedby_name_playerID_year', methods=['GET'])
class get_players_teams_filteredby_name_groupedby_name_playerID_year_resource(Resource):
    
    @players_teams_namespace.expect(get_players_teams_filteredby_name_groupedby_name_playerID_year_parser)
    def get(self):
        args = get_players_teams_filteredby_name_groupedby_name_playerID_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(teams, teams.name, players, players.playerID, teams.year, func.count().label('count_all'))\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.filter(teams.name == args['teams.name'])\
				.group_by(players.playerID, teams.name, teams.year).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_teams_filteredby_year_groupedby_firstName_year_middleName_parser = reqparse.RequestParser()
get_players_teams_filteredby_year_groupedby_firstName_year_middleName_parser.add_argument('teams.year', type=int, required=True, location='args')
get_players_teams_filteredby_year_groupedby_firstName_year_middleName_parser.add_argument('teams.year', type=int, required=True, location='args')

@players_teams_namespace.route('/get_players_teams_filteredby_year_groupedby_firstName_year_middleName', methods=['GET'])
class get_players_teams_filteredby_year_groupedby_firstName_year_middleName_resource(Resource):
    
    @players_teams_namespace.expect(get_players_teams_filteredby_year_groupedby_firstName_year_middleName_parser)
    def get(self):
        args = get_players_teams_filteredby_year_groupedby_firstName_year_middleName_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.firstName, players.middleName, teams, teams.year, func.count(teams.year).label('count_teams.year'))\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.filter(teams.year == args['teams.year'])\
				.group_by(teams.year, players.middleName, players.firstName).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_teams_namespace.route('/get_players_teams_groupedby_playerID', methods=['GET'])
class get_players_teams_groupedby_playerID_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, players.firstName, players.middleName)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.group_by(players.playerID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_teams_namespace.route('/get_players_teams_groupedby_year', methods=['GET'])
class get_players_teams_groupedby_year_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(teams, teams.year, func.count(teams.year).label('count_teams.year'))\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.join(players, players.playerID == players_teams.playerID)\
				.group_by(teams.year).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_teams_namespace.route('/get_players_teams', methods=['GET'])
class get_players_teams_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(func.count().label('count_all')).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

