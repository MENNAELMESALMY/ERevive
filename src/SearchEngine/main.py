import json
import tracemalloc
from .queryConstruction import constructQuery, queryStructure
from .globalVars import *
import timeit
from collections import Counter
from .ranker import flatten_query_entities, getRankedQueries, mapToSchema,queryCoverage,mapAttrEntity,mapEntity,getListQueries,getNonZeroQueryHits,constructDictionary
from .clustering import *
from .searchIndexer import init_one_hot_vocab , cleanEntityName

def cleanQuery(query):
    cleaned_query = []
    for q in query:
        cleaned_entity = cleanEntityName(q)
        cleaned_query.extend(cleaned_entity)
    return cleaned_query



def getMappedQueries(schemaGraph,finalQueriesIndexs,listOfQueries,testSchema,entityDict,schemaEntityNames):
    queries = []
    start = timeit.default_timer()
    for idx in finalQueriesIndexs:
        mappedEntites, mappedAttributes, goals,mappedEntitesDict,bestJoin =  mapToSchema(schemaGraph,listOfQueries[idx],testSchema,entityDict,schemaEntityNames)
        print("mappedEntites: ",mappedEntites,mappedAttributes,goals,mappedEntitesDict,bestJoin)
        coverage = queryCoverage(mappedAttributes)
        query = constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,idx,goals,listOfQueries[idx],bestJoin,testSchema)
               
        queries.append(query)
        #print("mappedAttributes: ",mappedAttributes)
        #query = constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,compactness)
        #queries.append(query)
  
    end = timeit.default_timer()
    print("mapToSchema Time: ",end-start)
    # print("mappedAttributes: ",totalMappedAttributes , "totalAttributes: ",totalAttributes)
    # print("percentage: ",totalMappedAttributes/totalAttributes)
    # print(mappedEntites)
    # print(mappedAttributes)
    return queries



def outQueries(outFileQueries,outFileClusters,allQueries):
    finalClusters = []
    for cluster in allQueries:
        clusterQueries = []
        for query in cluster["queries"]:
            #print(query)
            clusterQueries.append([query,queryStructure(query),query["origQuery"]["query"]])
        finalClusters.append(clusterQueries)

    clusters = {}
    for i,c in enumerate(finalClusters):
        clusters["cluster#"+str(i)]=c


    with open(outFileQueries,'w') as file:
        jsonObj = json.dumps(clusters)
        file.write(jsonObj)
        clusters={}

    for i,c in enumerate(allQueries):
        clusters["cluster#"+str(i)]=c

    with open(outFileClusters,'w') as file:
        jsonObj = json.dumps(clusters)
        file.write(jsonObj)

        
def suggest_queries(testSchema):
    tracemalloc.start()
    print("Start Running: ",tracemalloc.get_traced_memory())

    print("loading data")
    listOfQueries = getListQueries()

    
    
    print("testSchema: ",tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
###########one hot encoding############
#with open(path+'/SearchEngine/OneHotVocab.pickle','rb') as file:
#    OneHotVocab = pickle.load(file)
    OneHotVocab,schemaGraph = init(testSchema)
    init_one_hot_vocab(OneHotVocab)

    tracemalloc.stop()
    tracemalloc.start()

#queriesMatrix = load(path+'/SearchEngine/queriesMatrix.npy')
#print("Query Matrix sample",queriesMatrix[10])
    flattened_query_entities = flatten_query_entities(listOfQueries)
    queriesMatrix = getQueriesMatrix(flattened_query_entities)
    print("Query Matrix size",queriesMatrix.shape)

    print("queriesMatrix: ",tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    ################get query hits#################

    schemaEntityNames = [testSchema[idx]["TableName"] for idx in testSchema.keys()]
    query = cleanQuery(schemaEntityNames) #Generated Keywords from shcema or KG //Future work
    queryOneHotVector = getKeyWordsVector(query).T
    queryHits = getQueryHits(queryOneHotVector,queriesMatrix)
 

    nonZeroQueriesIndexs = getNonZeroQueryHits(queryHits)
    tracemalloc.stop()

    entityDict = constructDictionary(testSchema)
    queries = getMappedQueries(schemaGraph,nonZeroQueriesIndexs,listOfQueries,testSchema,entityDict,schemaEntityNames)
    clusteredQueries = getClusteredQueries(queries)
    mergedClusters = getMergdClusters(clusteredQueries,queries)
    rankedQueries = getRankedQueries(mergedClusters,queries)
    outQueries("finalMergedQueries.json","finalMergedClusters.json",rankedQueries)
    rankedQueries = getRankedQueries(clusteredQueries,queries)
    outQueries("finalQueries.json","finalClusters.json",rankedQueries)


# handle alias nada,nihal
# * handle menna,hager
# consider ranking with attrs score  nada,nihal
# data  menna,hager
# api , handle final query validation nada,hager
# ui    menna,nihal


# synonyms // check comparing similarity
# appreviations

# evaluation





######################################
# unconnected components handle ----- done
# Query Matrix Json try ------ done
# more than one entity/attr mapping to the same entity/attr ---done
# optimize time and space if we can ---done
# Cache Joins ---done
# Self-loop ---delayed
# set max to cache size ---
######################################
# Data--------------------------
# Search for nested 
######################################
# exact Match discuss
# level 4 discuss
