from .holder_api import holder_namespace 
from .stock_api import stock_namespace 
from flask_restx import Api 


def api_namespaces(blueprint,url_prefix,title): 
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) 
    rest_plus_api.add_namespace(holder_namespace,path="/holder")
    rest_plus_api.add_namespace(stock_namespace,path="/stock")
    
    return rest_plus_api