from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_namespace = Namespace("players", description="players Api") 


players_model =players_namespace.model("players",convert_db_model_to_restx_model(players)) 
players_id_parser = reqparse.RequestParser() 
players_id_parser.add_argument('playerID',type=str)


@players_namespace.route("/")
class playersApi(Resource):

    @players_namespace.marshal_list_with(players_model) 
    def get(self):
        try:
            playerss = db.session.query(players).all()
        except Exception as e:
            print(e)
            return None , 500
        return playerss , 200  

    @players_namespace.marshal_with(players_model) 
    @players_namespace.expect(players_model) 
    def post(self):
        try:
            playerss = players(playerID = request.json.get("playerID"),useFirst = request.json.get("useFirst"),firstName = request.json.get("firstName"),middleName = request.json.get("middleName"),lastName = request.json.get("lastName"),nameGiven = request.json.get("nameGiven"),fullGivenName = request.json.get("fullGivenName"),nameSuffix = request.json.get("nameSuffix"),nameNick = request.json.get("nameNick"),pos = request.json.get("pos"),firstseason = request.json.get("firstseason"),lastseason = request.json.get("lastseason"),height = request.json.get("height"),weight = request.json.get("weight"),college = request.json.get("college"),collegeOther = request.json.get("collegeOther"),birthDate = request.json.get("birthDate"),birthCity = request.json.get("birthCity"),birthState = request.json.get("birthState"),birthCountry = request.json.get("birthCountry"),highSchool = request.json.get("highSchool"),hsCity = request.json.get("hsCity"),hsState = request.json.get("hsState"),hsCountry = request.json.get("hsCountry"),deathDate = request.json.get("deathDate"),race = request.json.get("race"))
            db.session.add(playerss)
            db.session.commit()    
        except Exception as e:
            print(e)
            return None , 500
        return playerss , 201 

    @players_namespace.marshal_with(players_model) 
    @players_namespace.expect(players_model) 
    def put(self):
        try:
            db.session.query(players).filter(players.playerID==request.json.get('playerID') ).update(request.json) 
            db.session.commit() 
            playerss = db.session.query(players).filter(players.playerID==request.json.get('playerID') ).first() 
        except Exception as e:
            print(e)
            return None , 500
        return playerss , 200    

    @players_namespace.marshal_with(players_model) 
    @players_namespace.expect(players_id_parser) 
    def delete(self):
        try:
            playerss = db.session.query(players).filter(players.playerID==players_id_parser.parse_args().get('playerID') ).first() 
            db.session.query(players).filter(players.playerID==players_id_parser.parse_args().get('playerID') ).delete() 
            db.session.commit() 
        except Exception as e:
            print(e)
            return None , 500
        return playerss , 200    

get_players_filteredby_playerID_model = players_namespace.model('get_players_filteredby_playerID_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'count_players.firstName' : fields.String,'count_all' : fields.Integer,'count_players.playerID' : fields.String,'min_players.hsCity' : fields.String,'count_players.birthDate' : fields.DateTime,'count_players.middleName' : fields.String })
get_players_filteredby_playerID_parser = reqparse.RequestParser()
get_players_filteredby_playerID_parser.add_argument('players.playerID', type=str, required=True, location='args')

@players_namespace.route('/get_players_filteredby_playerID', methods=['GET'])
class get_players_filteredby_playerID_resource(Resource):
    @players_namespace.marshal_list_with(get_players_filteredby_playerID_model)
    @players_namespace.expect(get_players_filteredby_playerID_parser)

    def get(self):
        args = get_players_filteredby_playerID_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID.label('players.playerID'), func.count().label('count_all'), func.min(players.hsCity).label('min_players.hsCity'))\
				.filter(players.playerID == args['players.playerID'])\
				.group_by(players.nameSuffix, players.birthDate, players.hsCountry, players.nameGiven, players.firstName, players.pos, players.hsCity, players.race, players.middleName, players.nameNick, players.deathDate, players.birthCity, players.lastseason, players.weight, players.birthCountry, players.firstseason, players.lastName, players.collegeOther, players.height, players.birthState, players.hsState, players.college, players.useFirst, players.fullGivenName, players.playerID, players.highSchool).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_filteredby_middleName_firstName_model = players_namespace.model('get_players_filteredby_middleName_firstName_model',{ 'players.playerID' : fields.String,'players.birthDate' : fields.DateTime,'players.middleName' : fields.String,'players.firstName' : fields.String,'count_all' : fields.Integer,'count_players.playerID' : fields.String,'count_players.firstName' : fields.String,'count_players.birthDate' : fields.DateTime })
get_players_filteredby_middleName_firstName_parser = reqparse.RequestParser()
get_players_filteredby_middleName_firstName_parser.add_argument('players.middleName', type=str, required=True, location='args')
get_players_filteredby_middleName_firstName_parser.add_argument('players.firstName', type=str, required=True, location='args')

@players_namespace.route('/get_players_filteredby_middleName_firstName', methods=['GET'])
class get_players_filteredby_middleName_firstName_resource(Resource):
    @players_namespace.marshal_list_with(get_players_filteredby_middleName_firstName_model)
    @players_namespace.expect(get_players_filteredby_middleName_firstName_parser)

    def get(self):
        args = get_players_filteredby_middleName_firstName_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID, players.birthDate, players.middleName, players.firstName, func.count().label('count_all'))\
				.filter(players.middleName == args['players.middleName'], players.firstName != args['players.firstName'])\
				.group_by(players.birthDate, players.playerID, players.firstName, players.middleName).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_filteredby_height_model = players_namespace.model('get_players_filteredby_height_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'count_all' : fields.Integer })
get_players_filteredby_height_parser = reqparse.RequestParser()
get_players_filteredby_height_parser.add_argument('players.height', type=float, required=True, location='args')

@players_namespace.route('/get_players_filteredby_height', methods=['GET'])
class get_players_filteredby_height_resource(Resource):
    @players_namespace.marshal_list_with(get_players_filteredby_height_model)
    @players_namespace.expect(get_players_filteredby_height_parser)

    def get(self):
        args = get_players_filteredby_height_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID.label('players.playerID'), func.count().label('count_all'))\
				.filter(players.height < args['players.height'])\
				.group_by(players.nameSuffix, players.birthDate, players.hsCountry, players.nameGiven, players.firstName, players.pos, players.hsCity, players.race, players.middleName, players.nameNick, players.deathDate, players.birthCity, players.lastseason, players.weight, players.birthCountry, players.firstseason, players.lastName, players.collegeOther, players.height, players.birthState, players.hsState, players.college, players.useFirst, players.fullGivenName, players.playerID, players.highSchool).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

