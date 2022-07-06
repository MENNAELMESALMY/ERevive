from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Employee 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
employee_namespace = Namespace("Employee", description="Employee Api") 


employee_model =employee_namespace.model("employee",convert_db_model_to_restx_model(Employee)) 
employee_id_parser = reqparse.RequestParser() 
employee_id_parser.add_argument('email',type=str)


@employee_namespace.route("/")
class EmployeeApi(Resource):

    def get(self):
        try:
            employees = db.session.query(Employee).all()
            employees = [row.serialize() for row in employees]
            return employees , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @employee_namespace.expect(employee_model) 
    def post(self):
        try:
            employees = Employee(name = request.json.get("name"),phone = request.json.get("phone"),email = request.json.get("email"),Login_Has_username = request.json.get("Login_Has_username"),Role_Has_name = request.json.get("Role_Has_name"),Department_Has_name = request.json.get("Department_Has_name"))
            db.session.add(employees)
            db.session.commit()    
            return employees.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @employee_namespace.expect(employee_model) 
    def put(self):
        try:
            db.session.query(Employee).filter(Employee.email==request.json.get('email') ).update(request.json) 
            db.session.commit() 
            employees = db.session.query(Employee).filter(Employee.email==request.json.get('email') ).first() 
            return employees.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @employee_namespace.expect(employee_id_parser) 
    def delete(self):
        try:
            employees = db.session.query(Employee).filter(Employee.email==employee_id_parser.parse_args().get('email') ).first() 
            db.session.query(Employee).filter(Employee.email==employee_id_parser.parse_args().get('email') ).delete() 
            db.session.commit() 
            return employees.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

get_employee_filteredby_name_groupedby_all_parser = reqparse.RequestParser()
get_employee_filteredby_name_groupedby_all_parser.add_argument('Employee.name', type=str, required=True, location='args')

@employee_namespace.route('/get_employee_filteredby_name_groupedby_all', methods=['GET'])
class get_employee_filteredby_name_groupedby_all_resource(Resource):
    
    @employee_namespace.expect(get_employee_filteredby_name_groupedby_all_parser)
    def get(self):
        args = get_employee_filteredby_name_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(Employee, func.count().label('count_all'))\
				.filter(Employee.name == args['Employee.name'])\
				.group_by(Employee.Role_Has_name, Employee.Department_Has_name, Employee.name, Employee.email, Employee.Login_Has_username, Employee.phone).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400


@employee_namespace.route('/get_employee_groupedby_all', methods=['GET'])
class get_employee_groupedby_all_resource(Resource):
    
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(Employee, func.count().label('count_all'))\
				.group_by(Employee.Role_Has_name, Employee.Department_Has_name, Employee.name, Employee.email, Employee.Login_Has_username, Employee.phone).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_employee_groupedby_all_orderedby_name_parser = reqparse.RequestParser()
get_employee_groupedby_all_orderedby_name_parser.add_argument('is_order_of_name_desc', type=bool, required=True, location='args')

@employee_namespace.route('/get_employee_groupedby_all_orderedby_name', methods=['GET'])
class get_employee_groupedby_all_orderedby_name_resource(Resource):
    
    @employee_namespace.expect(get_employee_groupedby_all_orderedby_name_parser)
    def get(self):
        args = get_employee_groupedby_all_orderedby_name_parser.parse_args()
        name_direction = desc if args['is_order_of_name_desc'] else asc

        results = None
        try:
            results = db.session.query(Employee, func.count().label('count_all'))\
				.group_by(Employee.Role_Has_name, Employee.Department_Has_name, Employee.name, Employee.email, Employee.Login_Has_username, Employee.phone)\
				.order_by(name_direction(Employee.name)).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_employee_groupedby_name_orderedby_all_parser = reqparse.RequestParser()
get_employee_groupedby_name_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@employee_namespace.route('/get_employee_groupedby_name_orderedby_all', methods=['GET'])
class get_employee_groupedby_name_orderedby_all_resource(Resource):
    
    @employee_namespace.expect(get_employee_groupedby_name_orderedby_all_parser)
    def get(self):
        args = get_employee_groupedby_name_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(Employee.name.label('Employee.name'), func.count().label('count_all'))\
				.group_by(Employee.name)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_employee_orderedby_email_parser = reqparse.RequestParser()
get_employee_orderedby_email_parser.add_argument('is_order_of_email_desc', type=bool, required=True, location='args')

@employee_namespace.route('/get_employee_orderedby_email', methods=['GET'])
class get_employee_orderedby_email_resource(Resource):
    
    @employee_namespace.expect(get_employee_orderedby_email_parser)
    def get(self):
        args = get_employee_orderedby_email_parser.parse_args()
        email_direction = desc if args['is_order_of_email_desc'] else asc

        results = None
        try:
            results = db.session.query(Employee.email.label('Employee.email'))\
				.order_by(email_direction(Employee.email)).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_employee_orderedby_all_parser = reqparse.RequestParser()
get_employee_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@employee_namespace.route('/get_employee_orderedby_all', methods=['GET'])
class get_employee_orderedby_all_resource(Resource):
    
    @employee_namespace.expect(get_employee_orderedby_all_parser)
    def get(self):
        args = get_employee_orderedby_all_parser.parse_args()
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

