from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , awards_players 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_awards_players_namespace = Namespace("players_awards_players", description="players_awards_players Api") 
get_players_awards_players_groupedby_playerID_model = players_awards_players_namespace.model('get_players_awards_players_groupedby_playerID_model',{ 'players.firstName' : fields.String,'players.birthCountry' : fields.String,'players.middleName' : fields.String,'players.birthCity' : fields.String,'awards_players.year' : fields.Integer,'players.playerID' : fields.String,'players.hsCity' : fields.String })
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
            results = db.session.query(players.firstName, players.birthCountry, players.middleName, players.birthCity, awards_players.year, players.playerID, players.hsCity)\
				.join(players, players.playerID == awards_players.playerID)\
				.group_by(players.playerID)\
				.order_by(direction(func.count())).all()

        except Exception as e:
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
				.join(players, players.playerID == awards_players.playerID)\
				.filter(awards_players.playerID.like(args['awards_players.playerID']))\
				.group_by(players.hsCity, players.height, awards_players.lgID, players.lastseason, players.weight, players.race, players.nameGiven, players.useFirst, players.collegeOther, awards_players.award, awards_players.playerID, players.college, players.birthCountry, awards_players.pos, awards_players.year, players.hsCountry, players.birthState, players.nameNick, players.hsState, players.firstseason, players.deathDate, players.nameSuffix, players.lastName, players.playerID, players.fullGivenName, players.highSchool, players.birthCity, awards_players.note, players.firstName, players.birthDate, players.pos, players.middleName).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_player_allstar_model = players_awards_players_namespace.model('get_awards_players_player_allstar_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'player_allstar.playerID' : fields.String,'player_allstar.last_name' : fields.DateTime,'player_allstar.first_name' : fields.String,'player_allstar.season_id' : fields.String,'player_allstar.conference' : fields.String,'player_allstar.league_id' : fields.String,'player_allstar.games_played' : fields.String,'player_allstar.minutes' : fields.String,'player_allstar.points' : fields.String,'player_allstar.o_rebounds' : fields.String,'player_allstar.d_rebounds' : fields.String,'player_allstar.rebounds' : fields.String,'player_allstar.assists' : fields.String,'player_allstar.steals' : fields.String,'player_allstar.blocks' : fields.String,'player_allstar.turnovers' : fields.String,'player_allstar.personal_fouls' : fields.String,'player_allstar.fg_attempted' : fields.String,'player_allstar.fg_made' : fields.String,'player_allstar.ft_attempted' : fields.String,'player_allstar.ft_made' : fields.String,'player_allstar.three_attempted' : fields.String,'player_allstar.three_made' : fields.String,'avg_player_allstar.minutes' : fields.String,'sum_player_allstar.minutes' : fields.String,'count_players.playerID' : fields.String,'count_all' : fields.Integer })
get_awards_players_player_allstar_parser = reqparse.RequestParser()
get_awards_players_player_allstar_parser.add_argument('player_allstar.minutes', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_player_allstar', methods=['GET'])
class get_awards_players_player_allstar_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_player_allstar_model)
    @players_awards_players_namespace.expect(get_awards_players_player_allstar_parser)

    def get(self):
        args = get_awards_players_player_allstar_parser.parse_args()

        results = None
        try:
            results = db.session.query(awards_players, player_allstar, func.avg(player_allstar.minutes).label('avg_player_allstar.minutes'), func.sum(player_allstar.minutes).label('sum_player_allstar.minutes'), func.count(players.playerID).label('count_players.playerID'), func.count().label('count_all'))\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.join(players, players.playerID == player_allstar.playerID)\
				.group_by(player_allstar.ft_attempted, awards_players.lgID, awards_players.year, player_allstar.season_id, player_allstar.minutes, player_allstar.playerID, player_allstar.conference, player_allstar.last_name, player_allstar.turnovers, player_allstar.blocks, player_allstar.points, player_allstar.fg_attempted, player_allstar.three_made, awards_players.note, player_allstar.ft_made, player_allstar.fg_made, player_allstar.first_name, player_allstar.three_attempted, player_allstar.league_id, awards_players.award, player_allstar.steals, awards_players.playerID, player_allstar.personal_fouls, player_allstar.games_played, player_allstar.assists, player_allstar.d_rebounds, player_allstar.o_rebounds, player_allstar.rebounds, awards_players.pos)\
				.having(func.sum(player_allstar.minutes) >= args['player_allstar.minutes']).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_players_groupedby_playerID_model = players_awards_players_namespace.model('get_awards_players_players_groupedby_playerID_model',{ 'players.firstName' : fields.String,'players.middleName' : fields.String,'players.playerID' : fields.String,'players.height' : fields.Float,'avg_players.height' : fields.Float,'count_all' : fields.Integer })
get_awards_players_players_groupedby_playerID_parser = reqparse.RequestParser()
get_awards_players_players_groupedby_playerID_parser.add_argument('having_value', type=int, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_groupedby_playerID', methods=['GET'])
class get_awards_players_players_groupedby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_players_groupedby_playerID_model)
    @players_awards_players_namespace.expect(get_awards_players_players_groupedby_playerID_parser)

    def get(self):
        args = get_awards_players_players_groupedby_playerID_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.firstName, players.middleName, players.playerID, players.height, func.avg(players.height).label('avg_players.height'), func.count().label('count_all'))\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.group_by(players.height, players.middleName, players.firstName, players.playerID)\
				.having(func.count() > args['having_value']).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_players_filteredby_year_model = players_awards_players_namespace.model('get_awards_players_players_filteredby_year_model',{ 'players.firstName' : fields.String,'awards_players.playerID' : fields.String })
get_awards_players_players_filteredby_year_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_year', methods=['GET'])
class get_awards_players_players_filteredby_year_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_players_filteredby_year_model)
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_year_parser)

    def get(self):
        args = get_awards_players_players_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.firstName, awards_players.playerID)\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.filter(awards_players.year == args['awards_players.year']).all()

        except Exception as e:
            return None , 400

        return results , 200

get_players_awards_players_orderedby_height_model = players_awards_players_namespace.model('get_players_awards_players_orderedby_height_model',{ 'players.playerID' : fields.String,'awards_players.playerID' : fields.String })
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
            results = db.session.query(players.playerID, awards_players.playerID)\
				.join(players, players.playerID == awards_players.playerID)\
				.order_by(height_direction(players.height)).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_players_filteredby_middleName_firstName_model = players_awards_players_namespace.model('get_awards_players_players_filteredby_middleName_firstName_model',{ 'players.playerID' : fields.String,'count_all' : fields.Integer })
get_awards_players_players_filteredby_middleName_firstName_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_middleName_firstName_parser.add_argument('players.firstName', type=str, required=True, location='args')
get_awards_players_players_filteredby_middleName_firstName_parser.add_argument('players.middleName', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_middleName_firstName', methods=['GET'])
class get_awards_players_players_filteredby_middleName_firstName_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_players_filteredby_middleName_firstName_model)
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_middleName_firstName_parser)

    def get(self):
        args = get_awards_players_players_filteredby_middleName_firstName_parser.parse_args()

        results = None
        try:
            results = db.session.query(players.playerID, func.count().label('count_all'))\
				.join(awards_players, awards_players.playerID == players.playerID)\
				.filter(players.firstName == args['players.firstName'], players.middleName == args['players.middleName'])\
				.group_by(players.playerID).all()

        except Exception as e:
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
            results = db.session.query(awards_players.playerID)\
				.join(players, players.playerID == awards_players.playerID)\
				.order_by(direction(func.count())).all()

        except Exception as e:
            return None , 400

        return results , 200

