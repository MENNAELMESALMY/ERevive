from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
coaches_namespace = Namespace("coaches", description="coaches Api") 


coaches_model =coaches_namespace.model("coaches",convert_db_model_to_restx_model(coaches)) 
coaches_id_parser = reqparse.RequestParser() 
coaches_id_parser.add_argument('coachID',type=str)
coaches_id_parser.add_argument('year',type=int)
coaches_id_parser.add_argument('tmID',type=str)
coaches_id_parser.add_argument('stint',type=int)


@coaches_namespace.route("/")
class coachesApi(Resource):

    @coaches_namespace.marshal_list_with(coaches_model) 
    def get(self):
        coachess = db.session.query(coaches).all()
        return coachess , 200  

    @coaches_namespace.marshal_with(coaches_model) 
    @coaches_namespace.expect(coaches_model) 
    def post(self):
        coaches = coaches(coachID = request.json.get("coachID"),year = request.json.get("year"),tmID = request.json.get("tmID"),lgID = request.json.get("lgID"),stint = request.json.get("stint"),won = request.json.get("won"),lost = request.json.get("lost"),post_wins = request.json.get("post_wins"),post_losses = request.json.get("post_losses"))
        db.session.add(coaches)
        db.session.commit()    
        return coaches , 201 

    @coaches_namespace.marshal_with(coaches_model) 
    @coaches_namespace.expect(coaches_model) 
    def put(self):
        db.session.query(coaches).filter(coaches.id==id).update(request.json) 
        db.session.commit() 
        coaches = db.session.query(coaches).filter(coaches.id==id).first() 
        return coaches , 200    

    @coaches_namespace.marshal_with(coaches_model) 
    @coaches_namespace.expect(coaches_id_parser) 
    def delete(self):
        coaches = db.session.query(coaches).filter(coaches.id==id).first() 
        db.session.query(coaches).filter(coaches.id==id).delete() 
        db.session.commit() 
        return coaches , 200    

get_coaches_filteredby_coachID_model = coaches_namespace.model('get_coaches_filteredby_coachID_model',{ 'coaches.coachID' : fields.String,'coaches.year' : fields.Integer,'coaches.tmID' : fields.String,'coaches.lgID' : fields.String,'coaches.stint' : fields.Integer,'coaches.won' : fields.Integer,'coaches.lost' : fields.Integer,'coaches.post_wins' : fields.Integer,'coaches.post_losses' : fields.Integer,'count_all' : fields.Integer })
get_coaches_filteredby_coachID_parser = reqparse.RequestParser()
get_coaches_filteredby_coachID_parser.add_argument('coaches.coachID', type=str, required=True, location='args')

@coaches_namespace.route('/get_coaches_filteredby_coachID', methods=['GET'])
class get_coaches_filteredby_coachID_resource(Resource):
    @coaches_namespace.marshal_list_with(get_coaches_filteredby_coachID_model)
    @coaches_namespace.expect(get_coaches_filteredby_coachID_parser)

    def get(self):
        args = get_coaches_filteredby_coachID_parser.parse_args()

        results = db.session.query(coaches, func.count().label('count_all'))\
			.filter(coaches.coachID == args['coaches.coachID'])
        return results

get_coaches_model = coaches_namespace.model('get_coaches_model',{ 'coaches.coachID' : fields.String,'coaches.year' : fields.Integer,'coaches.tmID' : fields.String,'coaches.lgID' : fields.String,'coaches.stint' : fields.Integer,'coaches.won' : fields.Integer,'coaches.lost' : fields.Integer,'coaches.post_wins' : fields.Integer,'coaches.post_losses' : fields.Integer,'count_coaches.coachID' : fields.String,'count_all' : fields.Integer })

@coaches_namespace.route('/get_coaches', methods=['GET'])
class get_coaches_resource(Resource):
    @coaches_namespace.marshal_list_with(get_coaches_model)
    
    def get(self):
        
        results = db.session.query(coaches, func.count(coaches.coachID).label('count_coaches.coachID'), func.count().label('count_all'))
        return results

get_coaches_filteredby_year_model = coaches_namespace.model('get_coaches_filteredby_year_model',{ 'coaches.year' : fields.Integer,'coaches.coachID' : fields.String,'count_all' : fields.Integer,'count_coaches.coachID' : fields.String })
get_coaches_filteredby_year_parser = reqparse.RequestParser()
get_coaches_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@coaches_namespace.route('/get_coaches_filteredby_year', methods=['GET'])
class get_coaches_filteredby_year_resource(Resource):
    @coaches_namespace.marshal_list_with(get_coaches_filteredby_year_model)
    @coaches_namespace.expect(get_coaches_filteredby_year_parser)

    def get(self):
        args = get_coaches_filteredby_year_parser.parse_args()

        results = db.session.query(coaches.year, coaches.coachID, func.count().label('count_all'), func.count(coaches.coachID).label('count_coaches.coachID'))\
			.filter(coaches.year == args['coaches.year'])\
			.group_by(coaches.year, coaches.coachID)
        return results

get_coaches_groupedby_coachID_model = coaches_namespace.model('get_coaches_groupedby_coachID_model',{ 'coaches.tmID' : fields.String,'coaches.coachID' : fields.String,'count_all' : fields.Integer })
get_coaches_groupedby_coachID_parser = reqparse.RequestParser()
get_coaches_groupedby_coachID_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_namespace.route('/get_coaches_groupedby_coachID', methods=['GET'])
class get_coaches_groupedby_coachID_resource(Resource):
    @coaches_namespace.marshal_list_with(get_coaches_groupedby_coachID_model)
    @coaches_namespace.expect(get_coaches_groupedby_coachID_parser)

    def get(self):
        args = get_coaches_groupedby_coachID_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(coaches.tmID, coaches.coachID, func.count().label('count_all'))\
			.group_by(coaches.tmID, coaches.coachID)\
			.order_by(direction(func.count()))
        return results

get_coaches_model = coaches_namespace.model('get_coaches_model',{ 'coaches.coachID' : fields.String,'count_all' : fields.Integer })
get_coaches_parser = reqparse.RequestParser()
get_coaches_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_namespace.route('/get_coaches', methods=['GET'])
class get_coaches_resource(Resource):
    @coaches_namespace.marshal_list_with(get_coaches_model)
    @coaches_namespace.expect(get_coaches_parser)

    def get(self):
        args = get_coaches_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(coaches.coachID, func.count().label('count_all'))\
			.group_by(coaches.coachID)\
			.order_by(direction(func.count()))
        return results

get_coaches_filteredby_coachID_year_model = coaches_namespace.model('get_coaches_filteredby_coachID_year_model',{ 'coaches.coachID' : fields.String,'coaches.year' : fields.Integer,'coaches.tmID' : fields.String,'coaches.lgID' : fields.String,'coaches.stint' : fields.Integer,'coaches.won' : fields.Integer,'coaches.lost' : fields.Integer,'coaches.post_wins' : fields.Integer,'coaches.post_losses' : fields.Intege })
get_coaches_filteredby_coachID_year_parser = reqparse.RequestParser()
get_coaches_filteredby_coachID_year_parser.add_argument('coaches.coachID', type=str, required=True, location='args')
get_coaches_filteredby_coachID_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@coaches_namespace.route('/get_coaches_filteredby_coachID_year', methods=['GET'])
class get_coaches_filteredby_coachID_year_resource(Resource):
    @coaches_namespace.marshal_list_with(get_coaches_filteredby_coachID_year_model)
    @coaches_namespace.expect(get_coaches_filteredby_coachID_year_parser)

    def get(self):
        args = get_coaches_filteredby_coachID_year_parser.parse_args()

        results = db.session.query(coaches)\
			.filter(coaches.coachID == args['coaches.coachID'], coaches.year == args['coaches.year'])
        return results

get_coaches_groupedby_year_model = coaches_namespace.model('get_coaches_groupedby_year_model',{ 'coaches.year' : fields.Integer })
get_coaches_groupedby_year_parser = reqparse.RequestParser()
get_coaches_groupedby_year_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@coaches_namespace.route('/get_coaches_groupedby_year', methods=['GET'])
class get_coaches_groupedby_year_resource(Resource):
    @coaches_namespace.marshal_list_with(get_coaches_groupedby_year_model)
    @coaches_namespace.expect(get_coaches_groupedby_year_parser)

    def get(self):
        args = get_coaches_groupedby_year_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(coaches.year)\
			.group_by(coaches.year)\
			.order_by(direction(func.count()))
        return results

