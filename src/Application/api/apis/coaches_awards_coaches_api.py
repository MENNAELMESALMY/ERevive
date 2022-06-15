from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import coaches , awards_coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
coaches_awards_coaches_namespace = Namespace("coaches_awards_coaches", description="coaches_awards_coaches Api") 
get_coaches_awards_coaches_filteredby_year_model = coaches_awards_coaches_namespace.model('get_coaches_awards_coaches_filteredby_year_model',{ 'coaches.coachID' : fields.String })
get_coaches_awards_coaches_filteredby_year_parser = reqparse.RequestParser()
get_coaches_awards_coaches_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@coaches_awards_coaches_namespace.route('/get_coaches_awards_coaches_filteredby_year', methods=['GET'])
class get_coaches_awards_coaches_filteredby_year_resource(Resource):
    @coaches_awards_coaches_namespace.marshal_list_with(get_coaches_awards_coaches_filteredby_year_model)
    @coaches_awards_coaches_namespace.expect(get_coaches_awards_coaches_filteredby_year_parser)

    def get(self):
        args = get_coaches_awards_coaches_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID)\
				.join(awards_coaches, coaches.coachID == awards_coaches.coachID)\
				.filter(coaches.year == args['coaches.year']).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

get_coaches_awards_coaches_model = coaches_awards_coaches_namespace.model('get_coaches_awards_coaches_model',{ 'coaches.coachID' : fields.String,'coaches.year' : fields.Integer,'coaches.tmID' : fields.String,'coaches.lgID' : fields.String,'coaches.stint' : fields.Integer,'coaches.won' : fields.Integer,'coaches.lost' : fields.Integer,'coaches.post_wins' : fields.Integer,'coaches.post_losses' : fields.Integer,'awards_coaches.id' : fields.String,'awards_coaches.coachID' : fields.String,'awards_coaches.award' : fields.String,'awards_coaches.lgID' : fields.String,'awards_coaches.note' : fields.String })

@coaches_awards_coaches_namespace.route('/get_coaches_awards_coaches', methods=['GET'])
class get_coaches_awards_coaches_resource(Resource):
    @coaches_awards_coaches_namespace.marshal_list_with(get_coaches_awards_coaches_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(coaches, awards_coaches)\
				.join(awards_coaches, coaches.coachID == awards_coaches.coachID).all()

        except Exception as e:
            print(e)
            return None , 400

        return results , 200

