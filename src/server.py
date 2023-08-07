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
    with open('ImageProcessing/outImageProcessing.json','w') as file:    
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




@app.route('/imageprocessing', methods=['POST'])
def get_image():
    rm_file = "rm -rf ImageProcessing/outImageProcessing.json"
    os.system(rm_file)
    imgFile = request.files.get('image')
    imgFile.save('ImageProcessing/input/'+imgFile.filename)
    imgDir = 'input/'+imgFile.filename
    thread = threading.Thread(target=run_image_processing, args=(imgDir,))
    thread.start()
    return jsonify({"image":imgFile.filename}) , 200    

@app.get('/ipoutput')
def get_ipoutput():
    if os.path.exists('ImageProcessing/outImageProcessing.json'):
        with open('ImageProcessing/outImageProcessing.json','r') as file:
            jsonObj = json.load(file)
            return jsonify(jsonObj)
    else:
        return jsonify({"error":"No output available"}) , 404

@app.post('/searchengine')
def get_search_engine():    
    finalSchema =request.json['schema'] 
   
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
                    query[0]["ui_name"] = name["ui_name"]
                    query[0]["endpoint_name"] = name["endpoint_name"]
                    query[0]["url"] = name["url"]
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
    Create_Application(final_schema,clusters,user_name,password,db_name,port)
    process = Process(target=lambda: os.system('python3 run.py &'))
    process.start()
    os.chdir('./..')
    os.chdir('CreateFrontProject')
    process = Process(target=lambda: os.system('python3 run.py &'))
    process.start()
    os.chdir('./..')


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
    query = request.json.get('query')
    finalSchema = request.json.get('finalSchema')
    finalQuery = convertNlpToSQLQuery(query,finalSchema)
    os.chdir('./..')
    return jsonify({"query":finalQuery}) , 200

@app.get('/umlimage')
def get_umlimage():
    image_name = "Application/api/generated_schema.png"
    return send_file(image_name, mimetype='image/png') , 200

@app.get('/')
def get_home():
    return jsonify({"success":"success"}) , 200


@app.route('/', methods=['OPTIONS'])
def options():
    return jsonify({'message': 'options'})

# catch all 500 errors
@app.errorhandler(500)
def internal_error(error):
    if os.getcwd().split('/')[-1] != 'src':
        os.chdir('../')
    return jsonify({'message': '500 error'})


if __name__ == '__main__':
    app.run(port = 5000)
    