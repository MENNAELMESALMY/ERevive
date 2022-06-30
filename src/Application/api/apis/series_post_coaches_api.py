from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import series_post , coaches 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
series_post_coaches_namespace = Namespace("series_post_coaches", description="series_post_coaches Api") 

@series_post_coaches_namespace.route('/get_series_post_coaches', methods=['GET'])
class get_series_post_coaches_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, series_post).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

