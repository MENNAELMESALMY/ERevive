from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Airplane 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
airplane_namespace = Namespace("Airplane", description="Airplane Api") 


airplane_model =airplane_namespace.model("airplane",convert_db_model_to_restx_model(Airplane)) 
airplane_id_parser = reqparse.RequestParser() 
airplane_id_parser.add_argument('IncrementalKey',type=int)


@airplane_namespace.route("/")
class AirplaneApi(Resource):

    def get(self):
        try:
            airplanes = db.session.query(Airplane).all()
            airplanes = [row.serialize() for row in airplanes]
            return airplanes , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @airplane_namespace.expect(airplane_model) 
    def post(self):
        try:
            airplanes = Airplane(RegistrationNumnber = request.json.get("RegistrationNumnber"),MadelNumber = request.json.get("MadelNumber"),Capacity = request.json.get("Capacity"),IncrementalKey = request.json.get("IncrementalKey"))
            db.session.add(airplanes)
            db.session.commit()    
            return airplanes.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @airplane_namespace.expect(airplane_model) 
    def put(self):
        try:
            db.session.query(Airplane).filter(Airplane.IncrementalKey==request.json.get('IncrementalKey') ).update(request.json) 
            db.session.commit() 
            airplanes = db.session.query(Airplane).filter(Airplane.IncrementalKey==request.json.get('IncrementalKey') ).first() 
            return airplanes.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @airplane_namespace.expect(airplane_id_parser) 
    def delete(self):
        try:
            airplanes = db.session.query(Airplane).filter(Airplane.IncrementalKey==airplane_id_parser.parse_args().get('IncrementalKey') ).first() 
            db.session.query(Airplane).filter(Airplane.IncrementalKey==airplane_id_parser.parse_args().get('IncrementalKey') ).delete() 
            db.session.commit() 
            return airplanes.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

