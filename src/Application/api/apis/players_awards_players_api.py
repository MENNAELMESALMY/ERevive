from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , awards_players 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_awards_players_namespace = Namespace("players_awards_players", description="players_awards_players Api") 
get_players_awards_players_groupedby_playerID_model = players_awards_players_namespace.model('get_players_awards_players_groupedby_playerID_model',{ 'players.playerID' : fields.String,'players.hsCity' : fields.String,'players.firstName' : fields.String,'players.birthCountry' : fields.String,'awards_players.year' : fields.Integer,'players.middleName' : fields.String,'players.birthCity' : fields.String })
get_players_awards_players_groupedby_playerID_parser = reqparse.RequestParser()
get_players_awards_players_groupedby_playerID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_groupedby_playerID', methods=['GET'])
class get_players_awards_players_groupedby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_groupedby_playerID_model)
    @players_awards_players_namespace.expect(get_players_awards_players_groupedby_playerID_parser)

    def get(self):
        args = get_players_awards_players_groupedby_playerID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(players, players.playerID, players.hsCity, players.firstName, players.birthCountry, awards_players, awards_players.year, players.middleName, players.birthCity)\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(awards_players.year, players.firstName, players.hsCity, players.middleName, players.birthCity, players.playerID, players.birthCountry)\
				.order_by(direction(func.count())).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_players_filteredby_playerID_model = players_awards_players_namespace.model('get_players_awards_players_filteredby_playerID_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'count_all' : fields.Integer })
get_players_awards_players_filteredby_playerID_parser = reqparse.RequestParser()
get_players_awards_players_filteredby_playerID_parser.add_argument('awards_players.playerID', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_filteredby_playerID', methods=['GET'])
class get_players_awards_players_filteredby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_filteredby_playerID_model)
    @players_awards_players_namespace.expect(get_players_awards_players_filteredby_playerID_parser)

    def get(self):
        args = get_players_awards_players_filteredby_playerID_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, awards_players, func.count().label('count_all'))\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.filter(awards_players.playerID.like(args['awards_players.playerID']))\
				.group_by(players.birthDate, players.nameGiven, players.hsCity, players.deathDate, awards_players.note, awards_players.playerID, players.birthCountry, players.firstseason, players.lastName, awards_players.pos, players.college, players.nameSuffix, players.hsCountry, awards_players.award, players.firstName, players.pos, players.race, players.middleName, players.nameNick, players.birthCity, players.lastseason, players.weight, players.collegeOther, players.height, players.birthState, players.hsState, awards_players.year, players.useFirst, awards_players.lgID, players.fullGivenName, players.playerID, players.highSchool).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_players_model = players_awards_players_namespace.model('get_players_awards_players_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'count_players.playerID' : fields.String,'count_all' : fields.Integer })

@players_awards_players_namespace.route('/get_players_awards_players', methods=['GET'])
class get_players_awards_players_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, awards_players, func.count().label('count_all'))\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(players.birthDate, players.nameGiven, players.hsCity, players.deathDate, awards_players.note, awards_players.playerID, players.birthCountry, players.firstseason, players.lastName, awards_players.pos, players.college, players.nameSuffix, players.hsCountry, awards_players.award, players.firstName, players.pos, players.race, players.middleName, players.nameNick, players.birthCity, players.lastseason, players.weight, players.collegeOther, players.height, players.birthState, players.hsState, awards_players.year, players.useFirst, awards_players.lgID, players.fullGivenName, players.playerID, players.highSchool).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_players_filteredby_firstName_model = players_awards_players_namespace.model('get_players_awards_players_filteredby_firstName_model',{ 'players.playerID' : fields.String,'players.middleName' : fields.String,'players.firstName' : fields.String,'players.height' : fields.Float,'avg_players.height' : fields.Float,'count_all' : fields.Integer })
get_players_awards_players_filteredby_firstName_parser = reqparse.RequestParser()
get_players_awards_players_filteredby_firstName_parser.add_argument('players.firstName', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_filteredby_firstName', methods=['GET'])
class get_players_awards_players_filteredby_firstName_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_filteredby_firstName_model)
    @players_awards_players_namespace.expect(get_players_awards_players_filteredby_firstName_parser)

    def get(self):
        args = get_players_awards_players_filteredby_firstName_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID, players.middleName, players.firstName, players.height, func.avg(players.height).label('avg_players.height'), func.count().label('count_all'))\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.filter(players.firstName == args['players.firstName'])\
				.group_by(players.playerID, players.firstName, players.height, players.middleName).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_players_model = players_awards_players_namespace.model('get_players_awards_players_model',{ 'awards_players.playerID' : fields.String })
get_players_awards_players_parser = reqparse.RequestParser()
get_players_awards_players_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players', methods=['GET'])
class get_players_awards_players_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_model)
    @players_awards_players_namespace.expect(get_players_awards_players_parser)

    def get(self):
        args = get_players_awards_players_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_players, awards_players.playerID)\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(awards_players.playerID)\
				.order_by(direction(func.count())).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_players_orderedby_height_model = players_awards_players_namespace.model('get_players_awards_players_orderedby_height_model',{ 'awards_players.playerID' : fields.String })
get_players_awards_players_orderedby_height_parser = reqparse.RequestParser()
get_players_awards_players_orderedby_height_parser.add_argument('is_order_of_height_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_orderedby_height', methods=['GET'])
class get_players_awards_players_orderedby_height_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_orderedby_height_model)
    @players_awards_players_namespace.expect(get_players_awards_players_orderedby_height_parser)

    def get(self):
        args = get_players_awards_players_orderedby_height_parser.parse_args()
        height_direction = desc if args['is_order_of_height_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_players, awards_players.playerID)\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.order_by(height_direction(players.height)).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_players_groupedby_playerID_model = players_awards_players_namespace.model('get_players_awards_players_groupedby_playerID_model',{ 'awards_players.playerID' : fields.String })
get_players_awards_players_groupedby_playerID_parser = reqparse.RequestParser()
get_players_awards_players_groupedby_playerID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_groupedby_playerID', methods=['GET'])
class get_players_awards_players_groupedby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_groupedby_playerID_model)
    @players_awards_players_namespace.expect(get_players_awards_players_groupedby_playerID_parser)

    def get(self):
        args = get_players_awards_players_groupedby_playerID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_players, awards_players.playerID)\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(awards_players.playerID)\
				.order_by(direction(func.count())).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_players_groupedby_playerID_orderedby_playerID_model = players_awards_players_namespace.model('get_players_awards_players_groupedby_playerID_orderedby_playerID_model',{ 'players.playerID' : fields.String,'count_all' : fields.Integer })
get_players_awards_players_groupedby_playerID_orderedby_playerID_parser = reqparse.RequestParser()
get_players_awards_players_groupedby_playerID_orderedby_playerID_parser.add_argument('is_order_of_playerID_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_groupedby_playerID_orderedby_playerID', methods=['GET'])
class get_players_awards_players_groupedby_playerID_orderedby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_groupedby_playerID_orderedby_playerID_model)
    @players_awards_players_namespace.expect(get_players_awards_players_groupedby_playerID_orderedby_playerID_parser)

    def get(self):
        args = get_players_awards_players_groupedby_playerID_orderedby_playerID_parser.parse_args()
        playerID_direction = desc if args['is_order_of_playerID_desc'] else asc

        results = None
        try:
            results = db.session.query(players, players.playerID, func.count().label('count_all'))\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(players.playerID)\
				.order_by(playerID_direction(players.playerID)).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

