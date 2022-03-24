import tracemalloc
from queryConstruction import constructQuery,queryStructure
import globalVars
import timeit
from ranker import *
from clustering import *
tracemalloc.start()
print("Start Running: ",tracemalloc.get_traced_memory())

print("loading data")
listOfQueries = getListQueries()
path = globalVars.path

##########load schema###########
with open(path+'/TestSchemas/movieSchema.pickle','rb') as file:
    testSchema = pickle.load(file)
    
print("testSchema: ",tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
###########one hot encoding############
#with open(path+'/SearchEngine/OneHotVocab.pickle','rb') as file:
#    OneHotVocab = pickle.load(file)
globalVars.init()

OneHotVocab = globalVars.OneHotVocab 

#OneHotVocab = globalVars.OneHotVocab
print("OneHotVocab: ",tracemalloc.get_traced_memory())
tracemalloc.stop()
tracemalloc.start()
print("one hot encoding test",OneHotVocab["movie"].shape)
flattened_query_entities = flatten_query_entities(listOfQueries)
queriesMatrix = getQueriesMatrix(flattened_query_entities)
print("queriesMatric: ",tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
################get uery hits#################
query = ["movie","actor","director","award"] #Generated Keywords from shcema or KG //Future work
queryOneHotVector = getKeyWordsVector(query).T
queryHits = getQueryHits(queryOneHotVector,queriesMatrix)


nonZeroQueriesIndexs = getNonZeroQueryHits(queryHits)
tracemalloc.stop()

################calculate scores for top queries#################
schemaEntityNames = [testSchema[idx]["TableName"] for idx in testSchema.keys()]
entityDict = constructDictionary(testSchema)

def getMappedQueries(finalQueriesIndexs):
    queries = []
    print(len(finalQueriesIndexs))
    start = timeit.default_timer()
    for idx in finalQueriesIndexs:
        mappedEntites, mappedAttributes, goals,mappedEntitesDict,bestJoin =  mapToSchema(listOfQueries[idx],testSchema,entityDict,schemaEntityNames)
        coverage = queryCoverage(mappedAttributes)
        query = constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,idx,goals,listOfQueries[idx],bestJoin)
        queries.append(query)
    end = timeit.default_timer()
    print("mapToSchema Time: ",end-start)
    print("mappedAttributes: ",mappedAttributes , "totalAttributes: ",mappedEntites)
    # print("percentage: ",totalMappedAttributes/totalAttributes)
    # print(mappedEntites)
    # print(mappedAttributes)
    return queries
queries = getMappedQueries(nonZeroQueriesIndexs)
print(mapEntity.cache_info())
print(mapAttrEntity.cache_info())
# for q in queries:
#     print("###################################################")
#     print("query",q)
#     print(listOfQueries[q["id"]])
#     print("###################################################")
clusteredQueries = getClusteredQueries(queries)
mergedClusters = getMergdClusters(clusteredQueries,queries)
#rankedQueries = getRankedQueries(mergedClusters,queries)
rankedQueries = getRankedQueries(mergedClusters,queries)

print("ranked queries")
finalClusters = []
for cluster in rankedQueries:
    clusterQueries = []
    for query in cluster:
        clusterQueries.append(queryStructure(query))
        print(query)
        print("##################################")
    finalClusters.append(clusterQueries)

clusters = {}
outFile = "rankedQueries.txt"
for i,c in enumerate(finalClusters):
    clusters["cluster#"+str(i)]=c

with open(outFile,'w') as file:
    jsonObj = json.dumps(clusters)
    file.write(jsonObj)


#start ranking

######################################
# Cache Joins
# optimize time and space if we can
# unconnected components handle----- done
# Query Matrix Json try
# Self-loop 
# more than one entity/attr mapping to the same entity/attr
# level 4 
######################################
# Data--------------------------
# Search for nested 
