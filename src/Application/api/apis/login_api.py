from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import Login 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
login_namespace = Namespace("Login", description="Login Api") 


login_model =login_namespace.model("login",convert_db_model_to_restx_model(Login)) 
login_id_parser = reqparse.RequestParser() 
login_id_parser.add_argument('username',type=str)


@login_namespace.route("/")
class LoginApi(Resource):

    def get(self):
        try:
            logins = db.session.query(Login).all()
            logins = [row.serialize() for row in logins]
            return logins , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @login_namespace.expect(login_model) 
    def post(self):
        try:
            logins = Login(password = request.json.get("password"),username = request.json.get("username"))
            db.session.add(logins)
            db.session.commit()    
            return logins.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @login_namespace.expect(login_model) 
    def put(self):
        try:
            db.session.query(Login).filter(Login.username==request.json.get('username') ).update(request.json) 
            db.session.commit() 
            logins = db.session.query(Login).filter(Login.username==request.json.get('username') ).first() 
            return logins.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @login_namespace.expect(login_id_parser) 
    def delete(self):
        try:
            logins = db.session.query(Login).filter(Login.username==login_id_parser.parse_args().get('username') ).first() 
            db.session.query(Login).filter(Login.username==login_id_parser.parse_args().get('username') ).delete() 
            db.session.commit() 
            return logins.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

