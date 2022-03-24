import re
#import spacy
import numpy as np
import globalVars
from nltk.stem import 	WordNetLemmatizer
from nltk import word_tokenize

#nlp = spacy.load('en_core_web_sm')

def get_lemma(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    tokenization = word_tokenize(text)
    if len(tokenization)==0:
        return text
    lemma = wordnet_lemmatizer.lemmatize(tokenization[0])
    return lemma

def camel_case_paskal_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

def cleanName(colName):
    #remove names with one character 
    if len(colName) <= 1: return colName
    #seperate pascal and camel cases
    Names = camel_case_paskal_split(colName)
    clean_Names=[]
    for name in Names:
      #remove names that are only numbers
      result = re.search("^[ 0-9]+$", name)
      if result is not None: continue
      #remove numbers at the end of the string 
      name = re.sub("[0-9]+$", '', name)
      #lower
      name = name.lower()
      lemma = get_lemma(name)
      clean_Names.append(lemma)
      
    return clean_Names
    
def cleanEntityName(entityName):
  entityName = entityName.strip()
  entityName = re.split('_| |-',entityName)
  entity_clean=[]
  for name in entityName:
    clean_name = cleanName(name)
    entity_clean.extend(clean_name)
  return entity_clean

# [
# 1 0 0 =>word1
# 0 1 0 =>word2             idx = 1
# 0 0 1 
# ]
def oneHotVocabEncoding(vocab):
    OneHotVocab = {}
    idx = 0
    # print(vocab.shape,"sh")
    for key,synList in vocab.items():
        synList.append(key)
        synList = np.array(synList)
        newWord = True
        for word in synList:
            if word in OneHotVocab.keys(): 
                newWord = False
                break
            oneHotVec = np.zeros(len(vocab.keys()))
            oneHotVec[idx] = 1.0
            OneHotVocab[word] = oneHotVec
        if newWord: idx+=1
        
    # Remove leading zeros
    for word,oneHotVector in OneHotVocab.items():
        OneHotVocab[word] = oneHotVector[:idx].reshape(idx,1)
    return OneHotVocab
    
def getKeyWordsVector(keyWords):
    OneHotVocab = globalVars.OneHotVocab
    uniqueValues = list(OneHotVocab.values())[0].shape[0]
    keyWordsVector = np.zeros((uniqueValues,1))
    for word in keyWords:
        if word not in OneHotVocab:
            continue
        keyWordsVector=  np.logical_or(OneHotVocab[word],keyWordsVector)
    return keyWordsVector*1.0

def getQueriesMatrix(queriesKeywords):
    OneHotVocab = globalVars.OneHotVocab
    VocabSize = list(OneHotVocab.values())[0].shape[0]
    queriesNum = len(queriesKeywords)
    queriesMatrix = np.zeros((queriesNum,VocabSize))
    for idx,keyWords in enumerate(queriesKeywords):
        queriesMatrix[idx] = getKeyWordsVector(keyWords).reshape(VocabSize)
    return queriesMatrix.T

def getQueryHits(queryOneHotVector,queriesMatrix):
    queryHits = np.dot(queryOneHotVector,queriesMatrix)
    return queryHits[0]

def getTopKHitQueries(queryHits,k):
    queryIndices = (-queryHits).argsort()[:k]
    return queryIndices

# entities= ['department', 'head', 'management',"CMP","TEST","Nada","Nihal","Menna","Hager","pp"]
# entities = np.array(entities)
# OneHotVocab = oneHotVocabEncoding(entities)
# keywords = [["Menna","Hager"],["department","head"],["Nihal","Menna"]]
# queriesMatrix = getQueriesMatrix(keywords,OneHotVocab)
# query = ["Hager","department","head"]
# queryOneHotVector = getKeyWordsVector(query,OneHotVocab).T
# queryHits = getQueryHits(queryOneHotVector,queriesMatrix)
# print("Hits",queryHits)
# topK= getTopKHitQueries(queryHits,2)
# print("topk indexes",topK)

#Mapping to schema
#Coverage
#Compactness => number of joins, joins distances
#N-grams
#Clustering