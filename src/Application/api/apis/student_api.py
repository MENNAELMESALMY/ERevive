from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Student 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
student_namespace = Namespace("Student", description="Student Api") 


student_model =student_namespace.model("student",convert_db_model_to_restx_model(Student)) 
student_id_parser = reqparse.RequestParser() 
student_id_parser.add_argument('Student_ID',type=int)


@student_namespace.route("/")
class StudentApi(Resource):

    def get(self):
        try:
            students = db.session.query(Student).all()
            students = [row.serialize() for row in students]
            return students , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @student_namespace.expect(student_model) 
    def post(self):
        try:
            students = Student(YearEnralled = request.json.get("YearEnralled"),Student_ID = request.json.get("Student_ID"),GivenNames = request.json.get("GivenNames"),Program_Envollsin_program_id = request.json.get("Program_Envollsin_program_id"),Sumame = request.json.get("Sumame"))
            db.session.add(students)
            db.session.commit()    
            return students.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @student_namespace.expect(student_model) 
    def put(self):
        try:
            db.session.query(Student).filter(Student.Student_ID==request.json.get('Student_ID') ).update(request.json) 
            db.session.commit() 
            students = db.session.query(Student).filter(Student.Student_ID==request.json.get('Student_ID') ).first() 
            return students.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @student_namespace.expect(student_id_parser) 
    def delete(self):
        try:
            students = db.session.query(Student).filter(Student.Student_ID==student_id_parser.parse_args().get('Student_ID') ).first() 
            db.session.query(Student).filter(Student.Student_ID==student_id_parser.parse_args().get('Student_ID') ).delete() 
            db.session.commit() 
            return students.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_filteredby_student_id_yearenralled_groupedby_all_parser = reqparse.RequestParser()
get_student_filteredby_student_id_yearenralled_groupedby_all_parser.add_argument('Student.Student_ID', type=int, required=True, location='args')
get_student_filteredby_student_id_yearenralled_groupedby_all_parser.add_argument('Student.YearEnralled', type=int, required=True, location='args')

@student_namespace.route('/get_student_filteredby_student_id_yearenralled_groupedby_all', methods=['GET'])
class get_student_filteredby_student_id_yearenralled_groupedby_all_resource(Resource):
    
    @student_namespace.expect(get_student_filteredby_student_id_yearenralled_groupedby_all_parser)
    def get(self):
        args = get_student_filteredby_student_id_yearenralled_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student, func.avg(Student.YearEnralled).label('avg_Student.YearEnralled'), func.max(Student.YearEnralled).label('max_Student.YearEnralled'), func.count().label('count_all'))\
				.filter(Student.Student_ID > args['Student.Student_ID'], Student.YearEnralled == args['Student.YearEnralled'])\
				.group_by(Student.GivenNames, Student.YearEnralled, Student.Student_ID, Student.Program_Envollsin_program_id, Student.Sumame).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_filteredby_student_id_groupedby_all_parser = reqparse.RequestParser()
get_student_filteredby_student_id_groupedby_all_parser.add_argument('Student.Student_ID', type=int, required=True, location='args')

@student_namespace.route('/get_student_filteredby_student_id_groupedby_all', methods=['GET'])
class get_student_filteredby_student_id_groupedby_all_resource(Resource):
    
    @student_namespace.expect(get_student_filteredby_student_id_groupedby_all_parser)
    def get(self):
        args = get_student_filteredby_student_id_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student, func.count().label('count_all'), func.avg(Student.YearEnralled).label('avg_Student.YearEnralled'), func.max(Student.YearEnralled).label('max_Student.YearEnralled'))\
				.filter(Student.Student_ID == args['Student.Student_ID'])\
				.group_by(Student.GivenNames, Student.YearEnralled, Student.Student_ID, Student.Program_Envollsin_program_id, Student.Sumame).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_filteredby_yearenralled_groupedby_all_parser = reqparse.RequestParser()
get_student_filteredby_yearenralled_groupedby_all_parser.add_argument('Student.YearEnralled', type=int, required=True, location='args')

@student_namespace.route('/get_student_filteredby_yearenralled_groupedby_all', methods=['GET'])
class get_student_filteredby_yearenralled_groupedby_all_resource(Resource):
    
    @student_namespace.expect(get_student_filteredby_yearenralled_groupedby_all_parser)
    def get(self):
        args = get_student_filteredby_yearenralled_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student, func.avg(Student.Student_ID).label('avg_Student.Student_ID'), func.count().label('count_all'), func.avg(Student.YearEnralled).label('avg_Student.YearEnralled'), func.min(Student.YearEnralled).label('min_Student.YearEnralled'), func.max(Student.Student_ID).label('max_Student.Student_ID'), func.max(Student.YearEnralled).label('max_Student.YearEnralled'), func.min(Student.Student_ID).label('min_Student.Student_ID'))\
				.filter(Student.YearEnralled < args['Student.YearEnralled'])\
				.group_by(Student.GivenNames, Student.YearEnralled, Student.Student_ID, Student.Program_Envollsin_program_id, Student.Sumame).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@student_namespace.route('/get_student_groupedby_all', methods=['GET'])
class get_student_groupedby_all_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Student, func.avg(Student.Student_ID).label('avg_Student.Student_ID'), func.count().label('count_all'), func.avg(Student.YearEnralled).label('avg_Student.YearEnralled'), func.min(Student.YearEnralled).label('min_Student.YearEnralled'), func.max(Student.Student_ID).label('max_Student.Student_ID'), func.max(Student.YearEnralled).label('max_Student.YearEnralled'), func.min(Student.Student_ID).label('min_Student.Student_ID'))\
				.group_by(Student.GivenNames, Student.YearEnralled, Student.Student_ID, Student.Program_Envollsin_program_id, Student.Sumame).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_groupedby_all_orderedby_yearenralled_parser = reqparse.RequestParser()
get_student_groupedby_all_orderedby_yearenralled_parser.add_argument('is_order_of_count_YearEnralled_desc', type=bool, required=True, location='args')

@student_namespace.route('/get_student_groupedby_all_orderedby_yearenralled', methods=['GET'])
class get_student_groupedby_all_orderedby_yearenralled_resource(Resource):
    
    @student_namespace.expect(get_student_groupedby_all_orderedby_yearenralled_parser)
    def get(self):
        args = get_student_groupedby_all_orderedby_yearenralled_parser.parse_args()
        YearEnralled_direction = desc if args['is_order_of_count_YearEnralled_desc'] else asc

        results = None
        try:
            results = db.session.query(Student, func.avg(Student.YearEnralled).label('avg_Student.YearEnralled'), func.count().label('count_all'))\
				.group_by(Student.GivenNames, Student.YearEnralled, Student.Student_ID, Student.Program_Envollsin_program_id, Student.Sumame)\
				.order_by(YearEnralled_direction(func.count(Student.YearEnralled))).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_groupedby_all_orderedby_all_parser = reqparse.RequestParser()
get_student_groupedby_all_orderedby_all_parser.add_argument('is_order_ofof_rows_desc', type=bool, required=True, location='args')

@student_namespace.route('/get_student_groupedby_all_orderedby_all', methods=['GET'])
class get_student_groupedby_all_orderedby_all_resource(Resource):
    
    @student_namespace.expect(get_student_groupedby_all_orderedby_all_parser)
    def get(self):
        args = get_student_groupedby_all_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Student)\
				.group_by(Student.GivenNames, Student.YearEnralled, Student.Student_ID, Student.Program_Envollsin_program_id, Student.Sumame)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_groupedby_givennames_student_id_yearenralled_orderedby_all_parser = reqparse.RequestParser()
get_student_groupedby_givennames_student_id_yearenralled_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_namespace.route('/get_student_groupedby_givennames_student_id_yearenralled_orderedby_all', methods=['GET'])
class get_student_groupedby_givennames_student_id_yearenralled_orderedby_all_resource(Resource):
    
    @student_namespace.expect(get_student_groupedby_givennames_student_id_yearenralled_orderedby_all_parser)
    def get(self):
        args = get_student_groupedby_givennames_student_id_yearenralled_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), Student.YearEnralled.label('Student.YearEnralled'), Student.Student_ID.label('Student.Student_ID'), func.count().label('count_all'))\
				.group_by(Student.GivenNames, Student.YearEnralled, Student.Student_ID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_groupedby_givennames_yearenralled_orderedby_all_parser = reqparse.RequestParser()
get_student_groupedby_givennames_yearenralled_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_namespace.route('/get_student_groupedby_givennames_yearenralled_orderedby_all', methods=['GET'])
class get_student_groupedby_givennames_yearenralled_orderedby_all_resource(Resource):
    
    @student_namespace.expect(get_student_groupedby_givennames_yearenralled_orderedby_all_parser)
    def get(self):
        args = get_student_groupedby_givennames_yearenralled_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Student.GivenNames.label('Student.GivenNames'), Student.YearEnralled.label('Student.YearEnralled'), func.count().label('count_all'))\
				.group_by(Student.GivenNames, Student.YearEnralled)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_filteredby_student_id_groupedby_student_id_parser = reqparse.RequestParser()
get_student_filteredby_student_id_groupedby_student_id_parser.add_argument('Student.Student_ID', type=int, required=True, location='args')
get_student_filteredby_student_id_groupedby_student_id_parser.add_argument('Student.Student_ID', type=int, required=True, location='args')

@student_namespace.route('/get_student_filteredby_student_id_groupedby_student_id', methods=['GET'])
class get_student_filteredby_student_id_groupedby_student_id_resource(Resource):
    
    @student_namespace.expect(get_student_filteredby_student_id_groupedby_student_id_parser)
    def get(self):
        args = get_student_filteredby_student_id_groupedby_student_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(Student.Student_ID.label('Student.Student_ID'), func.avg(Student.YearEnralled).label('avg_Student.YearEnralled'), func.max(Student.YearEnralled).label('max_Student.YearEnralled'))\
				.filter(Student.Student_ID == args['Student.Student_ID'])\
				.group_by(Student.Student_ID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_groupedby_student_id_orderedby_all_parser = reqparse.RequestParser()
get_student_groupedby_student_id_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_namespace.route('/get_student_groupedby_student_id_orderedby_all', methods=['GET'])
class get_student_groupedby_student_id_orderedby_all_resource(Resource):
    
    @student_namespace.expect(get_student_groupedby_student_id_orderedby_all_parser)
    def get(self):
        args = get_student_groupedby_student_id_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Student.Student_ID.label('Student.Student_ID'), func.count().label('count_all'))\
				.group_by(Student.Student_ID)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_groupedby_student_id_yearenralled_orderedby_yearenralled_parser = reqparse.RequestParser()
get_student_groupedby_student_id_yearenralled_orderedby_yearenralled_parser.add_argument('is_order_of_count_YearEnralled_desc', type=bool, required=True, location='args')

@student_namespace.route('/get_student_groupedby_student_id_yearenralled_orderedby_yearenralled', methods=['GET'])
class get_student_groupedby_student_id_yearenralled_orderedby_yearenralled_resource(Resource):
    
    @student_namespace.expect(get_student_groupedby_student_id_yearenralled_orderedby_yearenralled_parser)
    def get(self):
        args = get_student_groupedby_student_id_yearenralled_orderedby_yearenralled_parser.parse_args()
        YearEnralled_direction = desc if args['is_order_of_count_YearEnralled_desc'] else asc

        results = None
        try:
            results = db.session.query(Student.YearEnralled.label('Student.YearEnralled'), func.count().label('count_all'))\
				.group_by(Student.YearEnralled, Student.Student_ID)\
				.order_by(YearEnralled_direction(func.count(Student.YearEnralled))).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_filteredby_program_envollsin_program_id_parser = reqparse.RequestParser()
get_student_filteredby_program_envollsin_program_id_parser.add_argument('Student.Program_Envollsin_program_id', type=int, required=True, location='args')

@student_namespace.route('/get_student_filteredby_program_envollsin_program_id', methods=['GET'])
class get_student_filteredby_program_envollsin_program_id_resource(Resource):
    
    @student_namespace.expect(get_student_filteredby_program_envollsin_program_id_parser)
    def get(self):
        args = get_student_filteredby_program_envollsin_program_id_parser.parse_args()

        results = None
        try:
            results = db.session.query(func.count().label('count_all'))\
				.filter(Student.Program_Envollsin_program_id == args['Student.Program_Envollsin_program_id']).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_student_orderedby_all_parser = reqparse.RequestParser()
get_student_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@student_namespace.route('/get_student_orderedby_all', methods=['GET'])
class get_student_orderedby_all_resource(Resource):
    
    @student_namespace.expect(get_student_orderedby_all_parser)
    def get(self):
        args = get_student_orderedby_all_parser.parse_args()
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

