from re import L
import sys
import threading

from click import progressbar
from searchIndexer import *
from joiner import *
import os
import json
import pickle

def mapEntities(query,schema,OneHotVocab):
    mappedEntites = []
    for entityKeywords in query['entities']:
        #print("entityKeywords",entityKeywords)
        entityKeywords = entityKeywords.split("_")
        MaxMatchScore,MatchedWord,MatchedKey  = 0,None,None
        for key in schema.keys():
            cleanName = cleanEntityName(schema[key]['TableName'])
            matchScore = getMatchScore(entityKeywords,cleanName,OneHotVocab)
            if matchScore > MaxMatchScore:
                MaxMatchScore = matchScore
                MatchedWord = cleanName
                MatchedKey = key
        if MatchedWord is not None:
            mappedEntites.append((MatchedKey,MatchedWord,MaxMatchScore,entityKeywords))

    return mappedEntites

def getMatchScore(queryWords,schemaWords,OneHotVocab):
    # matchedWords / max(len(queryWords),len(schemaWords))
    queryVector = getKeyWordsVector(queryWords,OneHotVocab)
    schemaVector = getKeyWordsVector(schemaWords,OneHotVocab)
    matchCount = np.dot(queryVector.T, schemaVector)
    matchScore = matchCount[0][0]/max(len(queryWords),len(schemaWords))
    return matchScore

def flatten_query_entities(listOfQueries):
    flattened_query_entities = []
    for query in listOfQueries:
        entities = []
        for entity in query['entities']:
            entities.extend(entity.split("_"))
        flattened_query_entities.append(entities)
    return flattened_query_entities

def constructDictionary(schema):
    entityDict = {}
    for key in schema.keys():
        entityDict[schema[key]["TableName"]] = key
    return entityDict

def mapAttr(entities , attribute , entityDict, schema):
    attribute = cleanEntityName(attribute)
    MaxMatchScore,MatchedWord,MatchedEntityName  = 0,None,None
    for entityName in entities:
        idx = entityDict[entityName]
        for attr in schema[idx]["attributes"].keys():
            matchScore = getMatchScore(attribute,cleanEntityName(attr),OneHotVocab)
            if matchScore > MaxMatchScore:
                MaxMatchScore = matchScore
                MatchedWord = attr
                MatchedEntityName = entityName
    if MatchedWord is not None:
        return (MatchedEntityName,MatchedWord,MaxMatchScore,attribute)
    return None

def mapToSchema(query,schema,OneHotVocab):
    entityDict = constructDictionary(schema)

    mappedEntites = mapEntities(query,schema,OneHotVocab)
    #print("mappedEntites",mappedEntites)
    mappedEntitesDict = {'_'.join(v):schema[k]["TableName"] for k,_,_,v in mappedEntites}

    mappedEntitesNames = [schema[idx]["TableName"] for idx,_,_,_ in mappedEntites]
    #print("mappedEntitesNames",mappedEntitesNames)
    bestJoin , goals = connectEntities(schema,mappedEntitesNames)
    #print(mappedEntitesNames)
    #print(goals)

    '''
    select s.name , s.age , a.name , a.age , a.address
    from student s , address a

    mapAttr([student],[name,age])
    mapAttr([address],[name,age,address])

    
    check for . if true
    same entity => in search
    if successful => break
    if not
        entities in mapped => if successful => break
        if not:
            entities goals_joins => if successful => break
            if not:
                search => schema if successful => break
                if not return None
    '''
    
    mappedAttributes = []
    #print("mappedEntitesDict",mappedEntitesDict)
    for attribute in query['selectAttrs']:
        
        goals_copy = goals.copy()
        schemaEntities = {schema[idx]["TableName"] for idx in schema.keys()}

        #level 1
        if '.' in attribute:
            entity = attribute.split('.')[0]
            if entity in mappedEntitesDict.keys(): 
                entity = mappedEntitesDict[entity]
                attribute = attribute.split('.')[1]
                
                mapping = mapAttr([entity],attribute,entityDict,schema)
                if mapping is not None:
                    mappedAttributes.append(mapping)
                    continue
            #else: print(f"This Alias entity '{entity}' did not exist")
            goals_copy.discard(entity) #discard searched entity
            schemaEntities.discard(entity) #discard searched entity
            
        #level 2
        entities = {entity for _,entity in mappedEntitesDict.items()}
        mapping = mapAttr(entities,attribute,entityDict,schema)
        if mapping is not None:
            mappedAttributes.append(mapping)
            continue
        goals_copy = goals_copy - entities 
        schemaEntities = schemaEntities - entities

        #level 3
        #print("goals",goals_copy)
        mapping = mapAttr(goals_copy,attribute,entityDict,schema)
        if mapping is not None:
            mappedAttributes.append(mapping)
            continue
        #schemaEntities = schemaEntities - goals_copy

        # #level 4
        # TO BE DISCUSSED
        # mapping = mapAttr(schemaEntities,attribute,entityDict,schema)
        # if mapping is not None:
        #     mappedAttributes.append(mapping)
        #     continue

        mappedAttributes.append((None,None,0,attribute))

    return mappedEntites,mappedAttributes,goals,mappedEntitesDict


def queryCoverage(mappedAttributes):
    found = sum([1 for entity,_,_,_ in mappedAttributes if entity is not None])
    attributesMapped = max(len(mappedAttributes),1)
    return found/attributesMapped

def queryCompactness(mappedEntitiesDict,goals):
    mappedEntites = max(len(goals) ,1)
    compactness = len(mappedEntitiesDict)/mappedEntites
    return compactness

def getListQueries():
    listOfQueries=[]
    datapath = "/home/nada/GP/GP/GP/notebooks/preparingDatasets/finalOutputs"
    files = os.listdir(datapath)
    for queryFile in files:
        if queryFile.find("synonyms")!=-1:
            continue
        with open(datapath+"/"+queryFile)as f:
            fileObj = json.load(f)
            for query in fileObj:
                listOfQueries.extend(query["allQueries"])

    return listOfQueries


# listOfQueries =[
#                     {
#                         "entities":[ #one query with two entities
#                             ["employee"],
#                             ["department"] 
#                         ],
#                         "selectAttrs":["salary","employee.status","department.name"],
#                     },
#                     {
#                         "entities":[ #one query with two entities 
#                             ["employee"],
#                             ["project"]
#                             #["work","employee","project"],
#                         ],
#                         "selectAttrs":["employee.sex","employee.first_name","EMPLOYEE_Manages"],    
#                     },
#                     {
#                         "selectAttrs":[ #one query with two entities
#                             ["student"],
#                             ["instructor"]
#                         ],
#                         "selectAttrs":["student.name","student.age","instructor.name"],
#                     }    
#                 ]

print("loading data")

listOfQueries = getListQueries()

##########load schema###########
with open('/home/nada/GP/GP/GP/src/SearchEngine/testSchema.pickle','rb') as file:
    testSchema = pickle.load(file)
    #print("testSchema",testSchema)

##########load synanoms###########
with open('/home/nada/GP/GP/GP/notebooks/preparingDatasets/finalOutputs/synonyms.json', 'rb') as file:
   vocab_words = json.load(file)
   #print("vocab type",type(vocab_words))
   
##########clean vocab###########
# vocab_words = [
#                 "teacher":["instructor"],\
#                 ["work","ball"],\
#                 ["company","department","startup"],\
#                 "employee":["project"],["salary"],["status"]]
    
###########one hot encoding############
#print("vocab_words",vocab_words)
OneHotVocab = oneHotVocabEncoding(vocab_words)
print("one hot encoding test",OneHotVocab["movie"].shape)
# for entitySyn in vocab_words:
#     print("----------entity----------")
#     for entity in entitySyn:
#         print(OneHotVocab[entity].T)
flattened_query_entities = flatten_query_entities(listOfQueries)
queriesMatrix = getQueriesMatrix(flattened_query_entities,OneHotVocab)
#print("queriesMatrix",queriesMatrix)

################get uery hits#################
query = ["department","employee"] #Generated Keywords from shcema or KG //Future work
queryOneHotVector = getKeyWordsVector(query,OneHotVocab).T
queryHits = getQueryHits(queryOneHotVector,queriesMatrix)
countNonZero = sum([1 for i in queryHits if i!=0])
print("nozero",countNonZero,"total",len(queryHits))
print("queryHits",queryHits)

################get final query hits#################



# clusters=[]
# for cluster in clusteredQueries:
#     #create new thread for each cluster
#     #sort cluster by queryHits
#     cluster = sorted(cluster,key=lambda x:queryHits[x],reverse=True)
#     #take top 100 queries
#     cluster = cluster[:100]
#     clusters.append(cluster)
def flattenList(listOfLists):
    return [item for sublist in listOfLists for item in sublist]

def getNonZeroQueryHits(queryHits):
    nonZeroQueryHits = [ idx for idx,q in enumerate(queryHits) if q!=0]
    return nonZeroQueryHits


nonZeroQueriesIndexs = getNonZeroQueryHits(queryHits)
########################query construction####################
def constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes):
    query = {}
    query["entities"] = [ent for ent in mappedEntitesDict.values()]
    query["cleanedEntities"] = [ent[1] for ent in mappedEntites]
    query["selectAttrs"] = []
    for attr in mappedAttributes:
        if attr[1] is not None:
            query["selectAttrs"].append(attr[0]+"."+attr[1] if attr[0] is not None else attr[1])
    return query


################calculate scores for non zeros queries#################

def getMappedQueries(finalQueries):
    #clusterThreadName = threading.current_thread().name
    #print("clusterThreadName",clusterThreadName,len(cluster))
    #allClustersQueries[clusterThreadName] = []
    queries = []
    for i in finalQueries:
        #print('------------------------------------')
        mappedEntites, mappedAttributes, goals,mappedEntitesDict =  mapToSchema(listOfQueries[i],testSchema,OneHotVocab)
        coverage = queryCoverage(mappedAttributes)
        compactness = queryCompactness(mappedEntites,goals)

        queries.append(constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes))
        ##print("goals",goals)
        ##print("mappedEntites",mappedEntites)
        ##print("mappedAttributes",mappedAttributes)
        ##print("coverage: ",coverage)
        ##print("compactness: ",compactness)

        #allClustersQueries[clusterThreadName].append([mapEntities,mappedEntites,mappedAttributes,coverage,compactness])
    return queries
queries = getMappedQueries(nonZeroQueriesIndexs)
########################clustering############################

def getClusteredQueries(queries):
    clusteredQueries = {}
    for i,query in enumerate(queries):
        queryEntityKey = getKeyWordsVector(flattenList(query["cleanedEntities"]),OneHotVocab)
        if clusteredQueries.get((queryEntityKey.T).tostring()) is None: #if key not exist
            clusteredQueries[(queryEntityKey.T).tostring()] = [i]
        else:
            clusteredQueries[(queryEntityKey.T).tostring()].append(i)
    return list(clusteredQueries.values())

def getUniqueSelectAttrs(attrs):
    selectAttrs = []
    outAttrs=[]
    attrsCleaned = [re.split(r"[.|_]",attr) for attr in attrs]
    for i,attr in enumerate(attrsCleaned):
        attrOneHot = getKeyWordsVector(attr,OneHotVocab)
        if attrOneHot.tostring() not in selectAttrs:
            selectAttrs.append(attrOneHot.tostring())
            outAttrs.append(attrs[i])
    return outAttrs
def getMergdClusters(clusteredQueries,queries):
    mergedClusters = []
    for cluster in clusteredQueries:
        mergedQueries = {}
        newCluster = []
        for i in cluster:
            query = queries[i]
            #Todo : Check if where condition is same for merging , should split on _
            queryWhereKey = flattenList([re.split(r"[.|_]",q) for q in query["whereAttrs"]])
            queryGroupKey = flattenList([re.split(r"[.|_]",q) for q in query["groupByAttrs"]])
            queryOrderKey = flattenList([re.split(r"[.|_]",q[0]) for q in query["orderByAttrs"]])
            queryKeys = queryWhereKey+queryGroupKey+queryOrderKey
            queryKeysVector = getKeyWordsVector(queryKeys,OneHotVocab)

            if mergedQueries.get((queryKeysVector.T).tostring()) is None: #if key not exist
                mergedQueries[(queryKeysVector.T).tostring()] = [i]
            else:
                mergedQueries[(queryKeysVector.T).tostring()].append(i)

        mergedQueries = list(mergedQueries.values())
        for whereCluster in mergedQueries:
            selectAttrs = []
            for i in whereCluster:
                query = queries[i]
                selectAttrs.extend(query["selectAttrs"])
            #selectAttrs = getUniqueSelectAttrs(selectAttrs)
            selectAttrs = list(set(selectAttrs))
            queries[whereCluster[0]]["selectAttrs"] = selectAttrs
            newCluster.append(whereCluster[0])  
        mergedClusters.append(newCluster)
    return mergedClusters

clusteredQueries = getClusteredQueries(queries)
#mergedClusters = getMergdClusters(clusteredQueries,queries)



#def startClusterThreads(clusters):
    #clustersThreads = []
    #for cluster in clusters:
    #    getClusterFeatures(cluster)
    ##    clusterThread = threading.Thread(target=getClusterFeatures,args=(cluster,))
    ##    clustersThreads.append(clusterThread)
    #for clusterThread in clustersThreads:
    ##clustersThreads[0].start()
    #for clusterThread in clustersThreads:
    ##clustersThreads[0].join()
#startClusterThreads(clusters)

###################################################### ranker should be done after clustering ######################################################
#topK = getTopKHitQueries(queryHits,100)
#print("topK",topK)
#for i in topK:
#    print(queryHits[i],listOfQueries[i]["entities"],listOfQueries[i]["selectAttrs"])





#ranking
#Mapping to schema
#entities, attribute
#Map Entities ==> Joins

#Map Attributes in Select ==> which table in FROM 
#remove attribute

#Coverage 
#Compactness => number of joins, joins distances # entities count in returned query and entities count in mapped query
#N-grams
#correlation between queries
#-------------------------------------------------
#query optimization ===> No Redunduncy
#Clustering

##########Archive############
#====2 search all schema
#add table in From, where clause
#Map Attributes in where Clause ==>conditins not joins