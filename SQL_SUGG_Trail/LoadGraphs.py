import pickle
from SchemaGraph import *

def saveTopic(topic_name,topic):
  file_to_store = open('topics_pickles/'+topic_name+".pickle", "wb")
  pickle.dump(topic, file_to_store)
  file_to_store.close()
   
def loadTopic(topic_name):
  file_to_load = open('topics_pickles/'+topic_name+".pickle", "rb")
  topic = pickle.load(file_to_load)
  return topic 
