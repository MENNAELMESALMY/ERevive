from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
from collections import Counter
from scipy.sparse import csr_matrix
import math
import numpy as np

def IDF(corpus, unique_words):
  idf_dict={}
  N=len(corpus)
  for word in unique_words:
    count=0
    for topic in corpus:
      if word in topic:
        count=count+1
    idf_dict[word]=(math.log((N)/(count)))
  return idf_dict 

def TF_IDF(corpus,topics_names,idf_dict):
  topics_tfidf={}
  for j,topic in enumerate(corpus):
    topics_tfidf[topics_names[j]]={}
    for word in topic:
      if len(word)<=2:
        continue
      TF = topic.count(word)/len(topic)
      topics_tfidf[topics_names[j]].update({word:TF*(idf_dict[word])})
    #Normalize
    sum_t = sum(topics_tfidf[topics_names[j]].values())
    topics_tfidf[topics_names[j]] = { w:t/sum_t for w,t in topics_tfidf[topics_names[j]].items()}
  return topics_tfidf
def getUniqueWords(corpus):
  unique_words=set()
  for topic in corpus:
    for word in topic:
      unique_words.add(word)
  return unique_words




#######TESTING############
# current_topic =topics_tfidf[2]
# keys = list(current_topic.keys())
# xs = current_topic.values()
# ys = range(len(xs))
# plt.figure(figsize=(50,50), dpi= 100, facecolor='w', edgecolor='k')
# plt.scatter(xs, ys)
# plt.xlabel('tf-idf')
# plt.ylabel('words')
# # zip joins x and y coordinates in pairs
# for x,y in zip(xs,ys):

#     label = keys[y]
    
#     plt.annotate(label, # this is the text
#                  (x,y), # these are the coordinates to position the label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,5), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center
# plt.show()