import json
import pickle
from searchIndexer import oneHotVocabEncoding
path = "/home/nada/GP/GP/GP/src"
def init():
    global OneHotVocab
    with open(path+'/../notebooks/preparingDatasets/finalOutputs/synonyms.json','rb') as file:
        vocab_words = json.load(file)
        OneHotVocab = oneHotVocabEncoding(vocab_words)