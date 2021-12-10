 
from flask import Blueprint 
from flask_migrate import Migrate 
from app import create_app, create_db, db 
from apis import api_namespaces 
app = create_app() 
from models import * 
db = create_db(app) 
migrate = Migrate(app, db) 


prefix = "/api" 
API = Blueprint("api", __name__, url_prefix=prefix) 
rest_api= api_namespaces(blueprint=API, url_prefix=prefix,title="Main Api") 
app.register_blueprint(API, url_prefix=prefix) 
