from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players_teams 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_teams_namespace = Namespace("players_teams", description="players_teams Api") 


players_teams_model =players_teams_namespace.model("players_teams",convert_db_model_to_restx_model(players_teams)) 
players_teams_id_parser = reqparse.RequestParser() 
players_teams_id_parser.add_argument('id',type=int)


@players_teams_namespace.route("/")
class players_teamsApi(Resource):

    @players_teams_namespace.marshal_list_with(players_teams_model) 
    def get(self):
        try:
            players_teamss = db.session.query(players_teams).all()
        except Exception as e:
            print(e)
            return None , 500
        return players_teamss , 200  

    @players_teams_namespace.marshal_with(players_teams_model) 
    @players_teams_namespace.expect(players_teams_model) 
    def post(self):
        try:
            players_teamss = players_teams(id = request.json.get("id"),playerID = request.json.get("playerID"),year = request.json.get("year"),stint = request.json.get("stint"),tmID = request.json.get("tmID"),lgID = request.json.get("lgID"),GP = request.json.get("GP"),GS = request.json.get("GS"),minutes = request.json.get("minutes"),points = request.json.get("points"),oRebounds = request.json.get("oRebounds"),dRebounds = request.json.get("dRebounds"),rebounds = request.json.get("rebounds"),assists = request.json.get("assists"),steals = request.json.get("steals"),blocks = request.json.get("blocks"),turnovers = request.json.get("turnovers"),PF = request.json.get("PF"),fgAttempted = request.json.get("fgAttempted"),fgMade = request.json.get("fgMade"),ftAttempted = request.json.get("ftAttempted"),ftMade = request.json.get("ftMade"),threeAttempted = request.json.get("threeAttempted"),threeMade = request.json.get("threeMade"),PostGP = request.json.get("PostGP"),PostGS = request.json.get("PostGS"),PostMinutes = request.json.get("PostMinutes"),PostPoints = request.json.get("PostPoints"),PostoRebounds = request.json.get("PostoRebounds"),PostdRebounds = request.json.get("PostdRebounds"),PostRebounds = request.json.get("PostRebounds"),PostAssists = request.json.get("PostAssists"),PostSteals = request.json.get("PostSteals"),PostBlocks = request.json.get("PostBlocks"),PostTurnovers = request.json.get("PostTurnovers"),PostPF = request.json.get("PostPF"),PostfgAttempted = request.json.get("PostfgAttempted"),PostfgMade = request.json.get("PostfgMade"),PostftAttempted = request.json.get("PostftAttempted"),PostftMade = request.json.get("PostftMade"),PostthreeAttempted = request.json.get("PostthreeAttempted"),PostthreeMade = request.json.get("PostthreeMade"),note = request.json.get("note"))
            db.session.add(players_teamss)
            db.session.commit()    
        except Exception as e:
            print(e)
            return None , 500
        return players_teamss , 201 

    @players_teams_namespace.marshal_with(players_teams_model) 
    @players_teams_namespace.expect(players_teams_model) 
    def put(self):
        try:
            db.session.query(players_teams).filter(players_teams.id==request.json.get('id') ).update(request.json) 
            db.session.commit() 
            players_teamss = db.session.query(players_teams).filter(players_teams.id==request.json.get('id') ).first() 
        except Exception as e:
            print(e)
            return None , 500
        return players_teamss , 200    

    @players_teams_namespace.marshal_with(players_teams_model) 
    @players_teams_namespace.expect(players_teams_id_parser) 
    def delete(self):
        try:
            players_teamss = db.session.query(players_teams).filter(players_teams.id==players_teams_id_parser.parse_args().get('id') ).first() 
            db.session.query(players_teams).filter(players_teams.id==players_teams_id_parser.parse_args().get('id') ).delete() 
            db.session.commit() 
        except Exception as e:
            print(e)
            return None , 500
        return players_teamss , 200    

get_players_teams_filteredby_name_model = players_teams_namespace.model('get_players_teams_filteredby_name_model',{ 'teams.year' : fields.Integer,'players.playerID' : fields.String,'teams.name' : fields.String,'count_all' : fields.Integer })
get_players_teams_filteredby_name_parser = reqparse.RequestParser()
get_players_teams_filteredby_name_parser.add_argument('teams.name', type=str, required=True, location='args')

@players_teams_namespace.route('/get_players_teams_filteredby_name', methods=['GET'])
class get_players_teams_filteredby_name_resource(Resource):
    @players_teams_namespace.marshal_list_with(get_players_teams_filteredby_name_model)
    @players_teams_namespace.expect(get_players_teams_filteredby_name_parser)

    def get(self):
        args = get_players_teams_filteredby_name_parser.parse_args()

        results = None
        try:
            results = db.session.query(teams, teams.year, players, players.playerID, teams.name, func.count().label('count_all'))\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.filter(teams.name == args['teams.name'])\
				.group_by(players.playerID, teams.year, teams.name).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_teams_filteredby_name_year_model = players_teams_namespace.model('get_players_teams_filteredby_name_year_model',{ 'players.middleName' : fields.String,'players.firstName' : fields.String,'players.lastName' : fields.String })
get_players_teams_filteredby_name_year_parser = reqparse.RequestParser()
get_players_teams_filteredby_name_year_parser.add_argument('teams.name', type=str, required=True, location='args')
get_players_teams_filteredby_name_year_parser.add_argument('teams.year', type=int, required=True, location='args')

@players_teams_namespace.route('/get_players_teams_filteredby_name_year', methods=['GET'])
class get_players_teams_filteredby_name_year_resource(Resource):
    @players_teams_namespace.marshal_list_with(get_players_teams_filteredby_name_year_model)
    @players_teams_namespace.expect(get_players_teams_filteredby_name_year_parser)

    def get(self):
        args = get_players_teams_filteredby_name_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.middleName, players.firstName, players.lastName)\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.filter(teams.name == args['teams.name'], teams.year == args['teams.year']).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_teams_filteredby_year_model = players_teams_namespace.model('get_players_teams_filteredby_year_model',{ 'teams.year' : fields.Integer,'players.middleName' : fields.String,'players.firstName' : fields.String,'count_teams.year' : fields.Integer })
get_players_teams_filteredby_year_parser = reqparse.RequestParser()
get_players_teams_filteredby_year_parser.add_argument('teams.year', type=int, required=True, location='args')
get_players_teams_filteredby_year_parser.add_argument('teams.year', type=int, required=True, location='args')

@players_teams_namespace.route('/get_players_teams_filteredby_year', methods=['GET'])
class get_players_teams_filteredby_year_resource(Resource):
    @players_teams_namespace.marshal_list_with(get_players_teams_filteredby_year_model)
    @players_teams_namespace.expect(get_players_teams_filteredby_year_parser)

    def get(self):
        args = get_players_teams_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(teams, teams.year, players, players.middleName, players.firstName, func.count(teams.year).label('count_teams.year'))\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.filter(teams.year == args['teams.year'])\
				.group_by(players.firstName, teams.year, players.middleName).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_teams_groupedby_playerID_model = players_teams_namespace.model('get_players_teams_groupedby_playerID_model',{ 'players.middleName' : fields.String,'players.firstName' : fields.String })

@players_teams_namespace.route('/get_players_teams_groupedby_playerID', methods=['GET'])
class get_players_teams_groupedby_playerID_resource(Resource):
    @players_teams_namespace.marshal_list_with(get_players_teams_groupedby_playerID_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, players.middleName, players.firstName)\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.group_by(players.playerID).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_teams_groupedby_year_model = players_teams_namespace.model('get_players_teams_groupedby_year_model',{ 'teams.year' : fields.Integer,'count_teams.year' : fields.Integer })

@players_teams_namespace.route('/get_players_teams_groupedby_year', methods=['GET'])
class get_players_teams_groupedby_year_resource(Resource):
    @players_teams_namespace.marshal_list_with(get_players_teams_groupedby_year_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(teams, teams.year, func.count(teams.year).label('count_teams.year'))\
				.join(players, players.playerID == players_teams.playerID)\
				.join(players_teams, players_teams.tmID == teams.tmID)\
				.group_by(teams.year).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_teams_model = players_teams_namespace.model('get_players_teams_model',{ 'count_all' : fields.Integer })

@players_teams_namespace.route('/get_players_teams', methods=['GET'])
class get_players_teams_resource(Resource):
    @players_teams_namespace.marshal_list_with(get_players_teams_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(func.count().label('count_all')).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

