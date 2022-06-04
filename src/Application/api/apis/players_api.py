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
        playerss = db.session.query(players).all()
        return playerss , 200  

    @players_namespace.marshal_with(players_model) 
    @players_namespace.expect(players_model) 
    def post(self):
        players = players(playerID = request.json.get("playerID"),useFirst = request.json.get("useFirst"),firstName = request.json.get("firstName"),middleName = request.json.get("middleName"),lastName = request.json.get("lastName"),nameGiven = request.json.get("nameGiven"),fullGivenName = request.json.get("fullGivenName"),nameSuffix = request.json.get("nameSuffix"),nameNick = request.json.get("nameNick"),pos = request.json.get("pos"),firstseason = request.json.get("firstseason"),lastseason = request.json.get("lastseason"),height = request.json.get("height"),weight = request.json.get("weight"),college = request.json.get("college"),collegeOther = request.json.get("collegeOther"),birthDate = request.json.get("birthDate"),birthCity = request.json.get("birthCity"),birthState = request.json.get("birthState"),birthCountry = request.json.get("birthCountry"),highSchool = request.json.get("highSchool"),hsCity = request.json.get("hsCity"),hsState = request.json.get("hsState"),hsCountry = request.json.get("hsCountry"),deathDate = request.json.get("deathDate"),race = request.json.get("race"))
        db.session.add(players)
        db.session.commit()    
        return players , 201 

    @players_namespace.marshal_with(players_model) 
    @players_namespace.expect(players_model) 
    def put(self):
        db.session.query(players).filter(players.id==id).update(request.json) 
        db.session.commit() 
        players = db.session.query(players).filter(players.id==id).first() 
        return players , 200    

    @players_namespace.marshal_with(players_model) 
    @players_namespace.expect(players_id_parser) 
    def delete(self):
        players = db.session.query(players).filter(players.id==id).first() 
        db.session.query(players).filter(players.id==id).delete() 
        db.session.commit() 
        return players , 200    

get_players_filteredby_playerID_model = players_namespace.model('get_players_filteredby_playerID_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'count_all' : fields.Integer,'count_players.playerID' : fields.String,'count_players.firstName' : fields.String,'count_players.birthDate' : fields.DateTime,'min_players.hsCity' : fields.String })
get_players_filteredby_playerID_parser = reqparse.RequestParser()
get_players_filteredby_playerID_parser.add_argument('players.playerID', type=str, required=True, location='args')

@players_namespace.route('/get_players_filteredby_playerID', methods=['GET'])
class get_players_filteredby_playerID_resource(Resource):
    @players_namespace.marshal_list_with(get_players_filteredby_playerID_model)
    @players_namespace.expect(get_players_filteredby_playerID_parser)

    def get(self):
        args = get_players_filteredby_playerID_parser.parse_args()

        results = db.session.query(players, func.count().label('count_all'), func.count(players.playerID).label('count_players.playerID'), func.count(players.firstName).label('count_players.firstName'), func.count(players.birthDate).label('count_players.birthDate'), func.min(players.hsCity).label('min_players.hsCity'))\
			.filter(players.playerID == args['players.playerID'])
        return results

get_players_filteredby_firstName_middleName_model = players_namespace.model('get_players_filteredby_firstName_middleName_model',{ 'players.firstName' : fields.String,'players.middleName' : fields.String,'players.birthDate' : fields.DateTime,'players.playerID' : fields.String,'count_players.playerID' : fields.String,'count_all' : fields.Integer,'count_players.firstName' : fields.String,'count_players.birthDate' : fields.DateTime })
get_players_filteredby_firstName_middleName_parser = reqparse.RequestParser()
get_players_filteredby_firstName_middleName_parser.add_argument('players.firstName', type=str, required=True, location='args')
get_players_filteredby_firstName_middleName_parser.add_argument('players.middleName', type=str, required=True, location='args')

@players_namespace.route('/get_players_filteredby_firstName_middleName', methods=['GET'])
class get_players_filteredby_firstName_middleName_resource(Resource):
    @players_namespace.marshal_list_with(get_players_filteredby_firstName_middleName_model)
    @players_namespace.expect(get_players_filteredby_firstName_middleName_parser)

    def get(self):
        args = get_players_filteredby_firstName_middleName_parser.parse_args()

        results = db.session.query(players.firstName, players.middleName, players.birthDate, players.playerID, func.count(players.playerID).label('count_players.playerID'), func.count().label('count_all'), func.count(players.firstName).label('count_players.firstName'), func.count(players.birthDate).label('count_players.birthDate'))\
			.filter(players.firstName != args['players.firstName'], players.middleName == args['players.middleName'])\
			.group_by(players.birthDate, players.middleName, players.playerID, players.firstName)
        return results

get_players_filteredby_height_model = players_namespace.model('get_players_filteredby_height_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'count_all' : fields.Integer })
get_players_filteredby_height_parser = reqparse.RequestParser()
get_players_filteredby_height_parser.add_argument('players.height', type=float, required=True, location='args')

@players_namespace.route('/get_players_filteredby_height', methods=['GET'])
class get_players_filteredby_height_resource(Resource):
    @players_namespace.marshal_list_with(get_players_filteredby_height_model)
    @players_namespace.expect(get_players_filteredby_height_parser)

    def get(self):
        args = get_players_filteredby_height_parser.parse_args()

        results = db.session.query(players, func.count().label('count_all'))\
			.filter(players.height < args['players.height'])
        return results

get_players_model = players_namespace.model('get_players_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'count_all' : fields.Integer,'max_players.height' : fields.Float,'max_players.weight' : fields.Integer,'avg_players.hsCity' : fields.String,'min_players.weight' : fields.Integer,'avg_players.playerID' : fields.String,'min_players.birthDate' : fields.DateTime,'max_players.hsCity' : fields.String,'min_players.playerID' : fields.String,'count_players.playerID' : fields.String,'count_players.firstName' : fields.String,'avg_players.weight' : fields.Integer,'max_players.birthDate' : fields.DateTime,'count_players.birthCountry' : fields.String,'max_players.playerID' : fields.String,'min_players.hsCity' : fields.String,'avg_players.height' : fields.Float })

@players_namespace.route('/get_players', methods=['GET'])
class get_players_resource(Resource):
    @players_namespace.marshal_list_with(get_players_model)
    
    def get(self):
        
        results = db.session.query(players, func.count().label('count_all'), func.max(players.height).label('max_players.height'), func.max(players.weight).label('max_players.weight'), func.avg(players.hsCity).label('avg_players.hsCity'), func.min(players.weight).label('min_players.weight'), func.avg(players.playerID).label('avg_players.playerID'), func.min(players.birthDate).label('min_players.birthDate'), func.max(players.hsCity).label('max_players.hsCity'), func.min(players.playerID).label('min_players.playerID'), func.count(players.playerID).label('count_players.playerID'), func.count(players.firstName).label('count_players.firstName'), func.avg(players.weight).label('avg_players.weight'), func.max(players.birthDate).label('max_players.birthDate'), func.count(players.birthCountry).label('count_players.birthCountry'), func.max(players.playerID).label('max_players.playerID'), func.min(players.hsCity).label('min_players.hsCity'), func.avg(players.height).label('avg_players.height'))
        return results

get_players_groupedby_playerID_model = players_namespace.model('get_players_groupedby_playerID_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'count_all' : fields.Integer })
get_players_groupedby_playerID_parser = reqparse.RequestParser()
get_players_groupedby_playerID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_namespace.route('/get_players_groupedby_playerID', methods=['GET'])
class get_players_groupedby_playerID_resource(Resource):
    @players_namespace.marshal_list_with(get_players_groupedby_playerID_model)
    @players_namespace.expect(get_players_groupedby_playerID_parser)

    def get(self):
        args = get_players_groupedby_playerID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(players, func.count().label('count_all'))\
			.group_by(players.playerID)\
			.order_by(direction(func.count()))
        return results

get_players_orderedby_weight_model = players_namespace.model('get_players_orderedby_weight_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'count_players.playerID' : fields.String,'count_all' : fields.Integer })
get_players_orderedby_weight_parser = reqparse.RequestParser()
get_players_orderedby_weight_parser.add_argument('is_order_of_weight_desc', type=bool, required=True, location='args')

@players_namespace.route('/get_players_orderedby_weight', methods=['GET'])
class get_players_orderedby_weight_resource(Resource):
    @players_namespace.marshal_list_with(get_players_orderedby_weight_model)
    @players_namespace.expect(get_players_orderedby_weight_parser)

    def get(self):
        args = get_players_orderedby_weight_parser.parse_args()
        weight_direction = desc if args['is_order_of_weight_desc'] else asc

        results = db.session.query(players, func.count(players.playerID).label('count_players.playerID'), func.count().label('count_all'))\
			.order_by(weight_direction(players.weight))
        return results

