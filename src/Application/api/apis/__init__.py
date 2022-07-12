from .articles_api import articles_namespace 
from .comments_api import comments_namespace 
from .users_api import users_namespace 
from flask_restx import Api 


def api_namespaces(blueprint,url_prefix,title): 
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) 
    rest_plus_api.add_namespace(articles_namespace,path="/articles")
    rest_plus_api.add_namespace(comments_namespace,path="/comments")
    rest_plus_api.add_namespace(users_namespace,path="/users")
    
    return rest_plus_api