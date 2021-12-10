
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine 
from decouple import config 

user=config("user") 
password=config("password") 
database=config("database") 
db = SQLAlchemy() 
connection_string = "mysql+mysqlconnector://{0}:{1}@127.0.0.1:3306".format(user, password) 
def create_app(): 
    app = Flask(__name__) 
    settings = dict() 
    settings["SQLALCHEMY_DATABASE_URI"] = connection_string+"/{0}".format(database) 
    settings["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    app.config.update(settings) 
    return app 

def create_db(app): 
    with app.app_context(): 
        db.init_app(app) 
        engine = create_engine(connection_string) 
        create_str = "CREATE DATABASE IF NOT EXISTS `{0}` ;".format(database) 
        engine.execute(create_str) 
        engine.execute("USE `{0}`;".format(database)) 
        db.create_all(bind="__all__", app=app) 
        db.session.commit() 
        return db 

