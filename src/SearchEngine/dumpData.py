import pickle
import json
import globalVars 
from searchIndexer import *
from numpy import save , load
import os

def flatten_query_entities(listOfQueries):
    flattened_query_entities = []
    for query in listOfQueries:
        entities = []
        for entity in query['entities']:
            entities.extend(entity.split("_"))
        flattened_query_entities.append(entities)
    return flattened_query_entities

def getListQueries():
    listOfQueries=[]
    datapath = "/home/hager/college/GP/GP/notebooks/preparingDatasets/finalOutputs"
    files = os.listdir(datapath)
    for queryFile in files:
        if queryFile.find("synonyms")!=-1:
            continue
        with open(datapath+"/"+queryFile)as f:
            fileObj = json.load(f)
            for query in fileObj:
                if len(query["allQueries"])==1:
                    listOfQueries.extend(query["allQueries"])

    return listOfQueries


print("loading data")
#listOfQueries = getListQueries()
'''
##########load synanoms###########
with open('/home/hager/college/GP/GP/notebooks/preparingDatasets/finalOutputs/synonyms.json', 'rb') as file:
    vocab_words = json.load(file)
print("loading data done")
OneHotVocab = oneHotVocabEncoding(vocab_words)
print("creating one hot encoding done")

with open('/home/hager/college/GP/GP/src/SearchEngine/OneHotVocab.pickle', 'wb') as handle:
    pickle.dump(OneHotVocab, handle, protocol=pickle.HIGHEST_PROTOCOL)
print("saving one hot encoding done")
'''

globalVars.init()
OneHotVocab = globalVars.OneHotVocab
with open('/home/hager/college/GP/GP/notebooks/preparingDatasets/finalOutputs/synonyms.json', 'rb') as file:
    vocab_words = json.load(file)
print("loading data done")
OneHotVocab = oneHotVocabEncoding(vocab_words)

# flattened_query_entities = flatten_query_entities(listOfQueries)
# queriesMatrix = getQueriesMatrix(flattened_query_entities)
# #queriesMatrix = queriesMatrix.tolist()
# print("creating queries matrix done")
# with open('/home/hager/college/GP/GP/src/SearchEngine/queriesMatrix.npy', 'wb') as handle:
#     #pickle.dump(queriesMatrix, handle)
#     save(handle, queriesMatrix)
# print("saving queries matrix done")


 