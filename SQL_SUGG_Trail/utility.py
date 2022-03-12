import re
import spacy
import numpy as np
#nlp = spacy.load('en_core_web_sm')

def get_lemma(text):
    doc = nlp(text)
    return doc[0].lemma_

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


def oneHotVocabEncoding(vocab):
    OneHotVocab = {}
    for idx,word in enumerate(vocab):
        OneHotVocab[word] = np.eye(vocab.shape[0])[idx].reshape(vocab.shape[0],1)
    return OneHotVocab

def getKeyWordsVector(keyWords,OneHotVocab):
    keyWordsVector = np.zeros((len(OneHotVocab),1))
    for word in keyWords:
        keyWordsVector += OneHotVocab[word]
    return keyWordsVector

def getQueriesMatrix(queriesKeywords,OneHotVocab):
    VocabSize = len(OneHotVocab)
    queriesNum = len(queriesKeywords)
    queriesMatrix = np.zeros((queriesNum,VocabSize))
    for idx,keyWords in enumerate(queriesKeywords):
        queriesMatrix[idx] = getKeyWordsVector(keyWords,OneHotVocab).reshape(VocabSize)
    return queriesMatrix.T

def getQueryHits(queryOneHotVector,queriesMatrix):
    queryHits = np.dot(queryOneHotVector,queriesMatrix)
    return queryHits[0]

def getTopKHitQueries(queryHits,k):
    queryIndices = (-queryHits).argsort()[:k]
    return queryIndices

entities= ['department', 'head', 'management',"CMP","TEST","Nada","Nihal","Menna","Hager","pp"]
entities = np.array(entities)
OneHotVocab = oneHotVocabEncoding(entities)
keywords = [["Menna","Hager"],["department","head"],["Nihal","Menna"]]
queriesMatrix = getQueriesMatrix(keywords,OneHotVocab)
query = ["Hager","department","head"]
queryOneHotVector = getKeyWordsVector(query,OneHotVocab).T
queryHits = getQueryHits(queryOneHotVector,queriesMatrix)
print(queryHits)
topK= getTopKHitQueries(queryHits,2)
print(topK)
#Mapping to schema
#Coverage
#Compactness => number of joins, joins distances
#N-grams
#Clustering