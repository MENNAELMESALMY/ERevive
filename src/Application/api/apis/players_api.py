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
            return None , 500
        return playerss , 200    

get_players_filteredby_playerID_model = players_namespace.model('get_players_filteredby_playerID_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'count_players.firstName' : fields.String,'count_players.birthDate' : fields.DateTime,'count_all' : fields.Integer,'min_players.hsCity' : fields.String,'count_players.playerID' : fields.String })
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
            results = db.session.query(players, func.count(players.firstName).label('count_players.firstName'), func.count(players.birthDate).label('count_players.birthDate'), func.count().label('count_all'), func.min(players.hsCity).label('min_players.hsCity'), func.count(players.playerID).label('count_players.playerID'))\
				.filter(players.playerID == args['players.playerID'])\
				.group_by(players.hsCity, players.height, players.lastseason, players.hsCountry, players.birthState, players.nameNick, players.weight, players.hsState, players.firstseason, players.deathDate, players.nameSuffix, players.lastName, players.playerID, players.race, players.nameGiven, players.fullGivenName, players.highSchool, players.birthCity, players.useFirst, players.collegeOther, players.firstName, players.birthDate, players.pos, players.middleName, players.college, players.birthCountry).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_filteredby_middleName_firstName_model = players_namespace.model('get_players_filteredby_middleName_firstName_model',{ 'players.firstName' : fields.String,'players.middleName' : fields.String,'players.playerID' : fields.String,'players.birthDate' : fields.DateTime,'count_players.birthDate' : fields.DateTime,'count_players.playerID' : fields.String,'count_all' : fields.Integer,'count_players.firstName' : fields.String })
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
            results = db.session.query(players.firstName, players.middleName, players.playerID, players.birthDate, func.count(players.birthDate).label('count_players.birthDate'), func.count(players.playerID).label('count_players.playerID'), func.count().label('count_all'), func.count(players.firstName).label('count_players.firstName'))\
				.filter(players.middleName == args['players.middleName'], players.firstName != args['players.firstName'])\
				.group_by(players.middleName, players.firstName, players.birthDate, players.playerID).all()

        except Exception as e:
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
            results = db.session.query(players, func.count().label('count_all'))\
				.filter(players.height < args['players.height'])\
				.group_by(players.hsCity, players.height, players.lastseason, players.hsCountry, players.birthState, players.nameNick, players.weight, players.hsState, players.firstseason, players.deathDate, players.nameSuffix, players.lastName, players.playerID, players.race, players.nameGiven, players.fullGivenName, players.highSchool, players.birthCity, players.useFirst, players.collegeOther, players.firstName, players.birthDate, players.pos, players.middleName, players.college, players.birthCountry).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_model = players_namespace.model('get_players_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'max_players.weight' : fields.Integer,'min_players.playerID' : fields.String,'count_players.birthCountry' : fields.String,'count_players.firstName' : fields.String,'max_players.hsCity' : fields.String,'avg_players.height' : fields.Float,'min_players.birthDate' : fields.DateTime,'count_all' : fields.Integer,'max_players.playerID' : fields.String,'avg_players.weight' : fields.Integer,'min_players.weight' : fields.Integer,'min_players.hsCity' : fields.String,'avg_players.hsCity' : fields.String,'max_players.height' : fields.Float,'count_players.playerID' : fields.String,'avg_players.playerID' : fields.String,'max_players.birthDate' : fields.DateTime })

@players_namespace.route('/get_players', methods=['GET'])
class get_players_resource(Resource):
    @players_namespace.marshal_list_with(get_players_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, func.max(players.weight).label('max_players.weight'), func.min(players.playerID).label('min_players.playerID'), func.count(players.birthCountry).label('count_players.birthCountry'), func.count(players.firstName).label('count_players.firstName'), func.max(players.hsCity).label('max_players.hsCity'), func.avg(players.height).label('avg_players.height'), func.min(players.birthDate).label('min_players.birthDate'), func.count().label('count_all'), func.max(players.playerID).label('max_players.playerID'), func.avg(players.weight).label('avg_players.weight'), func.min(players.weight).label('min_players.weight'), func.min(players.hsCity).label('min_players.hsCity'), func.avg(players.hsCity).label('avg_players.hsCity'), func.max(players.height).label('max_players.height'), func.count(players.playerID).label('count_players.playerID'), func.avg(players.playerID).label('avg_players.playerID'), func.max(players.birthDate).label('max_players.birthDate'))\
				.group_by(players.hsCity, players.height, players.lastseason, players.hsCountry, players.birthState, players.nameNick, players.weight, players.hsState, players.firstseason, players.deathDate, players.nameSuffix, players.lastName, players.playerID, players.race, players.nameGiven, players.fullGivenName, players.highSchool, players.birthCity, players.useFirst, players.collegeOther, players.firstName, players.birthDate, players.pos, players.middleName, players.college, players.birthCountry).all()

        except Exception as e:
            return None , 400

        return results , 200

