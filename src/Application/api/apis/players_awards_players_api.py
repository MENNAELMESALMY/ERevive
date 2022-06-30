from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , awards_players 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
players_awards_players_namespace = Namespace("players_awards_players", description="players_awards_players Api") 
get_players_awards_players_filteredby_playerID_groupedby_all_parser = reqparse.RequestParser()
get_players_awards_players_filteredby_playerID_groupedby_all_parser.add_argument('players.playerID', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_filteredby_playerID_groupedby_all', methods=['GET'])
class get_players_awards_players_filteredby_playerID_groupedby_all_resource(Resource):
    
    @players_awards_players_namespace.expect(get_players_awards_players_filteredby_playerID_groupedby_all_parser)
    def get(self):
        args = get_players_awards_players_filteredby_playerID_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, awards_players, func.avg(players.height).label('avg_players.height'), func.count().label('count_all'))\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.filter(players.playerID >= args['players.playerID'])\
				.group_by(players.hsState, awards_players.year, awards_players.award, players.nameGiven, players.weight, awards_players.playerID, players.height, players.lastseason, awards_players.lgID, players.birthState, players.hsCountry, players.race, awards_players.pos, players.hsCity, players.birthCity, players.playerID, players.fullGivenName, players.college, players.firstName, players.nameNick, players.highSchool, players.birthCountry, players.lastName, players.useFirst, players.pos, players.collegeOther, players.deathDate, players.birthDate, players.nameSuffix, players.firstseason, awards_players.note, players.middleName).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all_parser = reqparse.RequestParser()
get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all', methods=['GET'])
class get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all_resource(Resource):
    
    @players_awards_players_namespace.expect(get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all_parser)
    def get(self):
        args = get_awards_players_players_groupedby_birthCity_playerID_firstName_birthCountry_middleName_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(players, players.firstName, players.birthCountry, players.playerID, players.birthCity, players.middleName)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.group_by(players.birthCountry, players.birthCity, players.playerID, players.middleName, players.firstName)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_awards_players_namespace.route('/get_players_awards_players_groupedby_all', methods=['GET'])
class get_players_awards_players_groupedby_all_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, awards_players, func.count().label('count_all'))\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(players.hsState, awards_players.year, awards_players.award, players.nameGiven, players.weight, awards_players.playerID, players.height, players.lastseason, awards_players.lgID, players.birthState, players.hsCountry, players.race, awards_players.pos, players.hsCity, players.birthCity, players.playerID, players.fullGivenName, players.college, players.firstName, players.nameNick, players.highSchool, players.birthCountry, players.lastName, players.useFirst, players.pos, players.collegeOther, players.deathDate, players.birthDate, players.nameSuffix, players.firstseason, awards_players.note, players.middleName).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_players_players_filteredby_year_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_year', methods=['GET'])
class get_awards_players_players_filteredby_year_resource(Resource):
    
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_year_parser)
    def get(self):
        args = get_awards_players_players_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.firstName, players.playerID)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.filter(awards_players.year == args['awards_players.year']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_awards_players_namespace.route('/get_players_awards_players_groupedby_playerID', methods=['GET'])
class get_players_awards_players_groupedby_playerID_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, players.firstName, players.middleName)\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(awards_players.playerID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_awards_players_groupedby_playerID_lgID_orderedby_all_parser = reqparse.RequestParser()
get_players_awards_players_groupedby_playerID_lgID_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_groupedby_playerID_lgID_orderedby_all', methods=['GET'])
class get_players_awards_players_groupedby_playerID_lgID_orderedby_all_resource(Resource):
    
    @players_awards_players_namespace.expect(get_players_awards_players_groupedby_playerID_lgID_orderedby_all_parser)
    def get(self):
        args = get_players_awards_players_groupedby_playerID_lgID_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(players, players.playerID, awards_players, awards_players.lgID)\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(players.playerID, awards_players.lgID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID_parser.add_argument('players.middleName', type=str, required=True, location='args')
get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID_parser.add_argument('players.firstName', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID', methods=['GET'])
class get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID_resource(Resource):
    
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID_parser)
    def get(self):
        args = get_awards_players_players_filteredby_firstName_middleName_groupedby_playerID_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID, func.count().label('count_all'))\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.filter(players.middleName == args['players.middleName'], players.firstName == args['players.firstName'])\
				.group_by(players.playerID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all_parser = reqparse.RequestParser()
get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all', methods=['GET'])
class get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all_resource(Resource):
    
    @players_awards_players_namespace.expect(get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all_parser)
    def get(self):
        args = get_players_awards_players_groupedby_hsCity_playerID_year_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(players, players.hsCity, awards_players, awards_players.year)\
				.join(awards_players, players.playerID == awards_players.playerID)\
				.group_by(players.playerID, players.hsCity, awards_players.year)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_awards_players_players_filteredby_height_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_height_parser.add_argument('players.height', type=float, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_height', methods=['GET'])
class get_awards_players_players_filteredby_height_resource(Resource):
    
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_height_parser)
    def get(self):
        args = get_awards_players_players_filteredby_height_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.playerID)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.filter(players.height == args['players.height']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

