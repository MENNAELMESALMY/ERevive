import itertools
from re import L
import sys
# import threading
from searchIndexer import *
from joiner import *
# import globalVars
import os
import json
import timeit
import pickle
from utilities import *

from functools import lru_cache

def getListQueries():
    listOfQueries=[]
    datapath = "/home/nada/GP/GP/GP/notebooks/preparingDatasets/finalOutputs"
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

@lru_cache(maxsize=None)
def mapEntity(entityKeywords,schemaEntityNames):
    #print("mapEntity",entity,schemaEntityNames)
    entityKeywordsSplit = entityKeywords.split("_")
    MaxMatchScore,MappedEntity  = 0,None
    for entity in schemaEntityNames:
        cleanName = cleanEntityName(entity)
        matchScore = getMatchScore(entityKeywordsSplit,cleanName)
        if matchScore > MaxMatchScore:
            MaxMatchScore = matchScore
            MappedEntity = entity
            MatchedWord = cleanName
    if MappedEntity is not None:
        return (MappedEntity,MatchedWord,MaxMatchScore,entityKeywordsSplit)
    return None
    
def mapEntities(queryEntities,schemaEntityNames):
    mappedEntitesDict = {}
    mappedEntities = []
    for entityKeywords in queryEntities:
        EntityMatchData = mapEntity(entityKeywords,schemaEntityNames)
        if EntityMatchData is not None:
            mappedEntitesDict[entityKeywords] = EntityMatchData[0]
            mappedEntities.append(EntityMatchData)
    return mappedEntitesDict,mappedEntities

def getMatchScore(queryWords,schemaWords):
    # matchedWords / max(len(queryWords),len(schemaWords))
    queryVector = getKeyWordsVector(queryWords)
    schemaVector = getKeyWordsVector(schemaWords)
    matchCount = np.dot(queryVector.T, schemaVector)
    matchScore = matchCount[0][0]/max(len(queryWords),len(schemaWords))
    return matchScore

def constructDictionary(schema):
    entityDict = {}
    for key in schema.keys():
        entityDict[schema[key]["TableName"]] = key
    return entityDict

@lru_cache(maxsize=None)
def mapAttrEntity(entityAttributes, attribute):
    MaxMatchScore,MatchedWord  = 0,None
    for attr in entityAttributes:
        matchScore = getMatchScore(attribute,cleanEntityName(attr))
        if matchScore > MaxMatchScore:
            MaxMatchScore = matchScore
            MatchedWord = attr
    if MatchedWord is not None:
        return (MatchedWord,MaxMatchScore)
    return None,0
        
def mapAttr(entities , attribute , entityDict, schema):
    origAttribute = attribute
    attribute = cleanEntityName(attribute)
    MaxMatchScore,MatchedWord,MatchedEntityName  = 0,None,None
    for entityName in entities:
        ####################################
        #(tuple of attributes of one one entity,)
        idx = entityDict[entityName]
        entityAttributes = tuple(schema[idx]["attributes"].keys())
        attr,matchScore = mapAttrEntity(entityAttributes,tuple(attribute))
        if matchScore > MaxMatchScore:
            MaxMatchScore = matchScore
            MatchedWord = attr
            MatchedEntityName = entityName
    if MatchedWord is not None:
        return (MatchedEntityName,MatchedWord,MaxMatchScore,attribute,origAttribute)
    return None

def getAllAttributes(query):
    attrKeys = ['selectAttrs','groupByAttrs']
    attrKeysAggr = ['orderByAttrs','aggrAttrs']
    attributes = set()
    for key in query.keys():
        if query[key] == []:
            continue
        if key in attrKeys:
            attributes.update(set(query[key]))
        elif key in attrKeysAggr:
            attNames = set(list(zip(*query[key]))[0])
            attributes.update(attNames)
        elif key == 'whereAttrs':
            whereAttributes = [[atr[0],atr[2]] if atr[2]!="value" else [atr[0]]  for atr in query[key]]
            attNames = set(flattenList(whereAttributes))
            attributes.update(attNames)
    return attributes


def mapToSchema(query,schema,entityDict,schemaEntityNames):
    ##################Remember mapped Entities
    mappedEntitesDict,mappedEntities = mapEntities(tuple(query['entities']),tuple(schemaEntityNames))
    mappedEntitesNames = [ v for k,v in mappedEntitesDict.items()]
    
    #mappedEntitesNames = ["players","teams","coaches","awards_coaches"]
    start = timeit.default_timer()
    bestJoin , goals = connectEntities(schema,mappedEntitesNames)

    #print(mappedEntitesNames)
    #print(bestJoin,goals,mappedEntitesNames)
    end = timeit.default_timer()
    
    '''
    select s.name , s.age , a.name , a.age , a.address
    from student s , address a

    mapAttr([student],[name,age])
    mapAttr([address],[name,age,address])

    check for . if true
    same entity => in search
    if successful => break
    if not
        entities in mapped => if successful => break
        if not:
            entities goals_joins => if successful => break
            if not:
                search => schema if successful => break
                if not return None
    '''
    
    mappedAttributes = []
    attributes = getAllAttributes(query)

    for attribute in attributes:
        
        goals_copy = goals.copy()
        schemaEntities = {schema[idx]["TableName"] for idx in schema.keys()}

        #level 1
        if '.' in attribute:
            entity = attribute.split('.')[0]
            if entity in mappedEntitesDict.keys(): 
                entity = mappedEntitesDict[entity]
                attributeName = attribute.split('.')[1]
                
                mapping = mapAttr([entity],attributeName,entityDict,schema)
                if mapping is not None:
                    mapping = list(mapping)
                    mapping[4] = attribute
                    mapping = tuple(mapping)
                    mappedAttributes.append(mapping)
                    continue
            #else: print(f"This Alias entity '{entity}' did not exist {mappedEntitesDict} xx {query['entities']} xx {attribute}")
            goals_copy.discard(entity) #discard searched entity
            schemaEntities.discard(entity) #discard searched entity
            
        #level 2
        entities = {entity for _,entity in mappedEntitesDict.items()}
        mapping = mapAttr(entities,attribute,entityDict,schema)
        if mapping is not None:
            mappedAttributes.append(mapping)
            continue
        goals_copy = goals_copy - entities 
        schemaEntities = schemaEntities - entities

        #level 3
        mapping = mapAttr(goals_copy,attribute,entityDict,schema)
        if mapping is not None:
            mappedAttributes.append(mapping)
            continue
        #schemaEntities = schemaEntities - goals_copy

        # level 4
        # TO BE DISCUSSED
        # mapping = mapAttr(schemaEntities,attribute,entityDict,schema)
        # if mapping is not None:
        #     mappedAttributes.append(mapping)
        #     continue

        mappedAttributes.append((None,None,0,attribute,attribute))

    return mappedEntities,mappedAttributes,goals,mappedEntitesDict


def queryCoverage(mappedAttributes):
    found = sum([1 for entity,_,_,_,_ in mappedAttributes if entity is not None])
    attributesMapped = max(len(mappedAttributes),1)
    return found/attributesMapped

def queryCompactness(mappedEntitiesDict,goals):
    mappedEntites = max(len(goals) ,1)
    compactness = len(mappedEntitiesDict)/mappedEntites
    return compactness

################get final query hits#################
def getNonZeroQueryHits(queryHits):
    nonZeroQueryHits = [ idx for idx,q in enumerate(queryHits) if q!=0]
    return nonZeroQueryHits


def flatten_query_entities(listOfQueries):
    flattened_query_entities = []
    for query in listOfQueries:
        entities = []
        for entity in query['entities']:
            entities.extend(entity.split("_"))
        flattened_query_entities.append(entities)
    return flattened_query_entities

def loadNgramsPickle():
    with open('/home/nada/GP/GP/GP/src/SearchEngine/nGrams/ngrams.pickle', 'rb') as handle:
        ngrams = pickle.load(handle)
    with open('/home/nada/GP/GP/GP/src/SearchEngine/nGrams/unigram.pickle', 'rb') as handle:
        unigram = pickle.load(handle)
    return ngrams,unigram
def getBestCombination(ngrams,entities):
    entitiesOneHotVector=[]
    #2kbr compination mwgoda
    for entity in list(set(entities)):
        entity = entity.split("_")
        entity = [get_lemma(word) for word in entity]
        entityOneHotVector = (getKeyWordsVector(entity)).tostring()
        entitiesOneHotVector.append(entityOneHotVector)
    best_combination = None
    best_combination_key = None
    len_best_combination = 0
    for r in range(len(entitiesOneHotVector)+1):
        for combination in itertools.combinations(entitiesOneHotVector, r):
            combination_key = np.array(list(combination)).tostring()
            if  combination_key in ngrams["whereAtrrsDict"] and len(list(combination)) > len_best_combination:
                best_combination = combination
                best_combination_key = combination_key
                len_best_combination = len(list(combination))
    return best_combination,best_combination_key
def getAttrsProps(attributes,type,query,ngrams,unigram):
    for attr in list(set(attributes)):
        if attr.find(".") != -1:
            attr = attr.split(".")[1]
        attr = attr.split("_")
        attr = [get_lemma(word) for word in attr]
        attrOneHotVector = (getKeyWordsVector(attr)).tostring()   
        if ngrams.get(attrOneHotVector):         
            query[type] += ngrams[attrOneHotVector]
        elif unigram.get(attrOneHotVector):
            query[type] += unigram[attrOneHotVector]
def rankCluster(cluster,queries,k,ngrams,unigram):
    cluster_queries=[]
    for idx in cluster:
        query = queries[idx]
        query['rank'] = 0
        query['whereScore']=0
        query['selectScore']=0
        best_combination,best_combination_key = getBestCombination(ngrams,query['entities'])
        if best_combination==None:
            best_combination,best_combination_key = getBestCombination(ngrams,list(query['mappedEntitesDict'].keys()))
        whereAttrsNgrams = ngrams["whereAtrrsDict"][best_combination_key]
        selectAttrsNgrams = ngrams["selectAttrsDict"][best_combination_key]
        whereAttrs = [attr[0] for attr in query["whereAttrs"]]
        getAttrsProps(whereAttrs,"whereScore",query,whereAttrsNgrams,unigram["whereAtrrsDict"]) 
        getAttrsProps(query["selectAttrs"],"selectScore",query,selectAttrsNgrams,unigram["selectAttrsDict"])
        cluster_queries.append(query)
    sorted_queries = sorted(cluster_queries, key=lambda k: k['selectScore']+k['whereScore'], reverse=True)
    return list(sorted_queries)    
def getRankedQueries(clusters,queries):
    ngrams,unigram = loadNgramsPickle()
    ranked_queries = []
    k=10 ## should be changed
    for cluster in clusters:
        ranked = rankCluster(cluster,queries,k,ngrams,unigram)
        ranked_queries.append(ranked)
    return ranked_queries
    

##############
#ngeb 2l ngrams for select attributes , where attributes
#nsort by sum of the propapility of where attributes
#nsort by sum of the propapility of select attributes
############## TO Do
#validate the output query , where condition , nrun 2l query we n4of lw feh 2y errors