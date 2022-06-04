from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , awards_coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_awards_coaches_namespace = Namespace("players_awards_coaches", description="players_awards_coaches Api") 
get_players_awards_coaches_groupedby_id_model = players_awards_coaches_namespace.model('get_players_awards_coaches_groupedby_id_model',{ 'players.firstName' : fields.String,'players.middleName' : fields.String,'awards_coaches.id' : fields.String,'count_all' : fields.Integer })
get_players_awards_coaches_groupedby_id_parser = reqparse.RequestParser()
get_players_awards_coaches_groupedby_id_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_coaches_namespace.route('/get_players_awards_coaches_groupedby_id', methods=['GET'])
class get_players_awards_coaches_groupedby_id_resource(Resource):
    @players_awards_coaches_namespace.marshal_list_with(get_players_awards_coaches_groupedby_id_model)
    @players_awards_coaches_namespace.expect(get_players_awards_coaches_groupedby_id_parser)

    def get(self):
        args = get_players_awards_coaches_groupedby_id_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(players.firstName, players.middleName, awards_coaches.id, func.count().label('count_all'))\
			.join(players)\
			.join(awards_coaches)\
			.group_by(awards_coaches.id, players.middleName, players.firstName)\
			.order_by(direction(func.count()))
        return results

get_players_awards_coaches_filteredby_id_model = players_awards_coaches_namespace.model('get_players_awards_coaches_filteredby_id_model',{ 'players.firstName' : fields.String,'players.middleName' : fields.String,'count_all' : fields.Integer })
get_players_awards_coaches_filteredby_id_parser = reqparse.RequestParser()
get_players_awards_coaches_filteredby_id_parser.add_argument('awards_coaches.id', type=str, required=True, location='args')

@players_awards_coaches_namespace.route('/get_players_awards_coaches_filteredby_id', methods=['GET'])
class get_players_awards_coaches_filteredby_id_resource(Resource):
    @players_awards_coaches_namespace.marshal_list_with(get_players_awards_coaches_filteredby_id_model)
    @players_awards_coaches_namespace.expect(get_players_awards_coaches_filteredby_id_parser)

    def get(self):
        args = get_players_awards_coaches_filteredby_id_parser.parse_args()

        results = db.session.query(players.firstName, players.middleName, func.count().label('count_all'))\
			.join(players)\
			.join(awards_coaches)\
			.filter(awards_coaches.id <= args['awards_coaches.id'])\
			.group_by(players.middleName, players.firstName)
        return results

get_awards_coaches_coaches_players_model = players_awards_coaches_namespace.model('get_awards_coaches_coaches_players_model',{ 'awards_coaches.id' : fields.String,'awards_coaches.coachID' : fields.DateTime,'awards_coaches.award' : fields.String,'awards_coaches.lgID' : fields.String,'awards_coaches.note' : fields.String,'coaches.coachID' : fields.String,'coaches.year' : fields.Integer,'coaches.tmID' : fields.String,'coaches.lgID' : fields.String,'coaches.stint' : fields.Integer,'coaches.won' : fields.Integer,'coaches.lost' : fields.Integer,'coaches.post_wins' : fields.Integer,'coaches.post_losses' : fields.Integer,'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.Strin })

@players_awards_coaches_namespace.route('/get_awards_coaches_coaches_players', methods=['GET'])
class get_awards_coaches_coaches_players_resource(Resource):
    @players_awards_coaches_namespace.marshal_list_with(get_awards_coaches_coaches_players_model)
    
    def get(self):
        
        results = db.session.query(awards_coaches, coaches, players)\
			.join(awards_coaches, awards_coaches.coachID == coaches.coachID)
        return results

get_awards_coaches_coaches_players_filteredby_year_model = players_awards_coaches_namespace.model('get_awards_coaches_coaches_players_filteredby_year_model',{ 'players.playerID' : fields.String,'coaches.coachID' : fields.String })
get_awards_coaches_coaches_players_filteredby_year_parser = reqparse.RequestParser()
get_awards_coaches_coaches_players_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@players_awards_coaches_namespace.route('/get_awards_coaches_coaches_players_filteredby_year', methods=['GET'])
class get_awards_coaches_coaches_players_filteredby_year_resource(Resource):
    @players_awards_coaches_namespace.marshal_list_with(get_awards_coaches_coaches_players_filteredby_year_model)
    @players_awards_coaches_namespace.expect(get_awards_coaches_coaches_players_filteredby_year_parser)

    def get(self):
        args = get_awards_coaches_coaches_players_filteredby_year_parser.parse_args()

        results = db.session.query(players.playerID, coaches.coachID)\
			.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
			.filter(coaches.year < args['coaches.year'])
        return results

get_awards_coaches_coaches_players_filteredby_coachID_model = players_awards_coaches_namespace.model('get_awards_coaches_coaches_players_filteredby_coachID_model',{ 'players.playerID' : fields.String,'coaches.coachID' : fields.String })
get_awards_coaches_coaches_players_filteredby_coachID_parser = reqparse.RequestParser()
get_awards_coaches_coaches_players_filteredby_coachID_parser.add_argument('coaches.coachID', type=str, required=True, location='args')

@players_awards_coaches_namespace.route('/get_awards_coaches_coaches_players_filteredby_coachID', methods=['GET'])
class get_awards_coaches_coaches_players_filteredby_coachID_resource(Resource):
    @players_awards_coaches_namespace.marshal_list_with(get_awards_coaches_coaches_players_filteredby_coachID_model)
    @players_awards_coaches_namespace.expect(get_awards_coaches_coaches_players_filteredby_coachID_parser)

    def get(self):
        args = get_awards_coaches_coaches_players_filteredby_coachID_parser.parse_args()

        results = db.session.query(players.playerID, coaches.coachID)\
			.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
			.filter(coaches.coachID == args['coaches.coachID'])
        return results

