from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players , awards_coaches 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
players_awards_coaches_namespace = Namespace("players_awards_coaches", description="players_awards_coaches Api") 
get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all_parser = reqparse.RequestParser()
get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@players_awards_coaches_namespace.route('/get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all', methods=['GET'])
class get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all_resource(Resource):
    
    @players_awards_coaches_namespace.expect(get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all_parser)
    def get(self):
        args = get_players_awards_coaches_groupedby_id_firstName_middleName_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(players, players.firstName, awards_coaches, awards_coaches.id, players.middleName, func.count().label('count_all'))\
				.group_by(players.firstName, players.middleName, awards_coaches.id)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_awards_coaches_namespace.route('/get_players_awards_coaches', methods=['GET'])
class get_players_awards_coaches_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, awards_coaches).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_players_awards_coaches_filteredby_id_parser = reqparse.RequestParser()
get_players_awards_coaches_filteredby_id_parser.add_argument('awards_coaches.id', type=str, required=True, location='args')

@players_awards_coaches_namespace.route('/get_players_awards_coaches_filteredby_id', methods=['GET'])
class get_players_awards_coaches_filteredby_id_resource(Resource):
    
    @players_awards_coaches_namespace.expect(get_players_awards_coaches_filteredby_id_parser)
    def get(self):
        args = get_players_awards_coaches_filteredby_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(players, awards_coaches)\
				.filter(awards_coaches.id <= args['awards_coaches.id']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@players_awards_coaches_namespace.route('/get_players_awards_coaches_groupedby_id_firstName_middleName', methods=['GET'])
class get_players_awards_coaches_groupedby_id_firstName_middleName_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(players, players.firstName, players.middleName, func.count().label('count_all'), awards_coaches)\
				.group_by(players.firstName, players.middleName, awards_coaches.id).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

