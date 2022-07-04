from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Program 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
program_namespace = Namespace("Program", description="Program Api") 


program_model =program_namespace.model("program",convert_db_model_to_restx_model(Program)) 
program_id_parser = reqparse.RequestParser() 
program_id_parser.add_argument('program_id',type=int)


@program_namespace.route("/")
class ProgramApi(Resource):

    def get(self):
        try:
            programs = db.session.query(Program).all()
            programs = [row.serialize() for row in programs]
            return programs , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @program_namespace.expect(program_model) 
    def post(self):
        try:
            programs = Program(YearCommenced = request.json.get("YearCommenced"),program_id = request.json.get("program_id"),Name = request.json.get("Name"),CreditPoints = request.json.get("CreditPoints"))
            db.session.add(programs)
            db.session.commit()    
            return programs.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @program_namespace.expect(program_model) 
    def put(self):
        try:
            db.session.query(Program).filter(Program.program_id==request.json.get('program_id') ).update(request.json) 
            db.session.commit() 
            programs = db.session.query(Program).filter(Program.program_id==request.json.get('program_id') ).first() 
            return programs.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @program_namespace.expect(program_id_parser) 
    def delete(self):
        try:
            programs = db.session.query(Program).filter(Program.program_id==program_id_parser.parse_args().get('program_id') ).first() 
            db.session.query(Program).filter(Program.program_id==program_id_parser.parse_args().get('program_id') ).delete() 
            db.session.commit() 
            return programs.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400


@program_namespace.route('/get_program_groupedby_all', methods=['GET'])
class get_program_groupedby_all_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Program, func.max(Program.program_id).label('max_Program.program_id'), func.count().label('count_all'), func.min(Program.program_id).label('min_Program.program_id'))\
				.group_by(Program.program_id, Program.YearCommenced, Program.CreditPoints, Program.Name).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_groupedby_all_orderedby_name_parser = reqparse.RequestParser()
get_program_groupedby_all_orderedby_name_parser.add_argument('is_order_of_Name_desc', type=bool, required=True, location='args')

@program_namespace.route('/get_program_groupedby_all_orderedby_name', methods=['GET'])
class get_program_groupedby_all_orderedby_name_resource(Resource):
    
    @program_namespace.expect(get_program_groupedby_all_orderedby_name_parser)
    def get(self):
        args = get_program_groupedby_all_orderedby_name_parser.parse_args()
        Name_direction = desc if args['is_order_of_Name_desc'] else asc

        results = None
        try:
            results = db.session.query(Program, func.count().label('count_all'))\
				.group_by(Program.program_id, Program.YearCommenced, Program.CreditPoints, Program.Name)\
				.order_by(Name_direction(Program.Name)).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_filteredby_yearcommenced_name_groupedby_name_parser = reqparse.RequestParser()
get_program_filteredby_yearcommenced_name_groupedby_name_parser.add_argument('Program.Name', type=str, required=True, location='args')
get_program_filteredby_yearcommenced_name_groupedby_name_parser.add_argument('Program.YearCommenced', type=int, required=True, location='args')

@program_namespace.route('/get_program_filteredby_yearcommenced_name_groupedby_name', methods=['GET'])
class get_program_filteredby_yearcommenced_name_groupedby_name_resource(Resource):
    
    @program_namespace.expect(get_program_filteredby_yearcommenced_name_groupedby_name_parser)
    def get(self):
        args = get_program_filteredby_yearcommenced_name_groupedby_name_parser.parse_args()

        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'), func.count().label('count_all'))\
				.filter(Program.Name <= args['Program.Name'], Program.YearCommenced == args['Program.YearCommenced'])\
				.group_by(Program.Name).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

# get_program_filteredby_workload_parser = reqparse.RequestParser()
# get_program_filteredby_workload_parser.add_argument('p', type=r, required=True, location='args')

# @program_namespace.route('/get_program_filteredby_workload', methods=['GET'])
# class get_program_filteredby_workload_resource(Resource):
    
#     @program_namespace.expect(get_program_filteredby_workload_parser)
#     def get(self):
#         args = get_program_filteredby_workload_parser.parse_args()

#         results = None
#         try:
#             results = db.session.query(Program.Name.label('Program.Name'))\
# 				.filter(p < args['p']).all()

#             results = serialize(results)
#             return results , 200
#         except Exception as e:
#             print(e)
#             return str(e) , 400


@program_namespace.route('/get_program_groupedby_name_program_id', methods=['GET'])
class get_program_groupedby_name_program_id_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'), Program.program_id.label('Program.program_id'), func.count().label('count_all'))\
				.group_by(Program.program_id, Program.Name).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_groupedby_name_program_id_orderedby_name_parser = reqparse.RequestParser()
get_program_groupedby_name_program_id_orderedby_name_parser.add_argument('is_order_of_Name_desc', type=bool, required=True, location='args')

@program_namespace.route('/get_program_groupedby_name_program_id_orderedby_name', methods=['GET'])
class get_program_groupedby_name_program_id_orderedby_name_resource(Resource):
    
    @program_namespace.expect(get_program_groupedby_name_program_id_orderedby_name_parser)
    def get(self):
        args = get_program_groupedby_name_program_id_orderedby_name_parser.parse_args()
        Name_direction = desc if args['is_order_of_Name_desc'] else asc

        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'), Program.program_id.label('Program.program_id'), func.count().label('count_all'))\
				.group_by(Program.program_id, Program.Name)\
				.order_by(Name_direction(Program.Name)).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_groupedby_name_program_id_orderedby_all_parser = reqparse.RequestParser()
get_program_groupedby_name_program_id_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@program_namespace.route('/get_program_groupedby_name_program_id_orderedby_all', methods=['GET'])
class get_program_groupedby_name_program_id_orderedby_all_resource(Resource):
    
    @program_namespace.expect(get_program_groupedby_name_program_id_orderedby_all_parser)
    def get(self):
        args = get_program_groupedby_name_program_id_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'), Program.program_id.label('Program.program_id'))\
				.group_by(Program.program_id, Program.Name)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_groupedby_name_program_id_orderedby_name_parser = reqparse.RequestParser()
get_program_groupedby_name_program_id_orderedby_name_parser.add_argument('is_order_of_Name_desc', type=bool, required=True, location='args')

@program_namespace.route('/get_program_groupedby_name_program_id_orderedby_name', methods=['GET'])
class get_program_groupedby_name_program_id_orderedby_name_resource(Resource):
    
    @program_namespace.expect(get_program_groupedby_name_program_id_orderedby_name_parser)
    def get(self):
        args = get_program_groupedby_name_program_id_orderedby_name_parser.parse_args()
        Name_direction = desc if args['is_order_of_Name_desc'] else asc

        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'), Program.program_id.label('Program.program_id'))\
				.group_by(Program.program_id, Program.Name)\
				.order_by(Name_direction(Program.Name)).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_groupedby_name_orderedby_all_parser = reqparse.RequestParser()
get_program_groupedby_name_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@program_namespace.route('/get_program_groupedby_name_orderedby_all', methods=['GET'])
class get_program_groupedby_name_orderedby_all_resource(Resource):
    
    @program_namespace.expect(get_program_groupedby_name_orderedby_all_parser)
    def get(self):
        args = get_program_groupedby_name_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'), func.count().label('count_all'))\
				.group_by(Program.Name)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_groupedby_program_id_orderedby_all_parser = reqparse.RequestParser()
get_program_groupedby_program_id_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@program_namespace.route('/get_program_groupedby_program_id_orderedby_all', methods=['GET'])
class get_program_groupedby_program_id_orderedby_all_resource(Resource):
    
    @program_namespace.expect(get_program_groupedby_program_id_orderedby_all_parser)
    def get(self):
        args = get_program_groupedby_program_id_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Program.program_id.label('Program.program_id'))\
				.group_by(Program.program_id)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

