from flask.helpers import make_response 
from flask_restx import Resource, Namespace , fields , reqparse 
from flask import jsonify, request 
from sqlalchemy import func,desc,asc 
from models import series_post 
from app import db 
from utils import convert_db_model_to_restx_model 
            
series_post_namespace = Namespace("series_post", description="series_post Api") 


series_post_model =series_post_namespace.model("series_post",convert_db_model_to_restx_model(series_post)) 
series_post_id_parser = reqparse.RequestParser() 
series_post_id_parser.add_argument('id',type=str)


@series_post_namespace.route("/")
class series_postApi(Resource):

    @series_post_namespace.marshal_list_with(series_post_model) 
    def get(self):
        series_posts = db.session.query(series_post).all()
        return series_posts , 200  

    @series_post_namespace.marshal_with(series_post_model) 
    @series_post_namespace.expect(series_post_model) 
    def post(self):
        series_post = series_post(id = request.json.get("id"),year = request.json.get("year"),round = request.json.get("round"),series = request.json.get("series"),tmIDWinner = request.json.get("tmIDWinner"),lgIDWinner = request.json.get("lgIDWinner"),tmIDLoser = request.json.get("tmIDLoser"),lgIDLoser = request.json.get("lgIDLoser"),w = request.json.get("w"),L = request.json.get("L"))
        db.session.add(series_post)
        db.session.commit()    
        return series_post , 201 

    @series_post_namespace.marshal_with(series_post_model) 
    @series_post_namespace.expect(series_post_model) 
    def put(self):
        db.session.query(series_post).filter(series_post.id==id).update(request.json) 
        db.session.commit() 
        series_post = db.session.query(series_post).filter(series_post.id==id).first() 
        return series_post , 200    

    @series_post_namespace.marshal_with(series_post_model) 
    @series_post_namespace.expect(series_post_id_parser) 
    def delete(self):
        series_post = db.session.query(series_post).filter(series_post.id==id).first() 
        db.session.query(series_post).filter(series_post.id==id).delete() 
        db.session.commit() 
        return series_post , 200    

