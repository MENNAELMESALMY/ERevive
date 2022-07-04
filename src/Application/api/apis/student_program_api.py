from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Student , Program 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
student_program_namespace = Namespace("student_program", description="student_program Api") 
get_student_program_filteredby_name_groupedby_givennames_student_id_parser = reqparse.RequestParser()
get_student_program_filteredby_name_groupedby_givennames_student_id_parser.add_argument('Program.Name', type=str, required=True, location='args')

@student_program_namespace.route('/get_student_program_filteredby_name_groupedby_givennames_student_id', methods=['GET'])
class get_student_program_filteredby_name_groupedby_givennames_student_id_resource(Resource):
    
    @student_program_namespace.expect(get_student_program_filteredby_name_groupedby_givennames_student_id_parser)
    def get(self):
        args = get_student_program_filteredby_name_groupedby_givennames_student_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), Student.Student_ID.label('Student.Student_ID'), func.count().label('count_all'))\
				.join(Program, Student.Program_Envollsin_program_id == Program.program_id)\
				.filter(Program.Name == args['Program.Name'])\
				.group_by(Student.GivenNames, Student.Student_ID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_program_filteredby_student_id_parser = reqparse.RequestParser()
get_student_program_filteredby_student_id_parser.add_argument('Student.Student_ID', type=int, required=True, location='args')

@student_program_namespace.route('/get_student_program_filteredby_student_id', methods=['GET'])
class get_student_program_filteredby_student_id_resource(Resource):
    
    @student_program_namespace.expect(get_student_program_filteredby_student_id_parser)
    def get(self):
        args = get_student_program_filteredby_student_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), Program.Name.label('Program.Name'))\
				.join(Program, Student.Program_Envollsin_program_id == Program.program_id)\
				.filter(Student.Student_ID == args['Student.Student_ID']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@student_program_namespace.route('/get_student_program', methods=['GET'])
class get_student_program_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), Program.Name.label('Program.Name'), Program.program_id.label('Program.program_id'))\
				.join(Program, Student.Program_Envollsin_program_id == Program.program_id).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_program_filteredby_program_id_groupedby_yearenralled_program_id_parser = reqparse.RequestParser()
get_student_program_filteredby_program_id_groupedby_yearenralled_program_id_parser.add_argument('Program.program_id', type=int, required=True, location='args')

@student_program_namespace.route('/get_student_program_filteredby_program_id_groupedby_yearenralled_program_id', methods=['GET'])
class get_student_program_filteredby_program_id_groupedby_yearenralled_program_id_resource(Resource):
    
    @student_program_namespace.expect(get_student_program_filteredby_program_id_groupedby_yearenralled_program_id_parser)
    def get(self):
        args = get_student_program_filteredby_program_id_groupedby_yearenralled_program_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student.YearEnralled.label('Student.YearEnralled'), Program.program_id.label('Program.program_id'), func.count(Student.Student_ID).label('count_Student.Student_ID'))\
				.join(Program, Student.Program_Envollsin_program_id == Program.program_id)\
				.filter(Program.program_id == args['Program.program_id'])\
				.group_by(Program.program_id, Student.YearEnralled).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@student_program_namespace.route('/get_student_program_groupedby_name_program_id', methods=['GET'])
class get_student_program_groupedby_name_program_id_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'), Program.program_id.label('Program.program_id'))\
				.join(Student, Student.Program_Envollsin_program_id == Program.program_id)\
				.group_by(Program.program_id, Program.Name).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_student_groupedby_name_program_id_orderedby_all_parser = reqparse.RequestParser()
get_program_student_groupedby_name_program_id_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_program_namespace.route('/get_program_student_groupedby_name_program_id_orderedby_all', methods=['GET'])
class get_program_student_groupedby_name_program_id_orderedby_all_resource(Resource):
    
    @student_program_namespace.expect(get_program_student_groupedby_name_program_id_orderedby_all_parser)
    def get(self):
        args = get_program_student_groupedby_name_program_id_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'), Program.program_id.label('Program.program_id'))\
				.join(Student, Program.program_id == Student.Program_Envollsin_program_id)\
				.group_by(Program.program_id, Program.Name)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_student_groupedby_name_orderedby_all_parser = reqparse.RequestParser()
get_program_student_groupedby_name_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_program_namespace.route('/get_program_student_groupedby_name_orderedby_all', methods=['GET'])
class get_program_student_groupedby_name_orderedby_all_resource(Resource):
    
    @student_program_namespace.expect(get_program_student_groupedby_name_orderedby_all_parser)
    def get(self):
        args = get_program_student_groupedby_name_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Program.Name.label('Program.Name'))\
				.join(Student, Program.program_id == Student.Program_Envollsin_program_id)\
				.group_by(Program.Name)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_program_filteredby_givennames_name_parser = reqparse.RequestParser()
get_student_program_filteredby_givennames_name_parser.add_argument('Program.Name', type=str, required=True, location='args')
get_student_program_filteredby_givennames_name_parser.add_argument('Student.GivenNames', type=str, required=True, location='args')

@student_program_namespace.route('/get_student_program_filteredby_givennames_name', methods=['GET'])
class get_student_program_filteredby_givennames_name_resource(Resource):
    
    @student_program_namespace.expect(get_student_program_filteredby_givennames_name_parser)
    def get(self):
        args = get_student_program_filteredby_givennames_name_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student, Program)\
				.join(Program, Student.Program_Envollsin_program_id == Program.program_id)\
				.filter(Program.Name == args['Program.Name'], Student.GivenNames.like(args['Student.GivenNames'])).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_program_student_groupedby_program_id_orderedby_all_parser = reqparse.RequestParser()
get_program_student_groupedby_program_id_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_program_namespace.route('/get_program_student_groupedby_program_id_orderedby_all', methods=['GET'])
class get_program_student_groupedby_program_id_orderedby_all_resource(Resource):
    
    @student_program_namespace.expect(get_program_student_groupedby_program_id_orderedby_all_parser)
    def get(self):
        args = get_program_student_groupedby_program_id_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Program.program_id.label('Program.program_id'))\
				.join(Student, Program.program_id == Student.Program_Envollsin_program_id)\
				.group_by(Program.program_id)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

