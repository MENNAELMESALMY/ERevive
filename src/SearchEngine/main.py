import json
import tracemalloc
from .queryConstruction import constructQuery, prepareClusters, queryStructure
from .globalVars import *
import timeit
from collections import Counter
from .ranker import rankQueriesSimilarities,flatten_query_entities, getRankedQueries, mapToSchema,queryCoverage,mapAttrEntity,mapEntity,getListQueries,getNonZeroQueryHits,constructDictionary
from .clustering import *
from .searchIndexer import init_one_hot_vocab , cleanEntityName

def cleanQuery(query):
    cleaned_query = []
    for q in query:
        cleaned_entity = cleanEntityName(q)
        cleaned_query.extend(cleaned_entity)
    return cleaned_query



def getMappedQueries(schemaGraph,rankedQueriesBySimilarity,testSchema,entityDict,schemaEntityNames):
    queries = []
    start = timeit.default_timer()
    for q in rankedQueriesBySimilarity:
        mappedEntites, mappedAttributes, goals,mappedEntitesDict,bestJoin =  mapToSchema(schemaGraph,q[0],testSchema,entityDict,schemaEntityNames)
        coverage = queryCoverage(mappedAttributes)
        query = constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,goals,q[0],bestJoin)
               
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
    nonZeroQueries = []
    quiries_keywords = []
    entities_keywords = list(set(query)) 
    for idx in nonZeroQueriesIndexs:
        query = listOfQueries[idx]
        nonZeroQueries.append(query)    
        entities = query["entities"]
        selectAttrs = [attr.split('.')[-1] for attr in query["selectAttrs"]]
        whereAttrs = [attr[0].split('.')[-1] for attr in query["whereAttrs"]]
        keywords = []
        keywords.extend(cleanQuery(entities))
        keywords.extend(cleanQuery(selectAttrs))
        keywords.extend(cleanQuery(whereAttrs))
        keywords = list(set(keywords))
        quiries_keywords.append(keywords)
    
    rankedQueriesBySimilarity = rankQueriesSimilarities(quiries_keywords,nonZeroQueries,entities_keywords)
    with open('rank_queries_similarities.json','w') as file:
        jsonObj = json.dumps(rankedQueriesBySimilarity)
        file.write(jsonObj)

 
    tracemalloc.stop()

    entityDict = constructDictionary(testSchema)
    queries = getMappedQueries(schemaGraph,rankedQueriesBySimilarity,testSchema,entityDict,schemaEntityNames)
    with open('getMappedQueries.json','w') as file:
        jsonObj = json.dumps(queries)
        file.write(jsonObj)
    clusteredQueries = getClusteredQueries(queries)

    finalClusters = []
    for cluster in clusteredQueries:
        clusterQueries = []
        for idx in cluster:
            query = queries[idx]
            clusterQueries.append([query,queryStructure(query),query["origQuery"]["query"]])
        finalClusters.append(clusterQueries)
    with open('clusteredQueries.json','w') as file:
        jsonObj = json.dumps(finalClusters)
        file.write(jsonObj)

    #mergedClusters = getMergdClusters(clusteredQueries,queries,testSchema)
    #mergedClusters = getMergdClusters(mergedClusters,queries,testSchema)
    
    rankedQueries = getRankedQueries(clusteredQueries,queries)
    outQueries("finalMergedQueries.json","finalMergedClusters.json",rankedQueries)

    


    return rankedQueries , schemaGraph , testSchema , entityDict , schemaEntityNames

def getMappedQuery(schemaGraph,query,testSchema,entityDict,schemaEntityNames):
    mappedEntites, mappedAttributes, goals,mappedEntitesDict,bestJoin =  mapToSchema(schemaGraph,query,testSchema,entityDict,schemaEntityNames)
    coverage = queryCoverage(mappedAttributes)
    query = constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,goals,query,bestJoin)
    return query
    

    


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
