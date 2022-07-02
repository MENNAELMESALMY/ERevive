import json
import pickle
from .searchIndexer import oneHotVocabEncoding
from .joiner import constructGraph
OneHotVocab = {}
schemaGraph = {}
def init(testSchema):
    global OneHotVocab
    global schemaGraph

    with open('../../notebooks/preparingDatasets/finalOutputs/synonyms.json', 'rb') as file:
        vocab_words = json.load(file)
        print("loading data done")
        OneHotVocab = oneHotVocabEncoding(vocab_words)

    schemaGraph = constructGraph(testSchema)
    return OneHotVocab ,schemaGraph
    
