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
from random import choice
global takenAttrs 
takenAttrs = set()
global takenEntities
takenEntities = set()
global bazetCount 
bazetCount = 0

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
            MappedEntity = [entity]
            MatchedWord = [cleanName]
        elif MaxMatchScore!=0 and matchScore == MaxMatchScore:
            MappedEntity.append(entity)
            MatchedWord.append(cleanName)
    if MappedEntity is not None:
        return (MappedEntity,MatchedWord,MaxMatchScore,entityKeywordsSplit)
    return None
    
def mapEntities(queryEntities,schemaEntityNames):
    global takenEntities
    global bazetCount
    mappedEntitesDict = {}
    mappedEntities = []
    for entityKeywords in queryEntities:
        EntityMatchData = mapEntity(entityKeywords,schemaEntityNames)
        #MappedEntity,MatchedWord,MaxMatchScore,entityKeywordsSplit)
        if EntityMatchData is not None:
            flagCanMatch = False
            for idx,MappedEntity in enumerate(EntityMatchData[0]):
                if MappedEntity not in takenEntities:
                    takenEntities.add(MappedEntity)
                    mappedEntitesDict[entityKeywords] = MappedEntity
                    #EntityMatchData[0] = MappedEntity
                    #EntityMatchData[1] = EntityMatchData[1][idx]
                    mappedEntities.append((MappedEntity,EntityMatchData[1][idx],EntityMatchData[2],EntityMatchData[3]))
                    flagCanMatch = True
                    break
            if not flagCanMatch:
                # print("Baaaaaaaazt")
                # print("built dict",mappedEntitesDict)
                # print("elbazt",entityKeywords,EntityMatchData[0],queryEntities) 
                bazetCount+=1
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
    #global takenAttrs
    #print("takenAttrs:",takenAttrs)
    MaxMatchScore,MatchedWord  = 0,None
    for attr in entityAttributes:
        # if attr in takenAttrs: 
        #     print("attr is taken ",attribute,attr,takenAttrs)
        #     continue
        matchScore = getMatchScore(attribute,cleanEntityName(attr))
        if matchScore > MaxMatchScore:
            MaxMatchScore = matchScore
            MatchedWord = [attr]
        elif MaxMatchScore!=0 and matchScore == MaxMatchScore:
            MatchedWord.append(attr)
    if MatchedWord is not None:
        return (MatchedWord,MaxMatchScore)
    return None,0
        
def mapAttr(entities , attribute , entityDict, schema):
    global takenAttrs
    # temp = attribute
    attribute = cleanEntityName(attribute)
    # if len(attribute) > 1 and attribute[1]== '*' :print("found *",temp)
    MaxMatchScore,Matched  = 0,None
    for entityName in entities:
        ####################################
        #(tuple of attributes of one one entity,)
        idx = entityDict[entityName]
        entityAttributes = tuple(schema[idx]["attributes"].keys())
        attr,matchScore = mapAttrEntity(entityAttributes,tuple(attribute))
        if matchScore > MaxMatchScore:
            MaxMatchScore = matchScore
            Matched = [(attr,entityName)]
        elif MaxMatchScore!=0 and matchScore == MaxMatchScore:
            Matched.append((attr,entityName))

    if Matched is not None:
        # attrs,MatchedEntityName = choice(Matched)
        # MatchedWord = choice(attrs)
        # trials = 0
        # while(MatchedWord in takenAttrs and trials != 4): 
        #     attrs,MatchedEntityName = choice(Matched)
        #     MatchedWord = choice(attrs)
        #     trials += 1
        # if MatchedWord in takenAttrs: return None
        # takenAttrs.add(MatchedWord)
        # return (MatchedEntityName,MatchedWord,MaxMatchScore,attribute)

        #Loooop

        for attrs,MatchedEntityName in Matched:
            for MatchedWord in attrs:
                if MatchedWord not in takenAttrs:
                    takenAttrs.add(MatchedWord)
                    return (MatchedEntityName,MatchedWord,MaxMatchScore,attribute) 
        

        #if len(Matched) > 1:print("tie in more than one entity", len(Matched))
        #if len(attrs) > 1:print("tie in the same entity",attribute,(attrs))
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
    # if len(set(query["entities"])) != len(query["entities"]):
    #     print('-------------------------------------------------')
    #     print("entities:",query["entities"])
    #     print("query:",query["query"])
    #     print()
    mappedEntitesDict,mappedEntities = mapEntities(tuple(set(query['entities'])),tuple(schemaEntityNames))
    mappedEntitesNames = [ v for k,v in mappedEntitesDict.items()]
    
    #mappedEntitesNames = ["players","teams","coaches","awards_coaches"]
    start = timeit.default_timer()
    bestJoin , goals = connectEntities(tuple(mappedEntitesNames))

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
            attribute = attribute.split('.')[1]
            if entity in mappedEntitesDict.keys(): 
                entity = mappedEntitesDict[entity]
                mapping = mapAttr([entity],attribute,entityDict,schema)
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

        # level 4
        # TO BE DISCUSSED
        # mapping = mapAttr(schemaEntities,attribute,entityDict,schema)
        # if mapping is not None:
        #     mappedAttributes.append(mapping)
        #     continue

        mappedAttributes.append((None,None,0,attribute))

    
    # print("/////////////////////////////////////////////")
    # print("mappedAttributes",mappedAttributes)
    # print("takenAttrs",takenAttrs)
    global takenAttrs
    takenAttrs = set()

    global takenEntities
    takenEntities = set()

    # global bazetCount
    # print("bazetCount",bazetCount)
    return mappedEntities,mappedAttributes,goals,mappedEntitesDict,bestJoin


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

