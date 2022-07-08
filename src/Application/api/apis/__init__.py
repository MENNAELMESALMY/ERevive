from .login_api import login_namespace 
from .role_api import role_namespace 
from .employee_api import employee_namespace 
from .department_api import department_namespace 
from flask_restx import Api 


def api_namespaces(blueprint,url_prefix,title): 
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) 
    rest_plus_api.add_namespace(login_namespace,path="/login")
    rest_plus_api.add_namespace(role_namespace,path="/role")
    rest_plus_api.add_namespace(employee_namespace,path="/employee")
    rest_plus_api.add_namespace(department_namespace,path="/department")
    
    return rest_plus_api