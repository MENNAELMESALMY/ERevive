from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import coaches 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
coaches_namespace = Namespace("coaches", description="coaches Api") 


coaches_model =coaches_namespace.model("coaches",convert_db_model_to_restx_model(coaches)) 
coaches_id_parser = reqparse.RequestParser() 
coaches_id_parser.add_argument('coachID',type=str)
coaches_id_parser.add_argument('year',type=int)
coaches_id_parser.add_argument('tmID',type=str)
coaches_id_parser.add_argument('stint',type=int)


@coaches_namespace.route("/")
class coachesApi(Resource):

    def get(self):
        try:
            coachess = db.session.query(coaches).all()
            coachess = [row.serialize() for row in coachess]
            return coachess , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @coaches_namespace.expect(coaches_model) 
    def post(self):
        try:
            coachess = coaches(coachID = request.json.get("coachID"),year = request.json.get("year"),tmID = request.json.get("tmID"),lgID = request.json.get("lgID"),stint = request.json.get("stint"),won = request.json.get("won"),lost = request.json.get("lost"),post_wins = request.json.get("post_wins"),post_losses = request.json.get("post_losses"))
            db.session.add(coachess)
            db.session.commit()    
            return coachess.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @coaches_namespace.expect(coaches_model) 
    def put(self):
        try:
            db.session.query(coaches).filter(coaches.coachID==request.json.get('coachID') and coaches.year==request.json.get('year') and coaches.tmID==request.json.get('tmID') and coaches.stint==request.json.get('stint') ).update(request.json) 
            db.session.commit() 
            coachess = db.session.query(coaches).filter(coaches.coachID==request.json.get('coachID') and coaches.year==request.json.get('year') and coaches.tmID==request.json.get('tmID') and coaches.stint==request.json.get('stint') ).first() 
            return coachess.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @coaches_namespace.expect(coaches_id_parser) 
    def delete(self):
        try:
            coachess = db.session.query(coaches).filter(coaches.coachID==coaches_id_parser.parse_args().get('coachID') and coaches.year==coaches_id_parser.parse_args().get('year') and coaches.tmID==coaches_id_parser.parse_args().get('tmID') and coaches.stint==coaches_id_parser.parse_args().get('stint') ).first() 
            db.session.query(coaches).filter(coaches.coachID==coaches_id_parser.parse_args().get('coachID') and coaches.year==coaches_id_parser.parse_args().get('year') and coaches.tmID==coaches_id_parser.parse_args().get('tmID') and coaches.stint==coaches_id_parser.parse_args().get('stint') ).delete() 
            db.session.commit() 
            return coachess.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

get_coaches_filteredby_coachID_groupedby_all_parser = reqparse.RequestParser()
get_coaches_filteredby_coachID_groupedby_all_parser.add_argument('coaches.coachID', type=str, required=True, location='args')

@coaches_namespace.route('/get_coaches_filteredby_coachID_groupedby_all', methods=['GET'])
class get_coaches_filteredby_coachID_groupedby_all_resource(Resource):
    
    @coaches_namespace.expect(get_coaches_filteredby_coachID_groupedby_all_parser)
    def get(self):
        args = get_coaches_filteredby_coachID_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID.label('coaches.coachID'), func.count().label('count_all'))\
				.filter(coaches.coachID <= args['coaches.coachID'])\
				.group_by(coaches.stint, coaches.year, coaches.won, coaches.post_wins, coaches.lgID, coaches.lost, coaches.post_losses, coaches.tmID, coaches.coachID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@coaches_namespace.route('/get_coaches_groupedby_all', methods=['GET'])
class get_coaches_groupedby_all_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(coaches, coaches.coachID.label('coaches.coachID'), func.count().label('count_all'))\
				.group_by(coaches.stint, coaches.year, coaches.won, coaches.post_wins, coaches.lgID, coaches.lost, coaches.post_losses, coaches.tmID, coaches.coachID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_coaches_filteredby_year_groupedby_coachID_year_parser = reqparse.RequestParser()
get_coaches_filteredby_year_groupedby_coachID_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@coaches_namespace.route('/get_coaches_filteredby_year_groupedby_coachID_year', methods=['GET'])
class get_coaches_filteredby_year_groupedby_coachID_year_resource(Resource):
    
    @coaches_namespace.expect(get_coaches_filteredby_year_groupedby_coachID_year_parser)
    def get(self):
        args = get_coaches_filteredby_year_groupedby_coachID_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, coaches.year, func.count().label('count_all'))\
				.filter(coaches.year >= args['coaches.year'])\
				.group_by(coaches.year, coaches.coachID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_coaches_groupedby_tmID_coachID_orderedby_all_parser = reqparse.RequestParser()
get_coaches_groupedby_tmID_coachID_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_namespace.route('/get_coaches_groupedby_tmID_coachID_orderedby_all', methods=['GET'])
class get_coaches_groupedby_tmID_coachID_orderedby_all_resource(Resource):
    
    @coaches_namespace.expect(get_coaches_groupedby_tmID_coachID_orderedby_all_parser)
    def get(self):
        args = get_coaches_groupedby_tmID_coachID_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(coaches, coaches.tmID, coaches.coachID)\
				.group_by(coaches.tmID, coaches.coachID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_coaches_groupedby_coachID_orderedby_all_parser = reqparse.RequestParser()
get_coaches_groupedby_coachID_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_namespace.route('/get_coaches_groupedby_coachID_orderedby_all', methods=['GET'])
class get_coaches_groupedby_coachID_orderedby_all_resource(Resource):
    
    @coaches_namespace.expect(get_coaches_groupedby_coachID_orderedby_all_parser)
    def get(self):
        args = get_coaches_groupedby_coachID_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID, func.count().label('count_all'))\
				.group_by(coaches.coachID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_coaches_groupedby_year_orderedby_all_parser = reqparse.RequestParser()
get_coaches_groupedby_year_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_namespace.route('/get_coaches_groupedby_year_orderedby_all', methods=['GET'])
class get_coaches_groupedby_year_orderedby_all_resource(Resource):
    
    @coaches_namespace.expect(get_coaches_groupedby_year_orderedby_all_parser)
    def get(self):
        args = get_coaches_groupedby_year_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(coaches, coaches.year)\
				.group_by(coaches.year)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_coaches_filteredby_year_parser = reqparse.RequestParser()
get_coaches_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')
get_coaches_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@coaches_namespace.route('/get_coaches_filteredby_year', methods=['GET'])
class get_coaches_filteredby_year_resource(Resource):
    
    @coaches_namespace.expect(get_coaches_filteredby_year_parser)
    def get(self):
        args = get_coaches_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(coaches, coaches.coachID.label('coaches.coachID'))\
				.filter(coaches.year == args['coaches.year']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_coaches_orderedby_all_parser = reqparse.RequestParser()
get_coaches_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_namespace.route('/get_coaches_orderedby_all', methods=['GET'])
class get_coaches_orderedby_all_resource(Resource):
    
    @coaches_namespace.expect(get_coaches_orderedby_all_parser)
    def get(self):
        args = get_coaches_orderedby_all_parser.parse_args()
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

