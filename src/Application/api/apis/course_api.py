from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import course 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
course_namespace = Namespace("course", description="course Api") 


course_model =course_namespace.model("course",convert_db_model_to_restx_model(course)) 
course_id_parser = reqparse.RequestParser() 
course_id_parser.add_argument('course_id',type=int)
course_id_parser.add_argument('contains_Program_program_id',type=int)


@course_namespace.route("/")
class courseApi(Resource):

    def get(self):
        try:
            courses = db.session.query(course).all()
            courses = [row.serialize() for row in courses]
            return courses , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @course_namespace.expect(course_model) 
    def post(self):
        try:
            courses = course(YearCommenced = request.json.get("YearCommenced"),course_id = request.json.get("course_id"),Name = request.json.get("Name"),CreditPoints = request.json.get("CreditPoints"),contains_Program_program_id = request.json.get("contains_Program_program_id"))
            db.session.add(courses)
            db.session.commit()    
            return courses.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @course_namespace.expect(course_model) 
    def put(self):
        try:
            db.session.query(course).filter(course.course_id==request.json.get('course_id') and course.contains_Program_program_id==request.json.get('contains_Program_program_id') ).update(request.json) 
            db.session.commit() 
            courses = db.session.query(course).filter(course.course_id==request.json.get('course_id') and course.contains_Program_program_id==request.json.get('contains_Program_program_id') ).first() 
            return courses.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @course_namespace.expect(course_id_parser) 
    def delete(self):
        try:
            courses = db.session.query(course).filter(course.course_id==course_id_parser.parse_args().get('course_id') and course.contains_Program_program_id==course_id_parser.parse_args().get('contains_Program_program_id') ).first() 
            db.session.query(course).filter(course.course_id==course_id_parser.parse_args().get('course_id') and course.contains_Program_program_id==course_id_parser.parse_args().get('contains_Program_program_id') ).delete() 
            db.session.commit() 
            return courses.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

