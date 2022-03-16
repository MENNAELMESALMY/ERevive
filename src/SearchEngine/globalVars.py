import pickle
path = "/home/hager/college/GP/GP/src"
def init():
    global OneHotVocab
    with open(path+'/SearchEngine/OneHotVocab.pickle','rb') as file:
        OneHotVocab = pickle.load(file)