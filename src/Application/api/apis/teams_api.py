from datetime import datetime 
from flask.helpers import make_response 
from flask_restx import Resource, Namespace , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import teams 
from app import db 
from utils import convert_db_model_to_restx_model , serialize 
            
teams_namespace = Namespace("teams", description="teams Api") 


teams_model =teams_namespace.model("teams",convert_db_model_to_restx_model(teams)) 
teams_id_parser = reqparse.RequestParser() 
teams_id_parser.add_argument('year',type=int)
teams_id_parser.add_argument('tmID',type=str)


@teams_namespace.route("/")
class teamsApi(Resource):

    def get(self):
        try:
            teamss = db.session.query(teams).all()
            teamss = [row.serialize() for row in teamss]
            return teamss , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @teams_namespace.expect(teams_model) 
    def post(self):
        try:
            teamss = teams(year = request.json.get("year"),lgID = request.json.get("lgID"),tmID = request.json.get("tmID"),franchID = request.json.get("franchID"),confID = request.json.get("confID"),divID = request.json.get("divID"),rank = request.json.get("rank"),confRank = request.json.get("confRank"),playoff = request.json.get("playoff"),name = request.json.get("name"))
            db.session.add(teamss)
            db.session.commit()    
            return teamss.serialize() , 201 
        except Exception as e:
            print(e)
            return str(e) , 400

    @teams_namespace.expect(teams_model) 
    def put(self):
        try:
            db.session.query(teams).filter(teams.year==request.json.get('year') and teams.tmID==request.json.get('tmID') ).update(request.json) 
            db.session.commit() 
            teamss = db.session.query(teams).filter(teams.year==request.json.get('year') and teams.tmID==request.json.get('tmID') ).first() 
            return teamss.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

    @teams_namespace.expect(teams_id_parser) 
    def delete(self):
        try:
            teamss = db.session.query(teams).filter(teams.year==teams_id_parser.parse_args().get('year') and teams.tmID==teams_id_parser.parse_args().get('tmID') ).first() 
            db.session.query(teams).filter(teams.year==teams_id_parser.parse_args().get('year') and teams.tmID==teams_id_parser.parse_args().get('tmID') ).delete() 
            db.session.commit() 
            return teamss.serialize() , 200 
        except Exception as e:
            print(e)
            return str(e) , 400

get_teams_filteredby_name_groupedby_all_parser = reqparse.RequestParser()
get_teams_filteredby_name_groupedby_all_parser.add_argument('teams.name', type=str, required=True, location='args')

@teams_namespace.route('/get_teams_filteredby_name_groupedby_all', methods=['GET'])
class get_teams_filteredby_name_groupedby_all_resource(Resource):
    
    @teams_namespace.expect(get_teams_filteredby_name_groupedby_all_parser)
    def get(self):
        args = get_teams_filteredby_name_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(teams, teams.year.label('teams.year'), func.count().label('count_all'))\
				.filter(teams.name == args['teams.name'])\
				.group_by(teams.playoff, teams.lgID, teams.rank, teams.confRank, teams.year, teams.tmID, teams.name, teams.franchID, teams.divID, teams.confID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_teams_groupedby_name_lgID_orderedby_all_parser = reqparse.RequestParser()
get_teams_groupedby_name_lgID_orderedby_all_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@teams_namespace.route('/get_teams_groupedby_name_lgID_orderedby_all', methods=['GET'])
class get_teams_groupedby_name_lgID_orderedby_all_resource(Resource):
    
    @teams_namespace.expect(get_teams_groupedby_name_lgID_orderedby_all_parser)
    def get(self):
        args = get_teams_groupedby_name_lgID_orderedby_all_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(teams, teams.lgID, teams.name)\
				.group_by(teams.lgID, teams.name)\
				.order_by(direction(func.count())).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_teams_filteredby_franchID_lgID_orderedby_tmID_parser = reqparse.RequestParser()
get_teams_filteredby_franchID_lgID_orderedby_tmID_parser.add_argument('is_order_of_tmID_desc', type=bool, required=True, location='args')

@teams_namespace.route('/get_teams_filteredby_franchID_lgID_orderedby_tmID', methods=['GET'])
class get_teams_filteredby_franchID_lgID_orderedby_tmID_resource(Resource):
    
    @teams_namespace.expect(get_teams_filteredby_franchID_lgID_orderedby_tmID_parser)
    def get(self):
        args = get_teams_filteredby_franchID_lgID_orderedby_tmID_parser.parse_args()
        tmID_direction = desc if args['is_order_of_tmID_desc'] else asc

        results = None
        try:
            results = db.session.query(teams, teams.year.label('teams.year'))\
				.filter(teams.lgID == teams.franchID)\
				.order_by(tmID_direction(teams.tmID)).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

get_teams_filteredby_lgID_groupedby_all_parser = reqparse.RequestParser()
get_teams_filteredby_lgID_groupedby_all_parser.add_argument('teams.lgID', type=str, required=True, location='args')

@teams_namespace.route('/get_teams_filteredby_lgID_groupedby_all', methods=['GET'])
class get_teams_filteredby_lgID_groupedby_all_resource(Resource):
    
    @teams_namespace.expect(get_teams_filteredby_lgID_groupedby_all_parser)
    def get(self):
        args = get_teams_filteredby_lgID_groupedby_all_parser.parse_args()

        results = None
        try:
            results = db.session.query(teams, teams.year.label('teams.year'), func.count().label('count_all'))\
				.filter(teams.lgID == args['teams.lgID'])\
				.group_by(teams.playoff, teams.lgID, teams.rank, teams.confRank, teams.year, teams.tmID, teams.name, teams.franchID, teams.divID, teams.confID).all()

            results = serialize(results)
            return results , 200
        except Exception as e:
            print(e)
            return str(e) , 400

