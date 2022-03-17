from re import L
import sys
# import threading
from searchIndexer import *
from joiner import *
# import globalVars
import os
import json
import timeit

from functools import lru_cache

def getListQueries():
    listOfQueries=[]
    datapath = "/home/hager/college/GP/GP/notebooks/preparingDatasets/finalOutputs"
    files = os.listdir(datapath)
    for queryFile in files:
        if queryFile.find("synonyms")!=-1:
            continue
        with open(datapath+"/"+queryFile)as f:
            fileObj = json.load(f)
            for query in fileObj:
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
        return (MatchedEntityName,MatchedWord,MaxMatchScore,attribute)
    return None

def getAllAttributes(query):
    attrKeys = ['selectAttrs','groupByAttrs','whereAttrs','aggrAttrs']
    attrKeysAggr = ['orderByAttrs']
    attributes = set()
    for key in query.keys():
        if query[key] == []:
            continue
        if key in attrKeys:
            attributes.update(set(query[key]))
        elif key in attrKeysAggr:
            attNames = set(list(zip(*query[key]))[0])
            attributes.update(attNames)
    return attributes


def mapToSchema(query,schema,entityDict,schemaEntityNames):
    ##################Remember mapped Entities
    mappedEntitesDict,mappedEntities = mapEntities(tuple(query['entities']),tuple(schemaEntityNames))
    mappedEntitesNames = [ v for k,v in mappedEntitesDict.items()]
    
    start = timeit.default_timer()
    bestJoin , goals = connectEntities(schema,mappedEntitesNames)

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

        # #level 4
        # TO BE DISCUSSED
        # mapping = mapAttr(schemaEntities,attribute,entityDict,schema)
        # if mapping is not None:
        #     mappedAttributes.append(mapping)
        #     continue

        mappedAttributes.append((None,None,0,attribute))

    return mappedEntities,mappedAttributes,goals,mappedEntitesDict


def queryCoverage(mappedAttributes):
    found = sum([1 for entity,_,_,_ in mappedAttributes if entity is not None])
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

