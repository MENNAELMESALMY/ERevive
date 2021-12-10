from .DEPARTMENT_api import departments_namespace 
from .DEPARTMENT_Clocation_api import department_clocations_namespace 
from .EMPLOYEE_api import employees_namespace 
from .PROJECT_api import projects_namespace 
from .DEPENDENT_api import dependents_namespace 
from .Works_EMPLOYEE_PROJECT_api import works_employee_projects_namespace 
from flask_restx import Api 


def api_namespaces(blueprint,url_prefix,title): 
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) 
    rest_plus_api.add_namespace(departments_namespace,path="/departments")
    rest_plus_api.add_namespace(department_clocations_namespace,path="/department_clocations")
    rest_plus_api.add_namespace(employees_namespace,path="/employees")
    rest_plus_api.add_namespace(projects_namespace,path="/projects")
    rest_plus_api.add_namespace(dependents_namespace,path="/dependents")
    rest_plus_api.add_namespace(works_employee_projects_namespace,path="/works_employee_projects")
    return rest_plus_api
