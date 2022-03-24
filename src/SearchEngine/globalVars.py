import pickle
from joiner import constructGraph
path = "/home/hager/college/GP/GP/src"
def init():
    global OneHotVocab
    global schemaGraph

    with open(path+'/SearchEngine/OneHotVocab.pickle','rb') as file:
        OneHotVocab = pickle.load(file)

    with open(path+'/TestSchemas/sportsSchema.pickle','rb') as file:
        schema = pickle.load(file)
        schemaGraph = constructGraph(schema)
    
