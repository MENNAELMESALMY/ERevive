from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import awards_coaches 
from app import db 
from utils import convert_db_model_to_restx_model 
            
awards_coaches_namespace = Namespace("awards_coaches", description="awards_coaches Api") 


awards_coaches_model =awards_coaches_namespace.model("awards_coaches",convert_db_model_to_restx_model(awards_coaches)) 
awards_coaches_id_parser = reqparse.RequestParser() 
awards_coaches_id_parser.add_argument('id',type=str)


@awards_coaches_namespace.route("/")
class awards_coachesApi(Resource):

    @awards_coaches_namespace.marshal_list_with(awards_coaches_model) 
    def get(self):
        awards_coachess = db.session.query(awards_coaches).all()
        return awards_coachess , 200  

    @awards_coaches_namespace.marshal_with(awards_coaches_model) 
    @awards_coaches_namespace.expect(awards_coaches_model) 
    def post(self):
        awards_coaches = awards_coaches(id = request.json.get("id"),coachID = request.json.get("coachID"),award = request.json.get("award"),lgID = request.json.get("lgID"),note = request.json.get("note"))
        db.session.add(awards_coaches)
        db.session.commit()    
        return awards_coaches , 201 

    @awards_coaches_namespace.marshal_with(awards_coaches_model) 
    @awards_coaches_namespace.expect(awards_coaches_model) 
    def put(self):
        db.session.query(awards_coaches).filter(awards_coaches.id==id).update(request.json) 
        db.session.commit() 
        awards_coaches = db.session.query(awards_coaches).filter(awards_coaches.id==id).first() 
        return awards_coaches , 200    

    @awards_coaches_namespace.marshal_with(awards_coaches_model) 
    @awards_coaches_namespace.expect(awards_coaches_id_parser) 
    def delete(self):
        awards_coaches = db.session.query(awards_coaches).filter(awards_coaches.id==id).first() 
        db.session.query(awards_coaches).filter(awards_coaches.id==id).delete() 
        db.session.commit() 
        return awards_coaches , 200    

get_awards_coaches_model = awards_coaches_namespace.model('get_awards_coaches_model',{ 'awards_coaches.id' : fields.String,'awards_coaches.coachID' : fields.DateTime,'awards_coaches.award' : fields.String,'awards_coaches.lgID' : fields.String,'awards_coaches.note' : fields.String,'count_all' : fields.Integer })

@awards_coaches_namespace.route('/get_awards_coaches', methods=['GET'])
class get_awards_coaches_resource(Resource):
    @awards_coaches_namespace.marshal_list_with(get_awards_coaches_model)
    
    def get(self):
        
        results = db.session.query(awards_coaches, func.count().label('count_all'))
        return results

get_awards_coaches_filteredby_coachID_model = awards_coaches_namespace.model('get_awards_coaches_filteredby_coachID_model',{ 'awards_coaches.id' : fields.String,'awards_coaches.coachID' : fields.DateTime,'awards_coaches.award' : fields.String,'awards_coaches.lgID' : fields.String,'awards_coaches.note' : fields.Strin })

@awards_coaches_namespace.route('/get_awards_coaches_filteredby_coachID', methods=['GET'])
class get_awards_coaches_filteredby_coachID_resource(Resource):
    @awards_coaches_namespace.marshal_list_with(get_awards_coaches_filteredby_coachID_model)
    
    def get(self):
        
        results = db.session.query(awards_coaches)\
			.filter(awards_coaches.coachID == awards_coaches.id)
        return results

get_coaches_awards_coaches_filteredby_year_model = awards_coaches_namespace.model('get_coaches_awards_coaches_filteredby_year_model',{ 'coaches.coachID' : fields.String })
get_coaches_awards_coaches_filteredby_year_parser = reqparse.RequestParser()
get_coaches_awards_coaches_filteredby_year_parser.add_argument('coaches.year', type=int, required=True, location='args')

@awards_coaches_namespace.route('/get_coaches_awards_coaches_filteredby_year', methods=['GET'])
class get_coaches_awards_coaches_filteredby_year_resource(Resource):
    @awards_coaches_namespace.marshal_list_with(get_coaches_awards_coaches_filteredby_year_model)
    @awards_coaches_namespace.expect(get_coaches_awards_coaches_filteredby_year_parser)

    def get(self):
        args = get_coaches_awards_coaches_filteredby_year_parser.parse_args()

        results = db.session.query(coaches.coachID)\
			.join(coaches, coaches.coachID == awards_coaches.coachID)\
			.filter(coaches.year == args['coaches.year'])
        return results

get_awards_coaches_coaches_model = awards_coaches_namespace.model('get_awards_coaches_coaches_model',{ 'count_all' : fields.Integer })
get_awards_coaches_coaches_parser = reqparse.RequestParser()
get_awards_coaches_coaches_parser.add_argument('is_order_of_count_of_rows_desc', type=bool, required=True, location='args')

@awards_coaches_namespace.route('/get_awards_coaches_coaches', methods=['GET'])
class get_awards_coaches_coaches_resource(Resource):
    @awards_coaches_namespace.marshal_list_with(get_awards_coaches_coaches_model)
    @awards_coaches_namespace.expect(get_awards_coaches_coaches_parser)

    def get(self):
        args = get_awards_coaches_coaches_parser.parse_args()
        direction = desc if args['is_order_of_count_of_rows_desc'] else asc

        results = db.session.query(func.count().label('count_all'))\
			.join(awards_coaches, awards_coaches.coachID == coaches.coachID)\
			.order_by(direction(func.count()))
        return results

