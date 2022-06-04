from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_players 
from app import db 
from utils import convert_db_model_to_restx_model 
            
awards_players_namespace = Namespace("awards_players", description="awards_players Api") 


awards_players_model =awards_players_namespace.model("awards_players",convert_db_model_to_restx_model(awards_players)) 
awards_players_id_parser = reqparse.RequestParser() 
awards_players_id_parser.add_argument('year',type=int)
awards_players_id_parser.add_argument('lgID',type=str)


@awards_players_namespace.route("/")
class awards_playersApi(Resource):

    @awards_players_namespace.marshal_list_with(awards_players_model) 
    def get(self):
        awards_playerss = db.session.query(awards_players).all()
        return awards_playerss , 200  

    @awards_players_namespace.marshal_with(awards_players_model) 
    @awards_players_namespace.expect(awards_players_model) 
    def post(self):
        awards_players = awards_players(playerID = request.json.get("playerID"),award = request.json.get("award"),year = request.json.get("year"),lgID = request.json.get("lgID"),note = request.json.get("note"),pos = request.json.get("pos"))
        db.session.add(awards_players)
        db.session.commit()    
        return awards_players , 201 

    @awards_players_namespace.marshal_with(awards_players_model) 
    @awards_players_namespace.expect(awards_players_model) 
    def put(self):
        db.session.query(awards_players).filter(awards_players.id==id).update(request.json) 
        db.session.commit() 
        awards_players = db.session.query(awards_players).filter(awards_players.id==id).first() 
        return awards_players , 200    

    @awards_players_namespace.marshal_with(awards_players_model) 
    @awards_players_namespace.expect(awards_players_id_parser) 
    def delete(self):
        awards_players = db.session.query(awards_players).filter(awards_players.id==id).first() 
        db.session.query(awards_players).filter(awards_players.id==id).delete() 
        db.session.commit() 
        return awards_players , 200    

