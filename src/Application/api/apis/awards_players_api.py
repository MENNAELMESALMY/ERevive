from datetime import datetime 
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
        try:
            awards_playerss = db.session.query(awards_players).all()
        except Exception as e:
            return None , 500
        return awards_playerss , 200  

    @awards_players_namespace.marshal_with(awards_players_model) 
    @awards_players_namespace.expect(awards_players_model) 
    def post(self):
        try:
            awards_playerss = awards_players(playerID = request.json.get("playerID"),award = request.json.get("award"),year = request.json.get("year"),lgID = request.json.get("lgID"),note = request.json.get("note"),pos = request.json.get("pos"))
            db.session.add(awards_playerss)
            db.session.commit()    
        except Exception as e:
            return None , 500
        return awards_playerss , 201 

    @awards_players_namespace.marshal_with(awards_players_model) 
    @awards_players_namespace.expect(awards_players_model) 
    def put(self):
        try:
            db.session.query(awards_players).filter(awards_players.year==request.json.get('year') and awards_players.lgID==request.json.get('lgID') ).update(request.json) 
            db.session.commit() 
            awards_playerss = db.session.query(awards_players).filter(awards_players.year==request.json.get('year') and awards_players.lgID==request.json.get('lgID') ).first() 
        except Exception as e:
            return None , 500
        return awards_playerss , 200    

    @awards_players_namespace.marshal_with(awards_players_model) 
    @awards_players_namespace.expect(awards_players_id_parser) 
    def delete(self):
        try:
            awards_playerss = db.session.query(awards_players).filter(awards_players.year==awards_players_id_parser.parse_args().get('year') and awards_players.lgID==awards_players_id_parser.parse_args().get('lgID') ).first() 
            db.session.query(awards_players).filter(awards_players.year==awards_players_id_parser.parse_args().get('year') and awards_players.lgID==awards_players_id_parser.parse_args().get('lgID') ).delete() 
            db.session.commit() 
        except Exception as e:
            return None , 500
        return awards_playerss , 200    

get_awards_players_filteredby_year_model = awards_players_namespace.model('get_awards_players_filteredby_year_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'count_awards_players.year' : fields.Integer,'count_all' : fields.Integer })
get_awards_players_filteredby_year_parser = reqparse.RequestParser()
get_awards_players_filteredby_year_parser.add_argument('awards_players.year', type=int, required=True, location='args')

@awards_players_namespace.route('/get_awards_players_filteredby_year', methods=['GET'])
class get_awards_players_filteredby_year_resource(Resource):
    @awards_players_namespace.marshal_list_with(get_awards_players_filteredby_year_model)
    @awards_players_namespace.expect(get_awards_players_filteredby_year_parser)

    def get(self):
        args = get_awards_players_filteredby_year_parser.parse_args()

        results = None
        try:
            results = db.session.query(awards_players, func.count(awards_players.year).label('count_awards_players.year'), func.count().label('count_all'))\
				.filter(awards_players.year == args['awards_players.year'])\
				.group_by(awards_players.note, awards_players.year, awards_players.lgID, awards_players.award, awards_players.pos, awards_players.playerID).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_model = awards_players_namespace.model('get_awards_players_model',{ 'awards_players.playerID' : fields.String,'awards_players.award' : fields.String,'awards_players.year' : fields.Integer,'awards_players.lgID' : fields.String,'awards_players.note' : fields.String,'awards_players.pos' : fields.String,'count_awards_players.year' : fields.Integer,'count_awards_players.playerID' : fields.String,'count_all' : fields.Integer })

@awards_players_namespace.route('/get_awards_players', methods=['GET'])
class get_awards_players_resource(Resource):
    @awards_players_namespace.marshal_list_with(get_awards_players_model)
    
    def get(self):
        
        results = None
        try:
            results = db.session.query(awards_players, func.count(awards_players.year).label('count_awards_players.year'), func.count(awards_players.playerID).label('count_awards_players.playerID'), func.count().label('count_all'))\
				.group_by(awards_players.note, awards_players.year, awards_players.lgID, awards_players.award, awards_players.pos, awards_players.playerID).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_filteredby_playerID_model = awards_players_namespace.model('get_awards_players_filteredby_playerID_model',{ 'awards_players.playerID' : fields.String,'awards_players.lgID' : fields.String,'count_all' : fields.Integer })
get_awards_players_filteredby_playerID_parser = reqparse.RequestParser()
get_awards_players_filteredby_playerID_parser.add_argument('awards_players.playerID', type=str, required=True, location='args')

@awards_players_namespace.route('/get_awards_players_filteredby_playerID', methods=['GET'])
class get_awards_players_filteredby_playerID_resource(Resource):
    @awards_players_namespace.marshal_list_with(get_awards_players_filteredby_playerID_model)
    @awards_players_namespace.expect(get_awards_players_filteredby_playerID_parser)

    def get(self):
        args = get_awards_players_filteredby_playerID_parser.parse_args()

        results = None
        try:
            results = db.session.query(awards_players.playerID, awards_players.lgID, func.count().label('count_all'))\
				.filter(awards_players.playerID == args['awards_players.playerID'])\
				.group_by(awards_players.lgID, awards_players.playerID).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_filteredby_year_playerID_model = awards_players_namespace.model('get_awards_players_filteredby_year_playerID_model',{ 'awards_players.year' : fields.Integer })
get_awards_players_filteredby_year_playerID_parser = reqparse.RequestParser()
get_awards_players_filteredby_year_playerID_parser.add_argument('awards_players.year', type=int, required=True, location='args')
get_awards_players_filteredby_year_playerID_parser.add_argument('awards_players.playerID', type=str, required=True, location='args')

@awards_players_namespace.route('/get_awards_players_filteredby_year_playerID', methods=['GET'])
class get_awards_players_filteredby_year_playerID_resource(Resource):
    @awards_players_namespace.marshal_list_with(get_awards_players_filteredby_year_playerID_model)
    @awards_players_namespace.expect(get_awards_players_filteredby_year_playerID_parser)

    def get(self):
        args = get_awards_players_filteredby_year_playerID_parser.parse_args()

        results = None
        try:
            results = db.session.query(awards_players.year)\
				.filter(awards_players.year == args['awards_players.year'], awards_players.playerID == args['awards_players.playerID']).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_groupedby_playerID_model = awards_players_namespace.model('get_awards_players_groupedby_playerID_model',{ 'awards_players.playerID' : fields.String,'count_all' : fields.Integer })
get_awards_players_groupedby_playerID_parser = reqparse.RequestParser()
get_awards_players_groupedby_playerID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@awards_players_namespace.route('/get_awards_players_groupedby_playerID', methods=['GET'])
class get_awards_players_groupedby_playerID_resource(Resource):
    @awards_players_namespace.marshal_list_with(get_awards_players_groupedby_playerID_model)
    @awards_players_namespace.expect(get_awards_players_groupedby_playerID_parser)

    def get(self):
        args = get_awards_players_groupedby_playerID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(awards_players.playerID, func.count().label('count_all'))\
				.group_by(awards_players.playerID)\
				.order_by(direction(func.count())).all()

        except Exception as e:
            return None , 400

        return results , 200

get_awards_players_model = awards_players_namespace.model('get_awards_players_model',{ 'count_all' : fields.Integer })
get_awards_players_parser = reqparse.RequestParser()
get_awards_players_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@awards_players_namespace.route('/get_awards_players', methods=['GET'])
class get_awards_players_resource(Resource):
    @awards_players_namespace.marshal_list_with(get_awards_players_model)
    @awards_players_namespace.expect(get_awards_players_parser)

    def get(self):
        args = get_awards_players_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = None
        try:
            results = db.session.query(func.count().label('count_all'))\
				.order_by(direction(func.count())).all()

        except Exception as e:
            return None , 400

        return results , 200

