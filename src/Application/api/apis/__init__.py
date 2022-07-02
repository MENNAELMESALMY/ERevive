from .comments,_api import comments,_namespace 
from ._api import _namespace 
from .posts_comments,__api import posts_comments,__namespace 
from ._comments,__api import _comments,__namespace 
from .writes___api import writes___namespace 
from flask_restx import Api 


def api_namespaces(blueprint,url_prefix,title): 
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) 
    rest_plus_api.add_namespace(comments,_namespace,path="/comments,")
    rest_plus_api.add_namespace(_namespace,path="/")
    rest_plus_api.add_namespace(posts_comments,__namespace,path="/posts_comments,_")
    rest_plus_api.add_namespace(_comments,__namespace,path="/_comments,_")
    rest_plus_api.add_namespace(writes___namespace,path="/writes__")
    
    return rest_plus_api