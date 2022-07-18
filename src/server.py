import json
import os
import threading
import time
import requests
from SearchEngine.main import getMappedQuery
from SearchEngine.queryConstruction import prepareQuery, queryStructure
from flask import Flask, request, jsonify ,send_file
from ImageProcessing import process_image
from flask_cors import CORS 
from SearchEngine import suggest_queries ,prepareClusters ,parse_query ,init_one_hot_vocab ,init
from Application import Create_Application
from NlpToSql.convertQuestionToQuery import convertNlpToSQLQuery
from sqlvalidator import parse
from multiprocessing import Process

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def run_image_processing(imgDir):
    os.chdir('ImageProcessing')
    out = []
    try:
        out = process_image(imgDir)
    except Exception as e:
        print(e)
    os.chdir('./..')
    #dump initial schema to file
    with open('common/outImageProcessing.json','w') as file:    
        jsonObj = json.dumps(out)
        file.write(jsonObj) 

def start_search_engine(final_schema):
    os.chdir('SearchEngine')
    queries, schemaGraph , testSchema , entityDict , schemaEntityNames = suggest_queries(final_schema.copy())
    os.chdir('./..')
    return queries, schemaGraph , testSchema , entityDict , schemaEntityNames


def updateNewQuery(query):
    try:
        queryValidator = parse(query)
        isValid = queryValidator.is_valid()
        if isValid:
            parsed_query = parse_query(query)
            return parsed_query
        else:
            raise Exception("Invalid query")
    except Exception as e:
        raise Exception(e)


dummy = {
        "document": {
            "TableName": "document",
            "TableType": "",
            "attributes": {
                "ID": "int",
                "course_has_course_number_id": "int",
                "name": "str",
                "url": "str"
            },
            "primaryKey": [
                "ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "course_has_course_number_id",
                    "ForignKeyTable": "course",
                    "ForignKeyTableAttributeName": "course_number_id",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "course": {
            "TableName": "course",
            "TableType": "",
            "attributes": {
                "Building_belong_to_ID": "int",
                "course_number_id": "int",
                "credit": "str",
                "department": "str",
                "description": "str",
                "subject_area": "str",
                "title": "str"
            },
            "primaryKey": [
                "course_number_id"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "Building_belong_to_ID",
                    "ForignKeyTable": "Building",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "course_section": {
            "TableName": "course_section",
            "TableType": "",
            "attributes": {
                "ID": "int",
                "Profile_uri": "str",
                "access_code": "str",
                "course_belongs_to_course_number_id": "int",
                "location": "str",
                "title": "str"
            },
            "primaryKey": [
                "ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "course_belongs_to_course_number_id",
                    "ForignKeyTable": "course",
                    "ForignKeyTableAttributeName": "course_number_id",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "Building": {
            "TableName": "Building",
            "TableType": "",
            "attributes": {
                "ID": "int",
                "address": "str",
                "country": "str",
                "fax": "str",
                "name": "str",
                "phone": "str",
                "picture_url": "str",
                "school_has_ID": "int",
                "website": "str"
            },
            "primaryKey": [
                "ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "school_has_ID",
                    "ForignKeyTable": "school",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "assignment": {
            "TableName": "assignment",
            "TableType": "",
            "attributes": {
                "ID": "int",
                "allow_comments": "int",
                "course_section_has_ID": "int",
                "description": "str",
                "due_date": "datetime",
                "grading_category": "str",
                "publish_date": "datetime",
                "remark": "str",
                "title": "str",
                "type": "str"
            },
            "primaryKey": [
                "ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "course_section_has_ID",
                    "ForignKeyTable": "course_section",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "school": {
            "TableName": "school",
            "TableType": "",
            "attributes": {
                "ID": "int",
                "address": "str",
                "country": "str",
                "fax": "str",
                "name": "str",
                "phone": "str",
                "picture_url": "str",
                "website": "str"
            },
            "primaryKey": [
                "ID"
            ],
            "ForgeinKey": [],
            "isWeak": False
        },
        "user": {
            "TableName": "user",
            "TableType": "",
            "attributes": {
                "Building_has_ID": "int",
                "ID": "int",
                "Password": "str",
                "email": "str",
                "first_name": "str",
                "garduation_date": "datetime",
                "gender": "str",
                "last_name": "str",
                "middle_name": "str",
                "name_titile_show": "str",
                "name_title": "str",
                "position": "int",
                "school_has_ID": "int",
                "username": "str"
            },
            "primaryKey": [
                "ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "Building_has_ID",
                    "ForignKeyTable": "Building",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                },
                {
                    "attributeName": "school_has_ID",
                    "ForignKeyTable": "school",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "Enrollment": {
            "TableName": "Enrollment",
            "TableType": "",
            "attributes": {
                "ID": "int",
                "Status": "str",
                "course_section_has_ID": "int",
                "date": "datetime",
                "is_admin": "bool",
                "user_has_ID": "int"
            },
            "primaryKey": [
                "ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "course_section_has_ID",
                    "ForignKeyTable": "course_section",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                },
                {
                    "attributeName": "user_has_ID",
                    "ForignKeyTable": "user",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "events": {
            "TableName": "events",
            "TableType": "",
            "attributes": {
                "ID": "int",
                "date": "datetime",
                "description": "str",
                "has_rsvp": "int",
                "is_all_day": "bool",
                "school_create_ID": "int",
                "title": "str",
                "type": "str",
                "user_create_ID": "int"
            },
            "primaryKey": [
                "ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "school_create_ID",
                    "ForignKeyTable": "school",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                },
                {
                    "attributeName": "user_create_ID",
                    "ForignKeyTable": "user",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "grade": {
            "TableName": "grade",
            "TableType": "",
            "attributes": {
                "of_Enrollment_ID": "int",
                "of_assignment_ID": "int",
                "comment": "int",
                "data": "str",
                "is_final": "bool",
                "value": "str"
            },
            "primaryKey": [
                "of_Enrollment_ID",
                "of_assignment_ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "of_assignment_ID",
                    "ForignKeyTable": "assignment",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                },
                {
                    "attributeName": "of_Enrollment_ID",
                    "ForignKeyTable": "Enrollment",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": True
        },
        "comment": {
            "TableName": "comment",
            "TableType": "",
            "attributes": {
                "date": "datetime",
                "text": "str"
            },
            "primaryKey": [
                "date"
            ],
            "ForgeinKey": [],
            "isWeak": True
        },
        "blog": {
            "TableName": "blog",
            "TableType": "",
            "attributes": {
                "date": "datetime",
                "is_closed": "bool",
                "text": "str",
                "title": "str",
                "user_writes_ID": "int"
            },
            "primaryKey": [
                "date"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "user_writes_ID",
                    "ForignKeyTable": "user",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": True
        },
        "attendence": {
            "TableName": "attendence",
            "TableType": "",
            "attributes": {
                "of_Enrollment_ID": "int",
                "remark": "str"
            },
            "primaryKey": [
                "of_Enrollment_ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "of_Enrollment_ID",
                    "ForignKeyTable": "Enrollment",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "partial",
                    "dataType": "int"
                }
            ],
            "isWeak": True
        },
        "course_section_meeting_days": {
            "TableName": "course_section_meeting_days",
            "TableType": "",
            "attributes": {
                "course_section_ID": "int",
                "meeting_days": "int"
            },
            "primaryKey": [
                "course_section_ID",
                "meeting_days"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "course_section_ID",
                    "ForignKeyTable": "course_section",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "full",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "course_section_class_periods": {
            "TableName": "course_section_class_periods",
            "TableType": "",
            "attributes": {
                "class_periods": "str",
                "course_section_ID": "int"
            },
            "primaryKey": [
                "class_periods",
                "course_section_ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "course_section_ID",
                    "ForignKeyTable": "course_section",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "full",
                    "dataType": "int"
                }
            ],
            "isWeak": False
        },
        "writes_user_comment_blog": {
            "TableName": "writes_user_comment_blog",
            "TableType": "",
            "attributes": {
                "blog_date": "datetime",
                "comment_date": "datetime",
                "user_ID": "int"
            },
            "primaryKey": [
                "blog_date",
                "comment_date",
                "user_ID"
            ],
            "ForgeinKey": [
                {
                    "attributeName": "user_ID",
                    "ForignKeyTable": "user",
                    "ForignKeyTableAttributeName": "ID",
                    "patricipaction": "full",
                    "dataType": "int"
                },
                {
                    "attributeName": "comment_date",
                    "ForignKeyTable": "comment",
                    "ForignKeyTableAttributeName": "date",
                    "patricipaction": "full",
                    "dataType": "datetime"
                },
                {
                    "attributeName": "blog_date",
                    "ForignKeyTable": "blog",
                    "ForignKeyTableAttributeName": "date",
                    "patricipaction": "full",
                    "dataType": "datetime"
                }
            ],
            "isWeak": False
        }
    }


# with open('CreateFrontProject/userInterfaceInfo.json','w') as file:
#     dummy_forms = json.load(file)


@app.route('/imageprocessing', methods=['POST'])
def get_image():
    rm_file = "rm -rf common/outImageProcessing.json"
    os.system(rm_file)
    imgFile = request.files.get('image')
    imgFile.save('assets/'+imgFile.filename)
    imgDir = '../assets/'+imgFile.filename
    thread = threading.Thread(target=run_image_processing, args=(imgDir,))
    thread.start()
    return jsonify({"image":imgFile.filename}) , 200    

@app.get('/ipoutput')
def get_ipoutput():
    if os.path.exists('common/outImageProcessing.json'):
        with open('common/outImageProcessing.json','r') as file:
            jsonObj = json.load(file)
            return jsonify(jsonObj)
    else:
        return jsonify({"error":"No output available"}) , 404

@app.post('/searchengine')
def get_search_engine():    
    finalSchema =request.json['schema'] # dummy
   
    rankedQueries, schemaGraph , testSchema , entityDict , schemaEntityNames = start_search_engine(finalSchema)
    clusters = []
    for cluster in rankedQueries:
        clusterQueries = []
        for query in cluster["queries"]:
            clusterQueries.append([query,queryStructure(query)]) 
        clusters.append(clusterQueries)
    finalClusters = prepareClusters(clusters,finalSchema)
    outClusters = {}


    for cluster in finalClusters:
        if len(cluster) == 0 or len(cluster[0]) == 0 or len(cluster[0][0]) == 0:
            continue
        outClusters[cluster[0][0]["cluster_name"]] = cluster   
    searchOut = {
        "testSchema":testSchema,
        "schemaGraph":schemaGraph,
        "entityDict":entityDict,
        "schemaEntityNames":schemaEntityNames,
        "clusters":outClusters
    }

    return jsonify(searchOut) , 200

import json
@app.post('/validate')
def get_validate():
    searchOut = request.json
    clusters = searchOut.get('clusters')
    finalSchema = searchOut.get('testSchema')
    schemaGraph = searchOut.get('schemaGraph')
    entityDict = searchOut.get('entityDict')
    os.chdir('SearchEngine')
    #print(searchOut)
    try:
        with open("finalSchema.json","w+") as file:
            json.dump(searchOut,file)
    except Exception as e:
        print(e)

    OneHotVocab,_ = init(finalSchema)
    init_one_hot_vocab(OneHotVocab)

    schemaEntityNames = searchOut.get('schemaEntityNames')
    clustersErrors = {}
    clustersUpdated = {}
    for cluster in clusters.values():
        if len(cluster)==0:
            continue
        clustersErrors[cluster[0][0]["cluster_name"]] = []
        updatedCluster = []
        for query in cluster:
            if query[0]["is_updated"]:
                #print("query[0]",query[0])
                endpoint_name = query[0]["ui_name"].replace(' ','_')
                name = {
                    "ui_name":query[0]["ui_name"],
                    "endpoint_name":endpoint_name,
                    "url":cluster[0][0]["cluster_name"]+"/"+endpoint_name
                }
                parsed_query = None
                try:
                    parsed_query = updateNewQuery(query[0]["query"])
                except Exception as e:
                    clustersErrors[cluster[0][0]["cluster_name"]].append(query)
                if parsed_query:
                    mappedQuery = getMappedQuery(schemaGraph,parsed_query,finalSchema,entityDict,schemaEntityNames)
                    constructedQuery = queryStructure(mappedQuery)
                    preparedQuery = prepareQuery([mappedQuery,constructedQuery],testSchema=finalSchema)
                    query = preparedQuery
                    #print(query[0])
                    query[0]["ui_name"] = name["ui_name"]
                    query[0]["endpoint_name"] = name["endpoint_name"]
                    query[0]["url"] = name["url"]
                    #print(query[0])
            updatedCluster.append(query)
        if len(clustersErrors[cluster[0][0]["cluster_name"]]) == 0:
            clustersErrors.pop(cluster[0][0]["cluster_name"])
        clustersUpdated[cluster[0][0]["cluster_name"]] = updatedCluster
    os.chdir('./..')
    if len(list(clustersErrors.keys())) != 0:
        return jsonify(clustersErrors) , 400
    return jsonify(clustersUpdated) , 200


    
def start_creating_application(final_schema,clusters,port,user_name,password,db_name):
    os.chdir('Application')
    print("start creating application")
    Create_Application(final_schema,clusters,user_name,password,db_name,port)
    process = Process(target=lambda: os.system('python3 run.py &'))
    process.start()
    print("end creating application")
    os.chdir('./..')
    os.chdir('CreateFrontProject')
    process = Process(target=lambda: os.system('python3 run.py &'))
    process.start()
    os.chdir('./..') #src


def check_port(port):
    try:
        requests.get('http://localhost:'+str(port))
        return True
    except:
        return False

@app.post('/application')
def get_application():
    forms = request.json.get('forms')
    systemData = request.json.get('systemData')
    clusters = request.json.get('clusters')
    finalSchema = request.json.get('testSchema')
    print("systemData",systemData)
    with open('CreateFrontProject/userInterfaceInfo.json','w+') as file:
        json.dump(forms,file)

    with open('CreateFrontProject/systemInfo.json','w+') as file:
        json.dump(systemData,file)

    start_creating_application(finalSchema,clusters,systemData.get('port'),systemData.get('databaseUsername'),systemData.get('databasePassword'),systemData.get('databaseName'))
    while not check_port(systemData.get('port')):
        time.sleep(5)
    
    return jsonify({"success":"success"}) , 200

@app.post('/nlptosql')
def get_nlptosql():
    os.chdir('NlpToSql')
    print("hello")
    query = request.json.get('query')
    finalSchema =request.json.get('finalSchema')
    finalQuery = convertNlpToSQLQuery(query,finalSchema)
    os.chdir('./..')
    return jsonify({"query":finalQuery}) , 200

@app.get('/umlimage')
def get_umlimage():
    image_name = "Application/api/generated_schema.png"
    return send_file(image_name, mimetype='image/png') , 200

@app.get('/')
def get_home():
    test = "SELECT DEPARTMENT_location.DEPARTMENT_name FROM DEPARTMENT_location WHERE DEPARTMENT_location.DEPARTMENT_name in value;"
    try:
        queryValidator = parse(test)
        isValid = queryValidator.is_valid()
        if isValid:
            print("Query is valid",queryValidator.__dict__)
            parsed_query = parse_query(test)
            print(parsed_query)
        else:
            print(queryValidator)
            raise Exception("Invalid query")
    except Exception as e:
        return jsonify({"error":str(e)}) , 400
    return jsonify({"success":"success"}) , 200


@app.route('/', methods=['OPTIONS'])
def options():
    return jsonify({'message': 'options'})

# catch all 500 errors
@app.errorhandler(500)
def internal_error(error):
    #check if current path is src
    if os.getcwd().split('/')[-1] != 'src':
        os.chdir('../')
    return jsonify({'message': '500 error'})


if __name__ == '__main__':
    app.run(port = 5000)
    