import json
import os
import threading
from SearchEngine.main import getMappedQuery
from SearchEngine.queryConstruction import prepareQuery, queryStructure
from flask import Flask, request, jsonify
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
    "DEPARTMENT": {
        "TableName": "DEPARTMENT",
        "TableType": "",
        "attributes": {
            "EMPLOYEE_Manages_ssn": "str",
            "name": "str",
            "start_date": "datetime"
        },
        "primaryKey": [
            "name"
        ],
        "ForgeinKey": [
            {
                "attributeName": "EMPLOYEE_Manages_ssn",
                "ForignKeyTable": "EMPLOYEE",
                "ForignKeyTableAttributeName": "ssn",
                "patricipaction": "partial",
                "dataType": "str"
            }
        ],
        "isWeak": False
    },
    "EMPLOYEE": {
        "TableName": "EMPLOYEE",
        "TableType": "",
        "attributes": {
            "DEPARTMENT_Employed_name": "str",
            "EMPLOYEE_Supervision_ssn": "str",
            "address": "str",
            "ssn": "str",
            "birth_date": "str",
            "first_name": "str",
            "last_name": "str",
            "middle_initial": "str",
            "salary": "float",
            "sex": "str",
            "start_date": "datetime",
            "status": "str"
        },
        "primaryKey": [
            "ssn"
        ],
        "ForgeinKey": [
            {
                "attributeName": "DEPARTMENT_Employed_name",
                "ForignKeyTable": "DEPARTMENT",
                "ForignKeyTableAttributeName": "name",
                "patricipaction": "full",
                "dataType": "str"
            },
            {
                "attributeName": "EMPLOYEE_Supervision_ssn",
                "ForignKeyTable": "EMPLOYEE",
                "ForignKeyTableAttributeName": "ssn",
                "patricipaction": "partial",
                "dataType": "str"
            }
        ],
        "isWeak": False
    },
    "PROJECT": {
        "TableName": "PROJECT",
        "TableType": "",
        "attributes": {
            "DEPARTMENT_Assigned_name": "str",
            "name": "str",
            "budget": "float",
            "location": "str"
        },
        "primaryKey": [
            "name"
        ],
        "ForgeinKey": [
            {
                "attributeName": "DEPARTMENT_Assigned_name",
                "ForignKeyTable": "DEPARTMENT",
                "ForignKeyTableAttributeName": "name",
                "patricipaction": "partial",
                "dataType": "str"
            }
        ],
        "isWeak": False
    },
    "DEPENDENT": {
        "TableName": "DEPENDENT",
        "TableType": "",
        "attributes": {
            "sex": "str",
            "Dependents_EMPLOYEE_ssn": "str",
            "birth_date": "str",
            "name": "str",
            "relatlonship": "str"
        },
        "primaryKey": [
            "Dependents_EMPLOYEE_ssn",
            "name"
        ],
        "ForgeinKey": [
            {
                "attributeName": "Dependents_EMPLOYEE_ssn",
                "ForignKeyTable": "EMPLOYEE",
                "ForignKeyTableAttributeName": "ssn",
                "patricipaction": "partial",
                "dataType": "str"
            }
        ],
        "isWeak": True
    },
    "DEPARTMENT_location": {
        "TableName": "DEPARTMENT_location",
        "TableType": "",
        "attributes": {
            "location": "str",
            "DEPARTMENT_name": "str"
        },
        "primaryKey": [
            "location",
            "DEPARTMENT_name"
        ],
        "ForgeinKey": [
            {
                "attributeName": "DEPARTMENT_name",
                "ForignKeyTable": "DEPARTMENT",
                "ForignKeyTableAttributeName": "name",
                "patricipaction": "full",
                "dataType": "str"
            }
        ],
        "isWeak": False
    },
    "Works_EMPLOYEE_PROJECT": {
        "TableName": "Works_EMPLOYEE_PROJECT",
        "TableType": "",
        "attributes": {
            "EMPLOYEE_ssn": "str",
            "PROJECT_name": "str",
            "hours": "int",
            "start_date": "datetime"
        },
        "primaryKey": [
            "EMPLOYEE_ssn",
            "PROJECT_name"
        ],
        "ForgeinKey": [
            {
                "attributeName": "EMPLOYEE_ssn",
                "ForignKeyTable": "EMPLOYEE",
                "ForignKeyTableAttributeName": "ssn",
                "patricipaction": "full",
                "dataType": "str"
            },
            {
                "attributeName": "PROJECT_name",
                "ForignKeyTable": "PROJECT",
                "ForignKeyTableAttributeName": "name",
                "patricipaction": "full",
                "dataType": "str"
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


    
def start_creating_application(final_schema,clusters,user_name,password,db_name):
    os.chdir('Application')
    print("start creating application")
    Create_Application(final_schema,clusters,user_name,password,db_name)
    process = Process(target=lambda: os.system('python3 run.py &'))
    process.start()
    # os.chdir('api')
    # process = Process(target=lambda: os.system('python3 generate_data.py &'))
    # process.start()
    # os.chdir('./..')
    print("end creating application")
    os.chdir('./..')
    os.chdir('CreateFrontProject')
    process = Process(target=lambda: os.system('python3 run.py &'))
    process.start()
    os.chdir('./..') #src



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

    start_creating_application(finalSchema,clusters,systemData.get('databaseUsername'),systemData.get('databasePassword'),systemData.get('databaseName'))

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
    return jsonify({'message': '500 error'})


if __name__ == '__main__':
    app.run(port = 5000)
