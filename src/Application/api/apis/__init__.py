from .program_api import program_namespace 
from .student_api import student_namespace 
from .course_api import course_namespace 
from .attempts_course_student_api import attempts_course_student_namespace 
from .student_program_api import student_program_namespace 
from .student_attempts_course_student_api import student_attempts_course_student_namespace 
from flask_restx import Api 


def api_namespaces(blueprint,url_prefix,title): 
    rest_plus_api = Api(blueprint,url_prefix=url_prefix,title=title) 
    rest_plus_api.add_namespace(program_namespace,path="/program")
    rest_plus_api.add_namespace(student_namespace,path="/student")
    rest_plus_api.add_namespace(course_namespace,path="/course")
    rest_plus_api.add_namespace(attempts_course_student_namespace,path="/attempts_course_student")
    
    rest_plus_api.add_namespace(student_program_namespace,path="/student/program")
    rest_plus_api.add_namespace(student_attempts_course_student_namespace,path="/student/attempts_course_student")
    return rest_plus_api