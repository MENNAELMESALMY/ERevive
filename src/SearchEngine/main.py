import tracemalloc
from queryConstruction import constructQuery
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
with open(path+'/TestSchemas/sportsSchema.pickle','rb') as file:
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
query = ["coach","team","player"] #Generated Keywords from shcema or KG //Future work
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
    for idx in finalQueriesIndexs:
        mappedEntites, mappedAttributes, goals,mappedEntitesDict =  mapToSchema(listOfQueries[idx],testSchema,entityDict,schemaEntityNames)
        coverage = queryCoverage(mappedAttributes)
        compactness = queryCompactness(mappedEntites,goals)
        #query = constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,compactness)
        #queries.append(query)
    return queries
queries = getMappedQueries(nonZeroQueriesIndexs)
#clusteredQueries = getClusteredQueries(queries)
#mergedClusters = getMergdClusters(clusteredQueries,queries)
#start ranking