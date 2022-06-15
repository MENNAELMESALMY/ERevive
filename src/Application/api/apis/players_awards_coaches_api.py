from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , awards_coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_awards_coaches_namespace = Namespace("players_awards_coaches", description="players_awards_coaches Api") 
get_players_awards_coaches_groupedby_id_model = players_awards_coaches_namespace.model('get_players_awards_coaches_groupedby_id_model',{ 'awards_coaches.id' : fields.String,'players.middleName' : fields.String,'players.firstName' : fields.String,'count_all' : fields.Integer })
get_players_awards_coaches_groupedby_id_parser = reqparse.RequestParser()
get_players_awards_coaches_groupedby_id_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_coaches_namespace.route('/get_players_awards_coaches_groupedby_id', methods=['GET'])
class get_players_awards_coaches_groupedby_id_resource(Resource):
    @players_awards_coaches_namespace.marshal_list_with(get_players_awards_coaches_groupedby_id_model)
    @players_awards_coaches_namespace.expect(get_players_awards_coaches_groupedby_id_parser)

    def get(self):
        args = get_players_awards_coaches_groupedby_id_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_coaches, awards_coaches.id, players, players.middleName, players.firstName, func.count().label('count_all'))\
				.group_by(players.firstName, awards_coaches.id, players.middleName)\
				.order_by(direction(func.count())).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_coaches_filteredby_id_model = players_awards_coaches_namespace.model('get_players_awards_coaches_filteredby_id_model',{ 'players.middleName' : fields.String,'players.firstName' : fields.String,'count_all' : fields.Integer })
get_players_awards_coaches_filteredby_id_parser = reqparse.RequestParser()
get_players_awards_coaches_filteredby_id_parser.add_argument('awards_coaches.id', type=str, required=True, location='args')

@players_awards_coaches_namespace.route('/get_players_awards_coaches_filteredby_id', methods=['GET'])
class get_players_awards_coaches_filteredby_id_resource(Resource):
    @players_awards_coaches_namespace.marshal_list_with(get_players_awards_coaches_filteredby_id_model)
    @players_awards_coaches_namespace.expect(get_players_awards_coaches_filteredby_id_parser)

    def get(self):
        args = get_players_awards_coaches_filteredby_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, players.middleName, players.firstName, func.count().label('count_all'), awards_coaches)\
				.filter(awards_coaches.id <= args['awards_coaches.id'])\
				.group_by(players.firstName, players.middleName).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_players_awards_coaches_model = players_awards_coaches_namespace.model('get_players_awards_coaches_model',{ 'players.playerID' : fields.String,'players.useFirst' : fields.String,'players.firstName' : fields.String,'players.middleName' : fields.String,'players.lastName' : fields.String,'players.nameGiven' : fields.String,'players.fullGivenName' : fields.String,'players.nameSuffix' : fields.String,'players.nameNick' : fields.String,'players.pos' : fields.String,'players.firstseason' : fields.Integer,'players.lastseason' : fields.Integer,'players.height' : fields.Float,'players.weight' : fields.Integer,'players.college' : fields.String,'players.collegeOther' : fields.String,'players.birthDate' : fields.DateTime,'players.birthCity' : fields.String,'players.birthState' : fields.String,'players.birthCountry' : fields.String,'players.highSchool' : fields.String,'players.hsCity' : fields.String,'players.hsState' : fields.String,'players.hsCountry' : fields.String,'players.deathDate' : fields.DateTime,'players.race' : fields.String,'awards_coaches.id' : fields.String,'awards_coaches.coachID' : fields.String,'awards_coaches.award' : fields.String,'awards_coaches.lgID' : fields.String,'awards_coaches.note' : fields.String })

@players_awards_coaches_namespace.route('/get_players_awards_coaches', methods=['GET'])
class get_players_awards_coaches_resource(Resource):
    @players_awards_coaches_namespace.marshal_list_with(get_players_awards_coaches_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, awards_coaches).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

