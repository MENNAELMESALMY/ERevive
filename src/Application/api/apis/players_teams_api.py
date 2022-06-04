from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import players_teams 
from app import db 
from utils import convert_db_model_to_restx_model 
            
players_teams_namespace = Namespace("players_teams", description="players_teams Api") 


players_teams_model =players_teams_namespace.model("players_teams",convert_db_model_to_restx_model(players_teams)) 
players_teams_id_parser = reqparse.RequestParser() 
players_teams_id_parser.add_argument('id',type=int)


@players_teams_namespace.route("/")
class players_teamsApi(Resource):

    @players_teams_namespace.marshal_list_with(players_teams_model) 
    def get(self):
        players_teamss = db.session.query(players_teams).all()
        return players_teamss , 200  

    @players_teams_namespace.marshal_with(players_teams_model) 
    @players_teams_namespace.expect(players_teams_model) 
    def post(self):
        players_teams = players_teams(id = request.json.get("id"),playerID = request.json.get("playerID"),year = request.json.get("year"),stint = request.json.get("stint"),tmID = request.json.get("tmID"),lgID = request.json.get("lgID"),GP = request.json.get("GP"),GS = request.json.get("GS"),minutes = request.json.get("minutes"),points = request.json.get("points"),oRebounds = request.json.get("oRebounds"),dRebounds = request.json.get("dRebounds"),rebounds = request.json.get("rebounds"),assists = request.json.get("assists"),steals = request.json.get("steals"),blocks = request.json.get("blocks"),turnovers = request.json.get("turnovers"),PF = request.json.get("PF"),fgAttempted = request.json.get("fgAttempted"),fgMade = request.json.get("fgMade"),ftAttempted = request.json.get("ftAttempted"),ftMade = request.json.get("ftMade"),threeAttempted = request.json.get("threeAttempted"),threeMade = request.json.get("threeMade"),PostGP = request.json.get("PostGP"),PostGS = request.json.get("PostGS"),PostMinutes = request.json.get("PostMinutes"),PostPoints = request.json.get("PostPoints"),PostoRebounds = request.json.get("PostoRebounds"),PostdRebounds = request.json.get("PostdRebounds"),PostRebounds = request.json.get("PostRebounds"),PostAssists = request.json.get("PostAssists"),PostSteals = request.json.get("PostSteals"),PostBlocks = request.json.get("PostBlocks"),PostTurnovers = request.json.get("PostTurnovers"),PostPF = request.json.get("PostPF"),PostfgAttempted = request.json.get("PostfgAttempted"),PostfgMade = request.json.get("PostfgMade"),PostftAttempted = request.json.get("PostftAttempted"),PostftMade = request.json.get("PostftMade"),PostthreeAttempted = request.json.get("PostthreeAttempted"),PostthreeMade = request.json.get("PostthreeMade"),note = request.json.get("note"))
        db.session.add(players_teams)
        db.session.commit()    
        return players_teams , 201 

    @players_teams_namespace.marshal_with(players_teams_model) 
    @players_teams_namespace.expect(players_teams_model) 
    def put(self):
        db.session.query(players_teams).filter(players_teams.id==id).update(request.json) 
        db.session.commit() 
        players_teams = db.session.query(players_teams).filter(players_teams.id==id).first() 
        return players_teams , 200    

    @players_teams_namespace.marshal_with(players_teams_model) 
    @players_teams_namespace.expect(players_teams_id_parser) 
    def delete(self):
        players_teams = db.session.query(players_teams).filter(players_teams.id==id).first() 
        db.session.query(players_teams).filter(players_teams.id==id).delete() 
        db.session.commit() 
        return players_teams , 200    

