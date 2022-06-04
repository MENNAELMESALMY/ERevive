from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import teams 
from app import db 
from utils import convert_db_model_to_restx_model 
            
teams_namespace = Namespace("teams", description="teams Api") 


teams_model =teams_namespace.model("teams",convert_db_model_to_restx_model(teams)) 
teams_id_parser = reqparse.RequestParser() 
teams_id_parser.add_argument('year',type=int)
teams_id_parser.add_argument('tmID',type=str)


@teams_namespace.route("/")
class teamsApi(Resource):

    @teams_namespace.marshal_list_with(teams_model) 
    def get(self):
        teamss = db.session.query(teams).all()
        return teamss , 200  

    @teams_namespace.marshal_with(teams_model) 
    @teams_namespace.expect(teams_model) 
    def post(self):
        teams = teams(year = request.json.get("year"),lgID = request.json.get("lgID"),tmID = request.json.get("tmID"),franchID = request.json.get("franchID"),confID = request.json.get("confID"),divID = request.json.get("divID"),rank = request.json.get("rank"),confRank = request.json.get("confRank"),playoff = request.json.get("playoff"),name = request.json.get("name"))
        db.session.add(teams)
        db.session.commit()    
        return teams , 201 

    @teams_namespace.marshal_with(teams_model) 
    @teams_namespace.expect(teams_model) 
    def put(self):
        db.session.query(teams).filter(teams.id==id).update(request.json) 
        db.session.commit() 
        teams = db.session.query(teams).filter(teams.id==id).first() 
        return teams , 200    

    @teams_namespace.marshal_with(teams_model) 
    @teams_namespace.expect(teams_id_parser) 
    def delete(self):
        teams = db.session.query(teams).filter(teams.id==id).first() 
        db.session.query(teams).filter(teams.id==id).delete() 
        db.session.commit() 
        return teams , 200    

get_teams_filteredby_name_model = teams_namespace.model('get_teams_filteredby_name_model',{ 'teams.year' : fields.Integer,'teams.lgID' : fields.String,'teams.tmID' : fields.String,'teams.franchID' : fields.String,'teams.confID' : fields.String,'teams.divID' : fields.String,'teams.rank' : fields.Integer,'teams.confRank' : fields.Integer,'teams.playoff' : fields.String,'teams.name' : fields.String,'count_teams.year' : fields.Integer,'count_all' : fields.Integer,'count_teams.lgID' : fields.String })
get_teams_filteredby_name_parser = reqparse.RequestParser()
get_teams_filteredby_name_parser.add_argument('teams.name', type=str, required=True, location='args')

@teams_namespace.route('/get_teams_filteredby_name', methods=['GET'])
class get_teams_filteredby_name_resource(Resource):
    @teams_namespace.marshal_list_with(get_teams_filteredby_name_model)
    @teams_namespace.expect(get_teams_filteredby_name_parser)

    def get(self):
        args = get_teams_filteredby_name_parser.parse_args()

        results = db.session.query(teams, func.count(teams.year).label('count_teams.year'), func.count().label('count_all'), func.count(teams.lgID).label('count_teams.lgID'))\
			.filter(teams.name == args['teams.name'])
        return results

get_teams_groupedby_lgID_model = teams_namespace.model('get_teams_groupedby_lgID_model',{ 'teams.lgID' : fields.String,'teams.name' : fields.String })
get_teams_groupedby_lgID_parser = reqparse.RequestParser()
get_teams_groupedby_lgID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@teams_namespace.route('/get_teams_groupedby_lgID', methods=['GET'])
class get_teams_groupedby_lgID_resource(Resource):
    @teams_namespace.marshal_list_with(get_teams_groupedby_lgID_model)
    @teams_namespace.expect(get_teams_groupedby_lgID_parser)

    def get(self):
        args = get_teams_groupedby_lgID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(teams.lgID, teams.name)\
			.group_by(teams.lgID)\
			.order_by(direction(func.count()))
        return results

get_teams_filteredby_lgID_orderedby_franchID_model = teams_namespace.model('get_teams_filteredby_lgID_orderedby_franchID_model',{ 'teams.year' : fields.Integer,'teams.lgID' : fields.String,'teams.tmID' : fields.String,'teams.franchID' : fields.String,'teams.confID' : fields.String,'teams.divID' : fields.String,'teams.rank' : fields.Integer,'teams.confRank' : fields.Integer,'teams.playoff' : fields.String,'teams.name' : fields.Strin })
get_teams_filteredby_lgID_orderedby_franchID_parser = reqparse.RequestParser()
get_teams_filteredby_lgID_orderedby_franchID_parser.add_argument('is_order_of_franchID_desc', type=bool, required=True, location='args')

@teams_namespace.route('/get_teams_filteredby_lgID_orderedby_franchID', methods=['GET'])
class get_teams_filteredby_lgID_orderedby_franchID_resource(Resource):
    @teams_namespace.marshal_list_with(get_teams_filteredby_lgID_orderedby_franchID_model)
    @teams_namespace.expect(get_teams_filteredby_lgID_orderedby_franchID_parser)

    def get(self):
        args = get_teams_filteredby_lgID_orderedby_franchID_parser.parse_args()
        franchID_direction = desc if args['is_order_of_franchID_desc'] else asc

        results = db.session.query(teams)\
			.filter(teams.lgID == teams.tmID)\
			.order_by(franchID_direction(teams.franchID))
        return results

get_teams_filteredby_lgID_model = teams_namespace.model('get_teams_filteredby_lgID_model',{ 'teams.year' : fields.Integer,'teams.lgID' : fields.String,'teams.tmID' : fields.String,'teams.franchID' : fields.String,'teams.confID' : fields.String,'teams.divID' : fields.String,'teams.rank' : fields.Integer,'teams.confRank' : fields.Integer,'teams.playoff' : fields.String,'teams.name' : fields.String,'count_all' : fields.Integer,'count_teams.tmID' : fields.String })
get_teams_filteredby_lgID_parser = reqparse.RequestParser()
get_teams_filteredby_lgID_parser.add_argument('teams.lgID', type=str, required=True, location='args')

@teams_namespace.route('/get_teams_filteredby_lgID', methods=['GET'])
class get_teams_filteredby_lgID_resource(Resource):
    @teams_namespace.marshal_list_with(get_teams_filteredby_lgID_model)
    @teams_namespace.expect(get_teams_filteredby_lgID_parser)

    def get(self):
        args = get_teams_filteredby_lgID_parser.parse_args()

        results = db.session.query(teams, func.count().label('count_all'), func.count(teams.tmID).label('count_teams.tmID'))\
			.filter(teams.lgID == args['teams.lgID'])
        return results

get_teams_filteredby_lgID_orderedby_tmID_model = teams_namespace.model('get_teams_filteredby_lgID_orderedby_tmID_model',{ 'teams.year' : fields.Integer,'teams.lgID' : fields.String,'teams.tmID' : fields.String,'teams.franchID' : fields.String,'teams.confID' : fields.String,'teams.divID' : fields.String,'teams.rank' : fields.Integer,'teams.confRank' : fields.Integer,'teams.playoff' : fields.String,'teams.name' : fields.Strin })
get_teams_filteredby_lgID_orderedby_tmID_parser = reqparse.RequestParser()
get_teams_filteredby_lgID_orderedby_tmID_parser.add_argument('teams.lgID', type=str, required=True, location='args')
get_teams_filteredby_lgID_orderedby_tmID_parser.add_argument('is_order_of_tmID_desc', type=bool, required=True, location='args')

@teams_namespace.route('/get_teams_filteredby_lgID_orderedby_tmID', methods=['GET'])
class get_teams_filteredby_lgID_orderedby_tmID_resource(Resource):
    @teams_namespace.marshal_list_with(get_teams_filteredby_lgID_orderedby_tmID_model)
    @teams_namespace.expect(get_teams_filteredby_lgID_orderedby_tmID_parser)

    def get(self):
        args = get_teams_filteredby_lgID_orderedby_tmID_parser.parse_args()
        tmID_direction = desc if args['is_order_of_tmID_desc'] else asc

        results = db.session.query(teams)\
			.filter(teams.lgID between args['teams.lgID'])\
			.order_by(tmID_direction(teams.tmID))
        return results

get_teams_model = teams_namespace.model('get_teams_model',{ 'teams.year' : fields.Integer,'teams.lgID' : fields.String,'teams.tmID' : fields.String,'teams.franchID' : fields.String,'teams.confID' : fields.String,'teams.divID' : fields.String,'teams.rank' : fields.Integer,'teams.confRank' : fields.Integer,'teams.playoff' : fields.String,'teams.name' : fields.String,'max_teams.lgID' : fields.String,'count_all' : fields.Integer })

@teams_namespace.route('/get_teams', methods=['GET'])
class get_teams_resource(Resource):
    @teams_namespace.marshal_list_with(get_teams_model)
    
    def get(self):
        
        results = db.session.query(teams, func.max(teams.lgID).label('max_teams.lgID'), func.count().label('count_all'))
        return results

