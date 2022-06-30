from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import player_allstar 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
player_allstar_namespace = Namespace("player_allstar", description="player_allstar Api") 


player_allstar_model =player_allstar_namespace.model("player_allstar",convert_db_model_to_restx_model(player_allstar)) 
player_allstar_id_parser = reqparse.RequestParser() 
player_allstar_id_parser.add_argument('playerID',type=str)


@player_allstar_namespace.route("/")
class player_allstarApi(Resource):

    def get(self):
        try:
            player_allstars = db.session.query(player_allstar).all()
            player_allstars = [row.serialize() for row in player_allstars]
            return player_allstars , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @player_allstar_namespace.expect(player_allstar_model) 
    def post(self):
        try:
            player_allstars = player_allstar(playerID = request.json.get("playerID"),last_name = request.json.get("last_name"),first_name = request.json.get("first_name"),season_id = request.json.get("season_id"),conference = request.json.get("conference"),league_id = request.json.get("league_id"),games_played = request.json.get("games_played"),minutes = request.json.get("minutes"),points = request.json.get("points"),o_rebounds = request.json.get("o_rebounds"),d_rebounds = request.json.get("d_rebounds"),rebounds = request.json.get("rebounds"),assists = request.json.get("assists"),steals = request.json.get("steals"),blocks = request.json.get("blocks"),turnovers = request.json.get("turnovers"),personal_fouls = request.json.get("personal_fouls"),fg_attempted = request.json.get("fg_attempted"),fg_made = request.json.get("fg_made"),ft_attempted = request.json.get("ft_attempted"),ft_made = request.json.get("ft_made"),three_attempted = request.json.get("three_attempted"),three_made = request.json.get("three_made"))
            db.session.add(player_allstars)
            db.session.commit()    
            return player_allstars.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @player_allstar_namespace.expect(player_allstar_model) 
    def put(self):
        try:
            db.session.query(player_allstar).filter(player_allstar.playerID==request.json.get('playerID') ).update(request.json) 
            db.session.commit() 
            player_allstars = db.session.query(player_allstar).filter(player_allstar.playerID==request.json.get('playerID') ).first() 
            return player_allstars.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @player_allstar_namespace.expect(player_allstar_id_parser) 
    def delete(self):
        try:
            player_allstars = db.session.query(player_allstar).filter(player_allstar.playerID==player_allstar_id_parser.parse_args().get('playerID') ).first() 
            db.session.query(player_allstar).filter(player_allstar.playerID==player_allstar_id_parser.parse_args().get('playerID') ).delete() 
            db.session.commit() 
            return player_allstars.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

