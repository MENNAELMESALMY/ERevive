from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Student , Attempts_course_Student 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
student_attempts_course_student_namespace = Namespace("student_attempts_course_student", description="student_attempts_course_student Api") 
get_student_attempts_course_student_filteredby_givennames_parser = reqparse.RequestParser()
get_student_attempts_course_student_filteredby_givennames_parser.add_argument('Student.GivenNames', type=str, required=True, location='args')

@student_attempts_course_student_namespace.route('/get_student_attempts_course_student_filteredby_givennames', methods=['GET'])
class get_student_attempts_course_student_filteredby_givennames_resource(Resource):
    
    @student_attempts_course_student_namespace.expect(get_student_attempts_course_student_filteredby_givennames_parser)
    def get(self):
        args = get_student_attempts_course_student_filteredby_givennames_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student.YearEnralled.label('Student.YearEnralled'), Attempts_course_Student.Student_Student_ID.label('Attempts_course_Student.Student_Student_ID'))\
				.join(Attempts_course_Student, Student.Student_ID == Attempts_course_Student.Student_Student_ID)\
				.filter(Student.GivenNames == args['Student.GivenNames']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@student_attempts_course_student_namespace.route('/get_student_attempts_course_student_groupedby_givennames_student_id', methods=['GET'])
class get_student_attempts_course_student_groupedby_givennames_student_id_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), Student.Student_ID.label('Student.Student_ID'), func.count().label('count_all'))\
				.join(Attempts_course_Student, Student.Student_ID == Attempts_course_Student.Student_Student_ID)\
				.group_by(Student.GivenNames, Student.Student_ID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_attempts_course_student_groupedby_student_id_yearenralled_orderedby_all_parser = reqparse.RequestParser()
get_student_attempts_course_student_groupedby_student_id_yearenralled_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_attempts_course_student_namespace.route('/get_student_attempts_course_student_groupedby_student_id_yearenralled_orderedby_all', methods=['GET'])
class get_student_attempts_course_student_groupedby_student_id_yearenralled_orderedby_all_resource(Resource):
    
    @student_attempts_course_student_namespace.expect(get_student_attempts_course_student_groupedby_student_id_yearenralled_orderedby_all_parser)
    def get(self):
        args = get_student_attempts_course_student_groupedby_student_id_yearenralled_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Student.YearEnralled.label('Student.YearEnralled'))\
				.join(Attempts_course_Student, Student.Student_ID == Attempts_course_Student.Student_Student_ID)\
				.group_by(Student.YearEnralled, Student.Student_ID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@student_attempts_course_student_namespace.route('/get_student_attempts_course_student_groupedby_student_id', methods=['GET'])
class get_student_attempts_course_student_groupedby_student_id_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Student.Student_ID.label('Student.Student_ID'), func.count(Student.Student_ID).label('count_Student.Student_ID'))\
				.join(Attempts_course_Student, Student.Student_ID == Attempts_course_Student.Student_Student_ID)\
				.group_by(Student.Student_ID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@student_attempts_course_student_namespace.route('/get_student_attempts_course_student_groupedby_givennames_student_student_id', methods=['GET'])
class get_student_attempts_course_student_groupedby_givennames_student_student_id_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), func.count().label('count_all'))\
				.join(Attempts_course_Student, Student.Student_ID == Attempts_course_Student.Student_Student_ID)\
				.group_by(Student.GivenNames, Attempts_course_Student.Student_Student_ID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_givennames_parser = reqparse.RequestParser()
get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_givennames_parser.add_argument('is_order_of_GivenNames_desc', type=bool, required=True, location='args')

@student_attempts_course_student_namespace.route('/get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_givennames', methods=['GET'])
class get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_givennames_resource(Resource):
    
    @student_attempts_course_student_namespace.expect(get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_givennames_parser)
    def get(self):
        args = get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_givennames_parser.parse_args()
        GivenNames_direction = desc if args['is_order_of_GivenNames_desc'] else asc

        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), func.count().label('count_all'))\
				.join(Attempts_course_Student, Student.Student_ID == Attempts_course_Student.Student_Student_ID)\
				.group_by(Student.GivenNames, Attempts_course_Student.Student_Student_ID)\
				.order_by(GivenNames_direction(Student.GivenNames)).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_all_parser = reqparse.RequestParser()
get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_attempts_course_student_namespace.route('/get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_all', methods=['GET'])
class get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_all_resource(Resource):
    
    @student_attempts_course_student_namespace.expect(get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_all_parser)
    def get(self):
        args = get_student_attempts_course_student_groupedby_givennames_student_student_id_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), func.count().label('count_all'))\
				.join(Attempts_course_Student, Student.Student_ID == Attempts_course_Student.Student_Student_ID)\
				.group_by(Student.GivenNames, Attempts_course_Student.Student_Student_ID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

