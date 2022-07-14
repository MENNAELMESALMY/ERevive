from .department_api import department_namespace 
from .department_location_api import department_location_namespace 
from .dependent_api import dependent_namespace 
from .employee_api import employee_namespace 
from .project_api import project_namespace 
from .works_employee_project_api import works_employee_project_namespace 
from .employee_department_location_department_api import employee_department_location_department_namespace 
from flask_restx import Api 


def api_namespaces(blueprint,url_prefix,title): 
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) 
    rest_plus_api.add_namespace(department_namespace,path="/department")
    rest_plus_api.add_namespace(department_location_namespace,path="/department_location")
    rest_plus_api.add_namespace(dependent_namespace,path="/dependent")
    rest_plus_api.add_namespace(employee_namespace,path="/employee")
    rest_plus_api.add_namespace(project_namespace,path="/project")
    rest_plus_api.add_namespace(works_employee_project_namespace,path="/works_employee_project")
    
    rest_plus_api.add_namespace(employee_department_location_department_namespace,path="/employee/department_location/department")
    return rest_plus_api