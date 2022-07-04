from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Attempts_course_Student 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
attempts_course_student_namespace = Namespace("Attempts_course_Student", description="Attempts_course_Student Api") 


attempts_course_student_model =attempts_course_student_namespace.model("attempts_course_student",convert_db_model_to_restx_model(Attempts_course_Student)) 
attempts_course_student_id_parser = reqparse.RequestParser() 
attempts_course_student_id_parser.add_argument('Student_Student_ID',type=int)
attempts_course_student_id_parser.add_argument('course_Program_program_id',type=int)
attempts_course_student_id_parser.add_argument('course_course_id',type=int)


@attempts_course_student_namespace.route("/")
class Attempts_course_StudentApi(Resource):

    def get(self):
        try:
            attempts_course_students = db.session.query(Attempts_course_Student).all()
            attempts_course_students = [row.serialize() for row in attempts_course_students]
            return attempts_course_students , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @attempts_course_student_namespace.expect(attempts_course_student_model) 
    def post(self):
        try:
            attempts_course_students = Attempts_course_Student(Year = request.json.get("Year"),Grade = request.json.get("Grade"),Mark = request.json.get("Mark"),Semester = request.json.get("Semester"),Student_Student_ID = request.json.get("Student_Student_ID"),course_Program_program_id = request.json.get("course_Program_program_id"),course_course_id = request.json.get("course_course_id"))
            db.session.add(attempts_course_students)
            db.session.commit()    
            return attempts_course_students.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @attempts_course_student_namespace.expect(attempts_course_student_model) 
    def put(self):
        try:
            db.session.query(Attempts_course_Student).filter(Attempts_course_Student.Student_Student_ID==request.json.get('Student_Student_ID') and Attempts_course_Student.course_Program_program_id==request.json.get('course_Program_program_id') and Attempts_course_Student.course_course_id==request.json.get('course_course_id') ).update(request.json) 
            db.session.commit() 
            attempts_course_students = db.session.query(Attempts_course_Student).filter(Attempts_course_Student.Student_Student_ID==request.json.get('Student_Student_ID') and Attempts_course_Student.course_Program_program_id==request.json.get('course_Program_program_id') and Attempts_course_Student.course_course_id==request.json.get('course_course_id') ).first() 
            return attempts_course_students.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @attempts_course_student_namespace.expect(attempts_course_student_id_parser) 
    def delete(self):
        try:
            attempts_course_students = db.session.query(Attempts_course_Student).filter(Attempts_course_Student.Student_Student_ID==attempts_course_student_id_parser.parse_args().get('Student_Student_ID') and Attempts_course_Student.course_Program_program_id==attempts_course_student_id_parser.parse_args().get('course_Program_program_id') and Attempts_course_Student.course_course_id==attempts_course_student_id_parser.parse_args().get('course_course_id') ).first() 
            db.session.query(Attempts_course_Student).filter(Attempts_course_Student.Student_Student_ID==attempts_course_student_id_parser.parse_args().get('Student_Student_ID') and Attempts_course_Student.course_Program_program_id==attempts_course_student_id_parser.parse_args().get('course_Program_program_id') and Attempts_course_Student.course_course_id==attempts_course_student_id_parser.parse_args().get('course_course_id') ).delete() 
            db.session.commit() 
            return attempts_course_students.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

