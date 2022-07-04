from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Flight 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
flight_namespace = Namespace("Flight", description="Flight Api") 


flight_model =flight_namespace.model("flight",convert_db_model_to_restx_model(Flight)) 
flight_id_parser = reqparse.RequestParser() 
flight_id_parser.add_argument('IncrementalKey',type=int)


@flight_namespace.route("/")
class FlightApi(Resource):

    def get(self):
        try:
            flights = db.session.query(Flight).all()
            flights = [row.serialize() for row in flights]
            return flights , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @flight_namespace.expect(flight_model) 
    def post(self):
        try:
            flights = Flight(ArrivalDate = request.json.get("ArrivalDate"),Departureime = request.json.get("Departureime"),DepartureDate = request.json.get("DepartureDate"),to = request.json.get("to"),From = request.json.get("From"),FlightNumber = request.json.get("FlightNumber"),IncrementalKey = request.json.get("IncrementalKey"),Airplane_Flies_IncrementalKey = request.json.get("Airplane_Flies_IncrementalKey"))
            db.session.add(flights)
            db.session.commit()    
            return flights.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @flight_namespace.expect(flight_model) 
    def put(self):
        try:
            db.session.query(Flight).filter(Flight.IncrementalKey==request.json.get('IncrementalKey') ).update(request.json) 
            db.session.commit() 
            flights = db.session.query(Flight).filter(Flight.IncrementalKey==request.json.get('IncrementalKey') ).first() 
            return flights.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @flight_namespace.expect(flight_id_parser) 
    def delete(self):
        try:
            flights = db.session.query(Flight).filter(Flight.IncrementalKey==flight_id_parser.parse_args().get('IncrementalKey') ).first() 
            db.session.query(Flight).filter(Flight.IncrementalKey==flight_id_parser.parse_args().get('IncrementalKey') ).delete() 
            db.session.commit() 
            return flights.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

get_flight_filteredby_incrementalkey_groupedby_all_parser = reqparse.RequestParser()
get_flight_filteredby_incrementalkey_groupedby_all_parser.add_argument('Flight.IncrementalKey', type=int, required=True, location='args')

@flight_namespace.route('/get_flight_filteredby_incrementalkey_groupedby_all', methods=['GET'])
class get_flight_filteredby_incrementalkey_groupedby_all_resource(Resource):
    
    @flight_namespace.expect(get_flight_filteredby_incrementalkey_groupedby_all_parser)
    def get(self):
        args = get_flight_filteredby_incrementalkey_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(Flight, func.count().label('count_all'))\
				.filter(Flight.IncrementalKey == args['Flight.IncrementalKey'])\
				.group_by(Flight.FlightNumber, Flight.From, Flight.Departureime, Flight.Airplane_Flies_IncrementalKey, Flight.IncrementalKey, Flight.to, Flight.ArrivalDate, Flight.DepartureDate).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@flight_namespace.route('/get_flight_groupedby_all', methods=['GET'])
class get_flight_groupedby_all_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Flight, func.max(Flight.FlightNumber).label('max_Flight.FlightNumber'), func.min(Flight.DepartureDate).label('min_Flight.DepartureDate'), func.count().label('count_all'), func.min(Flight.ArrivalDate).label('min_Flight.ArrivalDate'), func.min(Flight.FlightNumber).label('min_Flight.FlightNumber'), func.max(Flight.DepartureDate).label('max_Flight.DepartureDate'), func.avg(Flight.FlightNumber).label('avg_Flight.FlightNumber'), func.max(Flight.IncrementalKey).label('max_Flight.IncrementalKey'), func.max(Flight.ArrivalDate).label('max_Flight.ArrivalDate'))\
				.group_by(Flight.FlightNumber, Flight.From, Flight.Departureime, Flight.Airplane_Flies_IncrementalKey, Flight.IncrementalKey, Flight.to, Flight.ArrivalDate, Flight.DepartureDate).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_flight_groupedby_all_orderedby_all_parser = reqparse.RequestParser()
get_flight_groupedby_all_orderedby_all_parser.add_argument('is_order_ofof_rows_desc', type=bool, required=True, location='args')

@flight_namespace.route('/get_flight_groupedby_all_orderedby_all', methods=['GET'])
class get_flight_groupedby_all_orderedby_all_resource(Resource):
    
    @flight_namespace.expect(get_flight_groupedby_all_orderedby_all_parser)
    def get(self):
        args = get_flight_groupedby_all_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Flight)\
				.group_by(Flight.FlightNumber, Flight.From, Flight.Departureime, Flight.Airplane_Flies_IncrementalKey, Flight.IncrementalKey, Flight.to, Flight.ArrivalDate, Flight.DepartureDate)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_flight_filteredby_airplane_flies_incrementalkey_arrivaldate_groupedby_arrivaldate_departuredate_flightnumber_parser = reqparse.RequestParser()
get_flight_filteredby_airplane_flies_incrementalkey_arrivaldate_groupedby_arrivaldate_departuredate_flightnumber_parser.add_argument('Flight.Airplane_Flies_IncrementalKey', type=int, required=True, location='args')
get_flight_filteredby_airplane_flies_incrementalkey_arrivaldate_groupedby_arrivaldate_departuredate_flightnumber_parser.add_argument('Flight.ArrivalDate', type=datetime, required=True, location='args')

@flight_namespace.route('/get_flight_filteredby_airplane_flies_incrementalkey_arrivaldate_groupedby_arrivaldate_departuredate_flightnumber', methods=['GET'])
class get_flight_filteredby_airplane_flies_incrementalkey_arrivaldate_groupedby_arrivaldate_departuredate_flightnumber_resource(Resource):
    
    @flight_namespace.expect(get_flight_filteredby_airplane_flies_incrementalkey_arrivaldate_groupedby_arrivaldate_departuredate_flightnumber_parser)
    def get(self):
        args = get_flight_filteredby_airplane_flies_incrementalkey_arrivaldate_groupedby_arrivaldate_departuredate_flightnumber_parser.parse_args()

        results = None
        try:
            results = db.session.query(Flight.FlightNumber.label('Flight.FlightNumber'), Flight.ArrivalDate.label('Flight.ArrivalDate'), Flight.DepartureDate.label('Flight.DepartureDate'), func.count().label('count_all'))\
				.filter(Flight.Airplane_Flies_IncrementalKey == args['Flight.Airplane_Flies_IncrementalKey'], Flight.ArrivalDate > args['Flight.ArrivalDate'])\
				.group_by(Flight.DepartureDate, Flight.ArrivalDate, Flight.FlightNumber).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_flight_filteredby_airplane_flies_incrementalkey_groupedby_airplane_flies_incrementalkey_incrementalkey_flightnumber_parser = reqparse.RequestParser()
get_flight_filteredby_airplane_flies_incrementalkey_groupedby_airplane_flies_incrementalkey_incrementalkey_flightnumber_parser.add_argument('Flight.Airplane_Flies_IncrementalKey', type=int, required=True, location='args')

@flight_namespace.route('/get_flight_filteredby_airplane_flies_incrementalkey_groupedby_airplane_flies_incrementalkey_incrementalkey_flightnumber', methods=['GET'])
class get_flight_filteredby_airplane_flies_incrementalkey_groupedby_airplane_flies_incrementalkey_incrementalkey_flightnumber_resource(Resource):
    
    @flight_namespace.expect(get_flight_filteredby_airplane_flies_incrementalkey_groupedby_airplane_flies_incrementalkey_incrementalkey_flightnumber_parser)
    def get(self):
        args = get_flight_filteredby_airplane_flies_incrementalkey_groupedby_airplane_flies_incrementalkey_incrementalkey_flightnumber_parser.parse_args()

        results = None
        try:
            results = db.session.query(Flight.FlightNumber.label('Flight.FlightNumber'), Flight.IncrementalKey.label('Flight.IncrementalKey'), Flight.Airplane_Flies_IncrementalKey.label('Flight.Airplane_Flies_IncrementalKey'), func.count().label('count_all'))\
				.filter(Flight.Airplane_Flies_IncrementalKey == args['Flight.Airplane_Flies_IncrementalKey'])\
				.group_by(Flight.IncrementalKey, Flight.FlightNumber, Flight.Airplane_Flies_IncrementalKey).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_flight_groupedby_airplane_flies_incrementalkey_orderedby_all_parser = reqparse.RequestParser()
get_flight_groupedby_airplane_flies_incrementalkey_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@flight_namespace.route('/get_flight_groupedby_airplane_flies_incrementalkey_orderedby_all', methods=['GET'])
class get_flight_groupedby_airplane_flies_incrementalkey_orderedby_all_resource(Resource):
    
    @flight_namespace.expect(get_flight_groupedby_airplane_flies_incrementalkey_orderedby_all_parser)
    def get(self):
        args = get_flight_groupedby_airplane_flies_incrementalkey_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Flight.Airplane_Flies_IncrementalKey.label('Flight.Airplane_Flies_IncrementalKey'))\
				.group_by(Flight.Airplane_Flies_IncrementalKey)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_flight_groupedby_incrementalkey_orderedby_all_parser = reqparse.RequestParser()
get_flight_groupedby_incrementalkey_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@flight_namespace.route('/get_flight_groupedby_incrementalkey_orderedby_all', methods=['GET'])
class get_flight_groupedby_incrementalkey_orderedby_all_resource(Resource):
    
    @flight_namespace.expect(get_flight_groupedby_incrementalkey_orderedby_all_parser)
    def get(self):
        args = get_flight_groupedby_incrementalkey_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Flight.IncrementalKey.label('Flight.IncrementalKey'), func.count().label('count_all'))\
				.group_by(Flight.IncrementalKey)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_flight_orderedby_all_parser = reqparse.RequestParser()
get_flight_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@flight_namespace.route('/get_flight_orderedby_all', methods=['GET'])
class get_flight_orderedby_all_resource(Resource):
    
    @flight_namespace.expect(get_flight_orderedby_all_parser)
    def get(self):
        args = get_flight_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(func.count().label('count_all'))\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

