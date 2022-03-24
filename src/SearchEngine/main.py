import tracemalloc
from queryConstruction import constructQuery
import globalVars
import timeit
from collections import Counter
from ranker import mapToSchema,queryCoverage,mapAttrEntity,mapEntity,getListQueries,getNonZeroQueryHits,constructDictionary
from clustering import *
from numpy import load

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

queriesMatrix = load(path+'/SearchEngine/queriesMatrix.npy')
print("Query Matrix sample",queriesMatrix[10])
print("Query Matrix size",queriesMatrix.shape)

print("queriesMatrix: ",tracemalloc.get_traced_memory())
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
    print("num of queries",len(finalQueriesIndexs))
    start = timeit.default_timer()
    countNone = 0
    totalAttr =0
    countOfMapping = 0
    countEntities = 0
    for idx in finalQueriesIndexs:
        mappedEntites, mappedAttributes, goals,mappedEntitesDict,bestJoin =  mapToSchema(listOfQueries[idx],testSchema,entityDict,schemaEntityNames)
        print(bestJoin)
        countEntities+= len(listOfQueries[idx]["entities"])
        l = [a for (_,a,_,_) in mappedAttributes]
        counts = Counter(l)
        counts[None] = 1
        #print(counts)
        countOfMapping += sum(a for a in counts.values() if a>1)
        queries.append({"query":listOfQueries[idx],"mappedEntites":mappedEntites,"mappedAttributes":mappedAttributes,"goals":goals,"mappedEntitesDict":mappedEntitesDict})
        #print("mappedAttributes: ",mappedAttributes)
        for m in mappedAttributes:
            totalAttr +=1
            if m[0] is None:
                countNone += 1
        coverage = queryCoverage(mappedAttributes)
        #query = constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,compactness)
        #queries.append(query)
    print("entitiesCount",countEntities)
    print("countofMapping",countOfMapping)
    print("countNone",countNone)
    print("totalAttr",totalAttr)
    end = timeit.default_timer()
    print("mapToSchema Time: ",end-start)
    # print("mappedAttributes: ",totalMappedAttributes , "totalAttributes: ",totalAttributes)
    # print("percentage: ",totalMappedAttributes/totalAttributes)
    # print(mappedEntites)
    # print(mappedAttributes)
    return queries
queries = getMappedQueries(nonZeroQueriesIndexs)
print("mapEntity",mapEntity.cache_info())
print("mapAttr",mapAttrEntity.cache_info())
print("join",connectEntities.cache_info())

# clusteredQueries = getClusteredQueries(queries)
# mergedClusters = getMergdClusters(clusteredQueries,queries)

#start ranking

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