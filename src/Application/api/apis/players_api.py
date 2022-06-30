from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
players_namespace = Namespace("players", description="players Api") 


players_model =players_namespace.model("players",convert_db_model_to_restx_model(players)) 
players_id_parser = reqparse.RequestParser() 
players_id_parser.add_argument('playerID',type=str)


@players_namespace.route("/")
class playersApi(Resource):

    def get(self):
        try:
            playerss = db.session.query(players).all()
            playerss = [row.serialize() for row in playerss]
            return playerss , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @players_namespace.expect(players_model) 
    def post(self):
        try:
            playerss = players(playerID = request.json.get("playerID"),useFirst = request.json.get("useFirst"),firstName = request.json.get("firstName"),middleName = request.json.get("middleName"),lastName = request.json.get("lastName"),nameGiven = request.json.get("nameGiven"),fullGivenName = request.json.get("fullGivenName"),nameSuffix = request.json.get("nameSuffix"),nameNick = request.json.get("nameNick"),pos = request.json.get("pos"),firstseason = request.json.get("firstseason"),lastseason = request.json.get("lastseason"),height = request.json.get("height"),weight = request.json.get("weight"),college = request.json.get("college"),collegeOther = request.json.get("collegeOther"),birthDate = request.json.get("birthDate"),birthCity = request.json.get("birthCity"),birthState = request.json.get("birthState"),birthCountry = request.json.get("birthCountry"),highSchool = request.json.get("highSchool"),hsCity = request.json.get("hsCity"),hsState = request.json.get("hsState"),hsCountry = request.json.get("hsCountry"),deathDate = request.json.get("deathDate"),race = request.json.get("race"))
            db.session.add(playerss)
            db.session.commit()    
            return playerss.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @players_namespace.expect(players_model) 
    def put(self):
        try:
            db.session.query(players).filter(players.playerID==request.json.get('playerID') ).update(request.json) 
            db.session.commit() 
            playerss = db.session.query(players).filter(players.playerID==request.json.get('playerID') ).first() 
            return playerss.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @players_namespace.expect(players_id_parser) 
    def delete(self):
        try:
            playerss = db.session.query(players).filter(players.playerID==players_id_parser.parse_args().get('playerID') ).first() 
            db.session.query(players).filter(players.playerID==players_id_parser.parse_args().get('playerID') ).delete() 
            db.session.commit() 
            return playerss.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_filteredby_playerID_groupedby_all_parser = reqparse.RequestParser()
get_players_filteredby_playerID_groupedby_all_parser.add_argument('players.playerID', type=str, required=True, location='args')

@players_namespace.route('/get_players_filteredby_playerID_groupedby_all', methods=['GET'])
class get_players_filteredby_playerID_groupedby_all_resource(Resource):
    
    @players_namespace.expect(get_players_filteredby_playerID_groupedby_all_parser)
    def get(self):
        args = get_players_filteredby_playerID_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID.label('players.playerID'), func.count().label('count_all'), func.min(players.hsCity).label('min_players.hsCity'))\
				.filter(players.playerID != args['players.playerID'])\
				.group_by(players.hsState, players.college, players.firstName, players.nameNick, players.highSchool, players.nameGiven, players.weight, players.birthCountry, players.height, players.lastName, players.useFirst, players.lastseason, players.pos, players.birthState, players.collegeOther, players.deathDate, players.birthDate, players.nameSuffix, players.hsCountry, players.firstseason, players.race, players.hsCity, players.birthCity, players.playerID, players.middleName, players.fullGivenName).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_filteredby_height_groupedby_all_parser = reqparse.RequestParser()
get_players_filteredby_height_groupedby_all_parser.add_argument('players.height', type=float, required=True, location='args')

@players_namespace.route('/get_players_filteredby_height_groupedby_all', methods=['GET'])
class get_players_filteredby_height_groupedby_all_resource(Resource):
    
    @players_namespace.expect(get_players_filteredby_height_groupedby_all_parser)
    def get(self):
        args = get_players_filteredby_height_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID.label('players.playerID'), func.count().label('count_all'))\
				.filter(players.height < args['players.height'])\
				.group_by(players.hsState, players.college, players.firstName, players.nameNick, players.highSchool, players.nameGiven, players.weight, players.birthCountry, players.height, players.lastName, players.useFirst, players.lastseason, players.pos, players.birthState, players.collegeOther, players.deathDate, players.birthDate, players.nameSuffix, players.hsCountry, players.firstseason, players.race, players.hsCity, players.birthCity, players.playerID, players.middleName, players.fullGivenName).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_filteredby_weight_groupedby_all_parser = reqparse.RequestParser()
get_players_filteredby_weight_groupedby_all_parser.add_argument('players.weight', type=int, required=True,action='append', location='args')

@players_namespace.route('/get_players_filteredby_weight_groupedby_all', methods=['GET'])
class get_players_filteredby_weight_groupedby_all_resource(Resource):
    
    @players_namespace.expect(get_players_filteredby_weight_groupedby_all_parser)
    def get(self):
        args = get_players_filteredby_weight_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID.label('players.playerID'), func.count().label('count_all'))\
				.filter(players.weight.in_(args['players.weight']))\
				.group_by(players.hsState, players.college, players.firstName, players.nameNick, players.highSchool, players.nameGiven, players.weight, players.birthCountry, players.height, players.lastName, players.useFirst, players.lastseason, players.pos, players.birthState, players.collegeOther, players.deathDate, players.birthDate, players.nameSuffix, players.hsCountry, players.firstseason, players.race, players.hsCity, players.birthCity, players.playerID, players.middleName, players.fullGivenName).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_namespace.route('/get_players_groupedby_all', methods=['GET'])
class get_players_groupedby_all_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, players.playerID.label('players.playerID'), func.max(players.height).label('max_players.height'), func.avg(players.hsCity).label('avg_players.hsCity'), func.min(players.playerID).label('min_players.playerID'), func.max(players.birthDate).label('max_players.birthDate'), func.count().label('count_all'), func.avg(players.weight).label('avg_players.weight'), func.max(players.hsCity).label('max_players.hsCity'), func.min(players.weight).label('min_players.weight'), func.avg(players.playerID).label('avg_players.playerID'), func.avg(players.height).label('avg_players.height'), func.min(players.birthDate).label('min_players.birthDate'), func.min(players.hsCity).label('min_players.hsCity'), func.max(players.playerID).label('max_players.playerID'), func.max(players.weight).label('max_players.weight'))\
				.group_by(players.hsState, players.college, players.firstName, players.nameNick, players.highSchool, players.nameGiven, players.weight, players.birthCountry, players.height, players.lastName, players.useFirst, players.lastseason, players.pos, players.birthState, players.collegeOther, players.deathDate, players.birthDate, players.nameSuffix, players.hsCountry, players.firstseason, players.race, players.hsCity, players.birthCity, players.playerID, players.middleName, players.fullGivenName).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

