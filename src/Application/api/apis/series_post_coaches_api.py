from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import series_post , coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
series_post_coaches_namespace = Namespace("series_post_coaches", description="series_post_coaches Api") 
get_series_post_coaches_model = series_post_coaches_namespace.model('get_series_post_coaches_model',{ 'coaches.coachID' : fields.String })

@series_post_coaches_namespace.route('/get_series_post_coaches', methods=['GET'])
class get_series_post_coaches_resource(Resource):
    @series_post_coaches_namespace.marshal_list_with(get_series_post_coaches_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(coaches.coachID)\
				.join(series_post)\
				.join(coaches).all()

        except Exception as e:
            return None , 400

        return results , 200

