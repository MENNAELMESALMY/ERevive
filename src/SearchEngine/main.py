import tracemalloc
import globalVars
import timeit
from ranker import *

tracemalloc.start()
print("Start Running: ",tracemalloc.get_traced_memory())

print("loading data")
listOfQueries = getListQueries()
path = "/home/hager/college/GP/GP/src"

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
with open(path+'/SearchEngine/queriesMatrix.pickle','rb') as file:
    queriesMatrix = pickle.load(file)
print("queriesMatric: ",tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
################get uery hits#################
query = ["coach","team","player"] #Generated Keywords from shcema or KG //Future work
queryOneHotVector = getKeyWordsVector(query).T
queryHits = getQueryHits(queryOneHotVector,queriesMatrix)
countNonZero = sum([1 for i in queryHits if i!=0])
#print("nozero",countNonZero,"total",len(queryHits))
#print("queryHits",queryHits)
topK = getTopKHitQueries(queryHits,3000)
print("topK",topK)
for i in topK:
    print(queryHits[i],listOfQueries[i]["entities"],listOfQueries[i]["selectAttrs"])

#print("TopK: ",tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
################calculate scores for top queries#################
schemaEntityNames = [testSchema[idx]["TableName"] for idx in testSchema.keys()]
entityDict = constructDictionary(testSchema)

start = timeit.default_timer()
for i in topK:
    # print('------------------------------------')

    #start = timeit.default_timer()
    mappedEntites, mappedAttributes, goals =  mapToSchema(listOfQueries[i],testSchema,entityDict,schemaEntityNames)
    #end = timeit.default_timer()
    #print("mapToSchema Time: ",end-start)

    coverage = queryCoverage(mappedAttributes)
    compactness = queryCompactness(mappedEntites,goals)
    # print("returnedQuery",listOfQueries[i]["query"])
    # print("mappedEntites",mappedEntites)
    # print("goals",goals)
    # print("mappedAttributes",mappedAttributes)
    # print("coverage: ",coverage)
    # print("compactness: ",compactness)
end = timeit.default_timer()
print("//////////////////////////////")
print("TopK Time: ",end-start)
print("Cache Info",mapEntity.cache_info())
print("//////////////////////////////")

print("mapping: ",tracemalloc.get_traced_memory())
tracemalloc.stop()