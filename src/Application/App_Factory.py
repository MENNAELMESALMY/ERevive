from Api_Factory import ApiFactory
import os
import stat
from generateModel import createAllModels
def Create_Directory(directory):
    path = os.path.join(os.getcwd(), directory) 
    os.umask(0)
    os.mkdir(path)
Create_Directory('api')
os.chdir('api')
  
# #Create Models method
def Create_Application(schema,user="root",password = "R$ingmybells5",db="default"):
    models = createAllModels(schema)  #should be replaced with nihal's models   
    api = ApiFactory(models,user,password,db)
    apisFiles = api.create_models_apis()
    createApis(apisFiles)
    create_api_init(api)
    create_app(api)
    create_app_init(api)
    create_app_requirements(api)
    create_app_run(api)
    create_app_setup(api)
    create_app_env(api)
    create_app_utils(api)   
def create_app_utils(api):
    app_utils = api.create_app_utils()
    with open('utils.py', 'w') as f:
        f.write(app_utils)
def create_app_env(api):
    app_env = api.create_app_env()
    with open('.env','w') as f:
        f.write(app_env)

def create_app_setup(api):
    app_setup = api.create_app_setup()
    with open('setup.sh','w') as f:
        f.write(app_setup)
    st = os.stat('setup.sh')
    os.chmod('setup.sh', st.st_mode | stat.S_IEXEC)

def create_app_run(api):
    app_run = api.create_app_run()
    with open('run.sh','w') as f:
        f.write(app_run)
    st = os.stat('run.sh')
    os.chmod('run.sh', st.st_mode | stat.S_IEXEC)

def create_app_requirements(api):
    app_reqs = api.create_app_requirements()
    with open('requirements.txt','w') as f:
        f.write(app_reqs)

def create_app_init(api):
    app_init = api.create_app_init()
    with open('__init__.py', 'w') as f:
        f.write(app_init)
    
def create_app(api):
    app = api.create_app()
    with open('app.py', 'w') as f:
        f.write(app)

def createApis(apisFiles):
    Create_Directory('apis')
    for api in apisFiles:
        with open('apis/'+api+'_api.py', 'w') as f:
            f.write(apisFiles[api])

def create_api_init(api):
    api_init = api.create_api_init()    
    with open('apis/__init__.py', 'w') as f:
        f.write(api_init)

Create_Application({
    11: 
    {'TableName': 'DEPARTMENT', 
    'TableType':'',
    'attributes': {'name': 'str', 
    'start_date': 'datetime',
    'EMPLOYEE_Manages': 'str'}, 
    'primaryKey': ['name'], 
    'ForgeinKey': [{'attributeName': 'EMPLOYEE_Manages',
    'ForignKeyTable': 'EMPLOYEE', 
    'ForignKeyTableAttributeName': 'ssn', 
    'patricipaction': 'partial', 
    'dataType': 'str'}], 
    'isWeak': False},
    34: 
    {'TableName': 'DEPARTMENT_Clocation', 
    'TableType':'',
    'attributes': {'Clocation': 'str',
    'DEPARTMENT_name': 'str'}, 
    'primaryKey': ['Clocation', 
    'DEPARTMENT_name'], 
    'ForgeinKey': [{'attributeName': 'DEPARTMENT_name', 
    'ForignKeyTable': 'DEPARTMENT', 
    'ForignKeyTableAttributeName': 'name', 
    'patricipaction': 'full', 
    'dataType': 'str'}], 
    'isWeak': False}, 
    12: 
    {'TableName': 'EMPLOYEE',
    'TableType':'',
    'attributes': {'last_name': 'str', 
    'middle_initis': 'str', 
    'first_name': 'str', 
    'address': 'str',
    'salary': 'float',
    'sex': 'str', 
    'status': 'str', 
    'birth_dat': 'str', 
    'ssn': 'str',
    'start_date': 'datetime',
    'DEPARTMENT_Employed_name': 'str',
    'EMPLOYEE_Supervision_': 'str'},
    'primaryKey': ['ssn'], 
    'ForgeinKey': [{'attributeName': 'DEPARTMENT_Employed_name',
    'ForignKeyTable': 'DEPARTMENT', 'ForignKeyTableAttributeName': 'name',
    'patricipaction': 'full', 'dataType': 'str'}, 
    {'attributeName': 'EMPLOYEE_Supervision_', 
    'ForignKeyTable': 'EMPLOYEE', 
    'ForignKeyTableAttributeName': 'ssn',
    'patricipaction': 'partial', 
    'dataType': 'str'}], 
    'isWeak': False},
    24: {'TableName': 'PROJECT', 
    'TableType':'',
    'attributes': {'location': 'str',
    'name': 'str', 
    'budget': 'float',
    'DEPARTMENT_Assigned_name': 'str'}, 
    'primaryKey': ['name'], 
    'ForgeinKey': [{'attributeName': 'DEPARTMENT_Assigned_name',
    'ForignKeyTable': 'DEPARTMENT', 
    'ForignKeyTableAttributeName': 'name',
    'patricipaction': 'partial', 
    'dataType': 'str'}], 
    'isWeak': False}, 
    25: 
    {'TableName': 'DEPENDENT',
    'TableType':'',
    'attributes': {'sex': 'str', 
    'relatlonship': 'str',
    'name': 'str',
    'birth_date': 'datetime', 
    'Dependents_EMPLOYEE_': 'str'}, 
    'primaryKey': ['Dependents_EMPLOYEE_'], 
    'ForgeinKey': [{'attributeName': 'Dependents_EMPLOYEE_', 
    'ForignKeyTable': 'EMPLOYEE', 
    'ForignKeyTableAttributeName': 'ssn', 
    'patricipaction': 'partial', 
    'dataType': 'str'}], 
    'isWeak': True}, 
    35: 
    {'TableName': 'Works_EMPLOYEE_PROJECT', 
    'TableType':'mTm',
    'attributes': {'start_date': 'datetime', 
    'hours': 'int', 
    'EMPLOYEE_': 'str', 
    'PROJECT_': 'str'}, 
    'primaryKey': ['EMPLOYEE_', 'PROJECT_'], 
    'ForgeinKey': [{'attributeName': 'EMPLOYEE_', 
    'ForignKeyTable': 'EMPLOYEE',
    'ForignKeyTableAttributeName': 'ssn', 
    'patricipaction': 'full',
    'dataType': 'str'}, 
    {'attributeName': 'PROJECT_',
    'ForignKeyTable': 'PROJECT', 
    'ForignKeyTableAttributeName': 'name',
    'patricipaction': 'full',
    'dataType': 'str'}], 
    'isWeak': False}})