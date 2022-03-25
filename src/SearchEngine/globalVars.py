import json
import pickle
from searchIndexer import oneHotVocabEncoding
from joiner import constructGraph
path = "/home/nada/GP/GP/GP/src"
def init():
    global OneHotVocab
    global schemaGraph

    with open('/home/nada/GP/GP/GP/notebooks/preparingDatasets/finalOutputs/synonyms.json', 'rb') as file:
        vocab_words = json.load(file)
        print("loading data done")
        OneHotVocab = oneHotVocabEncoding(vocab_words)

    with open(path+'/TestSchemas/sportsSchema.pickle','rb') as file:
        schema = pickle.load(file)
        schemaGraph = constructGraph(schema)
    
