from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Boaking 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
boaking_namespace = Namespace("Boaking", description="Boaking Api") 


boaking_model =boaking_namespace.model("boaking",convert_db_model_to_restx_model(Boaking)) 
boaking_id_parser = reqparse.RequestParser() 
boaking_id_parser.add_argument('IncrementalKey',type=int)


@boaking_namespace.route("/")
class BoakingApi(Resource):

    def get(self):
        try:
            boakings = db.session.query(Boaking).all()
            boakings = [row.serialize() for row in boakings]
            return boakings , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @boaking_namespace.expect(boaking_model) 
    def post(self):
        try:
            boakings = Boaking(IncrementalKey = request.json.get("IncrementalKey"),Flight_HasBooking_IncrementalKey = request.json.get("Flight_HasBooking_IncrementalKey"),Passenger_Books_EmailAddress. = request.json.get("Passenger_Books_EmailAddress."))
            db.session.add(boakings)
            db.session.commit()    
            return boakings.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @boaking_namespace.expect(boaking_model) 
    def put(self):
        try:
            db.session.query(Boaking).filter(Boaking.IncrementalKey==request.json.get('IncrementalKey') ).update(request.json) 
            db.session.commit() 
            boakings = db.session.query(Boaking).filter(Boaking.IncrementalKey==request.json.get('IncrementalKey') ).first() 
            return boakings.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @boaking_namespace.expect(boaking_id_parser) 
    def delete(self):
        try:
            boakings = db.session.query(Boaking).filter(Boaking.IncrementalKey==boaking_id_parser.parse_args().get('IncrementalKey') ).first() 
            db.session.query(Boaking).filter(Boaking.IncrementalKey==boaking_id_parser.parse_args().get('IncrementalKey') ).delete() 
            db.session.commit() 
            return boakings.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

