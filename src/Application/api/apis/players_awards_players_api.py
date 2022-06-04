from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , awards_players 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_awards_players_namespace = Namespace("players_awards_players", description="players_awards_players Api") 
get_players_awards_players_groupedby_playerID_model = players_awards_players_namespace.model('get_players_awards_players_groupedby_playerID_model',{ 'players.middleName' : fields.String,'players.birthCountry' : fields.String,'awards_players.lgID' : fields.String,'players.playerID' : fields.String,'players.firstName' : fields.String,'awards_players.year' : fields.Integer,'players.birthCity' : fields.String,'players.hsCity' : fields.String })
get_players_awards_players_groupedby_playerID_parser = reqparse.RequestParser()
get_players_awards_players_groupedby_playerID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_players_awards_players_groupedby_playerID', methods=['GET'])
class get_players_awards_players_groupedby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_players_awards_players_groupedby_playerID_model)
    @players_awards_players_namespace.expect(get_players_awards_players_groupedby_playerID_parser)

    def get(self):
        args = get_players_awards_players_groupedby_playerID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(players.middleName, players.birthCountry, awards_players.lgID, players.playerID, players.firstName, awards_players.year, players.birthCity, players.hsCity)\
			.join(players, players.playerID == awards_players.playerID)\
			.group_by(players.playerID)\
			.order_by(direction(func.count()))
        return results

get_awards_players_filteredby_year_model = players_awards_players_namespace.model('get_awards_players_filteredby_year_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'count_awards_players.year' : fields.Integer,'count_all' : fields.Integer })
get_awards_players_filteredby_year_parser = reqparse.RequestParser()
get_awards_players_filteredby_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_filteredby_year', methods=['GET'])
class get_awards_players_filteredby_year_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_filteredby_year_model)
    @players_awards_players_namespace.expect(get_awards_players_filteredby_year_parser)

    def get(self):
        args = get_awards_players_filteredby_year_parser.parse_args()

        results = db.session.query(awards_players, func.count(awards_players.year).label('count_awards_players.year'), func.count().label('count_all'))\
			.filter(awards_players.year == args['awards_players.year'])
        return results

get_awards_players_filteredby_playerID_model = players_awards_players_namespace.model('get_awards_players_filteredby_playerID_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'count_all' : fields.Integer })
get_awards_players_filteredby_playerID_parser = reqparse.RequestParser()
get_awards_players_filteredby_playerID_parser.add_argument('awards_players.playerID', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_filteredby_playerID', methods=['GET'])
class get_awards_players_filteredby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_filteredby_playerID_model)
    @players_awards_players_namespace.expect(get_awards_players_filteredby_playerID_parser)

    def get(self):
        args = get_awards_players_filteredby_playerID_parser.parse_args()

        results = db.session.query(awards_players, func.count().label('count_all'))\
			.filter(awards_players.playerID == args['awards_players.playerID'])
        return results

get_awards_players_model = players_awards_players_namespace.model('get_awards_players_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'count_all' : fields.Integer,'count_awards_players.year' : fields.Integer,'count_awards_players.playerID' : fields.String,'count_players.playerID' : fields.String,'avg_player_allstar.minutes' : fields.String,'sum_player_allstar.minutes' : fields.String })

@players_awards_players_namespace.route('/get_awards_players', methods=['GET'])
class get_awards_players_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_model)
    
    def get(self):
        
        results = db.session.query(awards_players, func.count().label('count_all'), func.count(awards_players.year).label('count_awards_players.year'), func.count(awards_players.playerID).label('count_awards_players.playerID'), func.count(players.playerID).label('count_players.playerID'), func.avg(player_allstar.minutes).label('avg_player_allstar.minutes'), func.sum(player_allstar.minutes).label('sum_player_allstar.minutes'))
        return results

get_awards_players_players_groupedby_playerID_model = players_awards_players_namespace.model('get_awards_players_players_groupedby_playerID_model',{ 'players.height' : fields.Float,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.playerID' : fields.String,'count_all' : fields.Integer,'avg_players.height' : fields.Float })
get_awards_players_players_groupedby_playerID_parser = reqparse.RequestParser()
get_awards_players_players_groupedby_playerID_parser.add_argument('having_value', type=int, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_groupedby_playerID', methods=['GET'])
class get_awards_players_players_groupedby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_players_groupedby_playerID_model)
    @players_awards_players_namespace.expect(get_awards_players_players_groupedby_playerID_parser)

    def get(self):
        args = get_awards_players_players_groupedby_playerID_parser.parse_args()

        results = db.session.query(players.height, players.firstName, players.middleName, players.playerID, func.count().label('count_all'), func.avg(players.height).label('avg_players.height'))\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.group_by(players.middleName, players.height, players.playerID, players.firstName)\
			.having(func.count() > args['having_value'])
        return results

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

        results = db.session.query(players.playerID, awards_players.playerID)\
			.join(players, players.playerID == awards_players.playerID)\
			.order_by(height_direction(players.height))
        return results

get_awards_players_players_filteredby_middleName_firstName_model = players_awards_players_namespace.model('get_awards_players_players_filteredby_middleName_firstName_model',{ 'players.playerID' : fields.String,'count_all' : fields.Integer })
get_awards_players_players_filteredby_middleName_firstName_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_middleName_firstName_parser.add_argument('players.middleName', type=str, required=True, location='args')
get_awards_players_players_filteredby_middleName_firstName_parser.add_argument('players.firstName', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_middleName_firstName', methods=['GET'])
class get_awards_players_players_filteredby_middleName_firstName_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_players_filteredby_middleName_firstName_model)
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_middleName_firstName_parser)

    def get(self):
        args = get_awards_players_players_filteredby_middleName_firstName_parser.parse_args()

        results = db.session.query(players.playerID, func.count().label('count_all'))\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.filter(players.middleName == args['players.middleName'], players.firstName == args['players.firstName'])\
			.group_by(players.playerID)
        return results

get_awards_players_filteredby_playerID_year_model = players_awards_players_namespace.model('get_awards_players_filteredby_playerID_year_model',{ 'awards_players.year' : fields.Integer })
get_awards_players_filteredby_playerID_year_parser = reqparse.RequestParser()
get_awards_players_filteredby_playerID_year_parser.add_argument('awards_players.playerID', type=str, required=True, location='args')
get_awards_players_filteredby_playerID_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_filteredby_playerID_year', methods=['GET'])
class get_awards_players_filteredby_playerID_year_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_filteredby_playerID_year_model)
    @players_awards_players_namespace.expect(get_awards_players_filteredby_playerID_year_parser)

    def get(self):
        args = get_awards_players_filteredby_playerID_year_parser.parse_args()

        results = db.session.query(awards_players.year)\
			.filter(awards_players.playerID == args['awards_players.playerID'], awards_players.year == args['awards_players.year'])
        return results

get_awards_players_players_filteredby_middleName_firstName_lastName_model = players_awards_players_namespace.model('get_awards_players_players_filteredby_middleName_firstName_lastName_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.Strin })
get_awards_players_players_filteredby_middleName_firstName_lastName_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_middleName_firstName_lastName_parser.add_argument('players.middleName', type=str, required=True, location='args')
get_awards_players_players_filteredby_middleName_firstName_lastName_parser.add_argument('players.firstName', type=str, required=True, location='args')
get_awards_players_players_filteredby_middleName_firstName_lastName_parser.add_argument('players.lastName', type=str, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_middleName_firstName_lastName', methods=['GET'])
class get_awards_players_players_filteredby_middleName_firstName_lastName_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_players_filteredby_middleName_firstName_lastName_model)
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_middleName_firstName_lastName_parser)

    def get(self):
        args = get_awards_players_players_filteredby_middleName_firstName_lastName_parser.parse_args()

        results = db.session.query(awards_players, players)\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.filter(players.middleName == args['players.middleName'], players.firstName == args['players.firstName'], players.lastName == args['players.lastName'])
        return results

get_awards_players_groupedby_playerID_model = players_awards_players_namespace.model('get_awards_players_groupedby_playerID_model',{ 'awards_players.playerID' : fields.String,'count_all' : fields.Integer })
get_awards_players_groupedby_playerID_parser = reqparse.RequestParser()
get_awards_players_groupedby_playerID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_groupedby_playerID', methods=['GET'])
class get_awards_players_groupedby_playerID_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_groupedby_playerID_model)
    @players_awards_players_namespace.expect(get_awards_players_groupedby_playerID_parser)

    def get(self):
        args = get_awards_players_groupedby_playerID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(awards_players.playerID, func.count().label('count_all'))\
			.group_by(awards_players.playerID)\
			.order_by(direction(func.count()))
        return results

get_awards_players_players_filteredby_playerID_birthDate_model = players_awards_players_namespace.model('get_awards_players_players_filteredby_playerID_birthDate_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.Strin })
get_awards_players_players_filteredby_playerID_birthDate_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_playerID_birthDate_parser.add_argument('awards_players.playerID', type=str, required=True, location='args')
get_awards_players_players_filteredby_playerID_birthDate_parser.add_argument('players.birthDate', type=datetime, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_playerID_birthDate', methods=['GET'])
class get_awards_players_players_filteredby_playerID_birthDate_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_players_filteredby_playerID_birthDate_model)
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_playerID_birthDate_parser)

    def get(self):
        args = get_awards_players_players_filteredby_playerID_birthDate_parser.parse_args()

        results = db.session.query(awards_players, players)\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.filter(awards_players.playerID == args['awards_players.playerID'], players.birthDate < args['players.birthDate'])
        return results

get_awards_players_players_filteredby_weight_model = players_awards_players_namespace.model('get_awards_players_players_filteredby_weight_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.Strin })
get_awards_players_players_filteredby_weight_parser = reqparse.RequestParser()
get_awards_players_players_filteredby_weight_parser.add_argument('players.weight', type=int, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players_players_filteredby_weight', methods=['GET'])
class get_awards_players_players_filteredby_weight_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_players_filteredby_weight_model)
    @players_awards_players_namespace.expect(get_awards_players_players_filteredby_weight_parser)

    def get(self):
        args = get_awards_players_players_filteredby_weight_parser.parse_args()

        results = db.session.query(awards_players, players)\
			.join(awards_players, awards_players.playerID == players.playerID)\
			.filter(players.weight == args['players.weight'])
        return results

get_awards_players_model = players_awards_players_namespace.model('get_awards_players_model',{ 'count_all' : fields.Integer })
get_awards_players_parser = reqparse.RequestParser()
get_awards_players_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_players_namespace.route('/get_awards_players', methods=['GET'])
class get_awards_players_resource(Resource):
    @players_awards_players_namespace.marshal_list_with(get_awards_players_model)
    @players_awards_players_namespace.expect(get_awards_players_parser)

    def get(self):
        args = get_awards_players_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(func.count().label('count_all'))\
			.order_by(direction(func.count()))
        return results

