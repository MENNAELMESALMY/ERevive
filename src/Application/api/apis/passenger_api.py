from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Passenger 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
passenger_namespace = Namespace("Passenger", description="Passenger Api") 


passenger_model =passenger_namespace.model("passenger",convert_db_model_to_restx_model(Passenger)) 
passenger_id_parser = reqparse.RequestParser() 
passenger_id_parser.add_argument('EmailAddress.',type=str)


@passenger_namespace.route("/")
class PassengerApi(Resource):

    def get(self):
        try:
            passengers = db.session.query(Passenger).all()
            passengers = [row.serialize() for row in passengers]
            return passengers , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @passenger_namespace.expect(passenger_model) 
    def post(self):
        try:
            passengers = Passenger(‘Surname = request.json.get("‘Surname"),GivenNames = request.json.get("GivenNames"),EmailAddress. = request.json.get("EmailAddress."))
            db.session.add(passengers)
            db.session.commit()    
            return passengers.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @passenger_namespace.expect(passenger_model) 
    def put(self):
        try:
            db.session.query(Passenger).filter(Passenger.EmailAddress.==request.json.get('EmailAddress.') ).update(request.json) 
            db.session.commit() 
            passengers = db.session.query(Passenger).filter(Passenger.EmailAddress.==request.json.get('EmailAddress.') ).first() 
            return passengers.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @passenger_namespace.expect(passenger_id_parser) 
    def delete(self):
        try:
            passengers = db.session.query(Passenger).filter(Passenger.EmailAddress.==passenger_id_parser.parse_args().get('EmailAddress.') ).first() 
            db.session.query(Passenger).filter(Passenger.EmailAddress.==passenger_id_parser.parse_args().get('EmailAddress.') ).delete() 
            db.session.commit() 
            return passengers.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

get_passenger_filteredby_givennames_parser = reqparse.RequestParser()
get_passenger_filteredby_givennames_parser.add_argument('Passenger.GivenNames', type=str, required=True, location='args')

@passenger_namespace.route('/get_passenger_filteredby_givennames', methods=['GET'])
class get_passenger_filteredby_givennames_resource(Resource):
    
    @passenger_namespace.expect(get_passenger_filteredby_givennames_parser)
    def get(self):
        args = get_passenger_filteredby_givennames_parser.parse_args()

        results = None
        try:
            results = db.session.query(Passenger)\
				.filter(Passenger.GivenNames.like(args['Passenger.GivenNames'])).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@passenger_namespace.route('/get_passenger_groupedby_all', methods=['GET'])
class get_passenger_groupedby_all_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Passenger, func.count().label('count_all'))\
				.group_by(Passenger.‘Surname, Passenger.EmailAddress., Passenger.GivenNames).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

