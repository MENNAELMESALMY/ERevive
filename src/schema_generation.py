import cv2
from numpy.core.defchararray import count
from skimage.morphology import skeletonize
import numpy as np
from math import sqrt
from removeLines import *


'''
loop on our object:
    -strong entites
    -weak entities and mark it as weak 
        -loop relations 
        -get weak 
        -find identifying
        -go to relation object and get all identifyin entites 
        -put primary keys as foriegn keys
        -primary key 
    -multivalued attributes of the strong relation
    -multivalued of weak relation and mark it as belongs to weak relation (return later)
    -loop on each entiy's relations and add the relation attributes to the relation object

loop on relations:
    if length > 2 : then n-ary array 
        -create new table 
        -put relation atrributes
        -primary key = all primary keys of entites
        -and also foreign key
    -if 1 to 1:
        -find full participation entity with idx and put relation attribute in it 
        -add in it primary key of other side as foreign key

    -if 1 to N:
        -go to n side and put as a forign key the primary key of 1 side
        -and add attribute of relation at n side

    -if N to M:
        -call func of n-ary
'''
'''
change of format:
    schema is dicionray
    attributes : {
        "name":"dataType"
    }
    
'''


def generateSchema(entites , relations , shapes_no):
    schema = {}
    multivaluedWeak = {}
    #strong and weak without full primary key
    for e in entites: 
        schema[e["idx"]] = {
            "TableName": e['name'],
            "attributes":{},
            "primaryKey":[],
            "ForgeinKey":[],
            "isWeak":e['isWeak']
        }

        #multivaled table
        multivalued = addAtrributesAndPrimaryKey(schema[e["idx"]],e['attributes'])
        if e["isWeak"]:
            multivaluedWeak[e["idx"]] = multivalued
        else:
            addMultivaluedTable(schema,multivalued,shapes_no,schema[e["idx"]])
            shapes_no+=len(multivalued)

        #loop on relations and add attributes
        addRelationsAttributes(e["relations"] , relations)

    #add weak keys
    for e in entites:
        if(e["isWeak"]):
            addCompositeKey(schema[e["idx"]],e["idx"],e["relations"],relations,schema)
            addMultivaluedTable(schema,multivaluedWeak[e["idx"]],shapes_no,schema[e["idx"]])
            shapes_no+=len(multivaluedWeak[e["idx"]])  

    for r in relations.values():
        if r["isIdentitfying"]:
            continue
        if len(r["entities"])>2:
            ##nary and NM relation
            shapes_no += 1
            addEntitiesAsTables(r["entities"] ,r["attributes"] , schema,shapes_no)
        else:
            r1 = r["entities"][0]
            r2 = r["entities"][0] if len(r["entities"]) == 1 else r["entities"][1]
            if r1["cardinality"] == '1' and r2["cardinality"] == '1':
                #1 to 1
                if r1["participation"] == 'full':
                    addForgeinKey(r['name'],r1,r2,schema,r["attributes"])
                else:
                    addForgeinKey(r['name'],r2,r1,schema,r["attributes"])

            elif (r1["cardinality"] == '1' and r2["cardinality"] == 'N'): 
                addForgeinKey(r['name'],r2,r1,schema,r["attributes"])
            elif (r1["cardinality"] == 'N' and r2["cardinality"] == '1'):
                addForgeinKey(r['name'],r1,r2,schema,r["attributes"])
            else:
                shapes_no += 1
                addEntitiesAsTables(r["name"],r["entities"] ,r["attributes"], schema,shapes_no)

    return schema



def addRelationsAttributes(entityRelation, relations):
    for r in entityRelation:
        if "attributes" not in relations[str(r["bounding_box"])]:
            relations[str(r["bounding_box"])]["attributes"]=[]
            
        relations[str(r["bounding_box"])]["attributes"] += r["attributes"]
        relations[str(r["bounding_box"])]["isIdentitfying"] = r["isIdentitfying"]


def addMultivaluedTable(schema,multivalued,shapes_no,table):
    for (m,dT) in multivalued:
        shapes_no+=1
        schema[shapes_no] = {
                "TableName": table["TableName"] +'_'+ m,
                "attributes":{m:dT},
                "primaryKey":[m],
                "ForgeinKey":[],
                "isWeak":False
            }
        for p in table["primaryKey"]:
            schema[shapes_no]["primaryKey"].append(table["TableName"]+'_'+p)
            schema[shapes_no]["attributes"][table["TableName"]+'_'+p] = table["attributes"][p]
            schema[shapes_no]["ForgeinKey"].append({
                "attributeName": table["TableName"]+'_'+p,
                "ForignKeyTable": table["TableName"],
                "ForignKeyTableAttributeName": p,
                "patricipaction":"full",
                "dataType": table["attributes"][p]
            })



def addCompositeKey(entity,entityIdx,entityRelations,relations,schema):
    '''
         ForignKey:[
        {
            attributeName:--,   in relations(entity attribute)
            ForignKeyTable:--,  in realtions(entity name)
            ForignKeyTableAttributeName:--, in relations(entity attribute name)
            patricipaction:--, in relations(entity participation)
            dataType:--, in relations
        }
        ]
    '''
    
    #find identifying relation
    for r in entityRelations:
        if r['isIdentitfying']:
            for identifyingEntites in relations[str(r["bounding_box"])]["entities"]:
                if(identifyingEntites["idx"]!=entityIdx):
                    primaryKeysOfEntity = schema[identifyingEntites["idx"]]["primaryKey"]
                    entity["primaryKey"]+= [r['name']+'_'+identifyingEntites["name"]+'_'+n for n in primaryKeysOfEntity]
                    dic = {r['name']+'_'+identifyingEntites["name"]+'_'+n : schema[identifyingEntites["idx"]]["attributes"][n]
                                    for n in primaryKeysOfEntity}
                    entity["attributes"].update(dic)
                    entity["ForgeinKey"]+= [ {
                        "attributeName": r['name']+'_'+identifyingEntites["name"]+'_'+n,
                        "ForignKeyTable": identifyingEntites["name"],
                        "ForignKeyTableAttributeName": n,
                        "patricipaction":identifyingEntites["participation"],
                        "dataType":schema[identifyingEntites["idx"]]["attributes"][n]
                    } for n in primaryKeysOfEntity]
                    


def addAtrributesAndPrimaryKey(entity,attributes):
    mulivalued = []
    for a in attributes:
        if a['isMultivalued']:
             mulivalued.append((a['name'],a['dataType']))
        elif a.get("children") and len(a["children"]):
            addAtrributesAndPrimaryKey(entity,a["children"])
        else:
            entity["attributes"][a['name']] = a['dataType']
            if a['isKey']:
                entity["primaryKey"].append(a['name'])
    return mulivalued


def addEntitiesAsTables(name,entities,attributes,schema,idx):   
    #for e in entities:
    primaryKey = []
    for e in entities:
        primaryKey+=schema[e["idx"]]["primaryKey"]

    schema[idx] = {
                "TableName": name +"_" + "_".join([schema[e["idx"]]["TableName"] for e in entities]),
                "attributes":{attributes[i]["name"] : attributes[i]["dataType"] for i in range(len(attributes))},
                "primaryKey": [],
                "ForgeinKey":[],
                "isWeak":False
            }       
    for e in entities:
        table = schema[e["idx"]]     
        for p in table["primaryKey"]:
            schema[idx]["primaryKey"].append(table["TableName"]+'_'+p)
            schema[idx]["attributes"][table["TableName"]+'_'+p] = table["attributes"][p]
            schema[idx]["ForgeinKey"].append({
                    "attributeName": table["TableName"]+'_'+p,
                    "ForignKeyTable": table["TableName"],
                    "ForignKeyTableAttributeName": p,
                    "patricipaction":"full",
                    "dataType": table["attributes"][p]
                })

def addForgeinKey(name,EntityToUpdate,Entity,schema,rAttributes):
    #add attributes
    dic = { rAttributes[i]["name"] : rAttributes[i]["dataType"] for i in range(len(rAttributes))}
    schema[ EntityToUpdate["idx"]]["attributes"].update(dic)

    #add attributes
    primaryKeysOfEntity = schema[Entity["idx"]]["primaryKey"]
    dic = { Entity["name"]+'_'+name+'_'+n : schema[Entity["idx"]]["attributes"][n] for n in primaryKeysOfEntity}

    #add forign keys
    
    schema[EntityToUpdate["idx"]]["attributes"].update(dic)
    schema[EntityToUpdate["idx"]]["ForgeinKey"]+= [ {
                        "attributeName": Entity["name"]+'_'+name+'_'+n,
                        "ForignKeyTable": Entity["name"],
                        "ForignKeyTableAttributeName": n,
                        "patricipaction":Entity["participation"],
                        "dataType":schema[Entity["idx"]]["attributes"][n]
                    } for n in primaryKeysOfEntity]  


test_schema = {
       1: {'TableName': 'awards_coaches', 
            'TableType':'',
            'attributes': {
            'id': 'str', 
            'coachID': 'datetime',
            'award': 'str',
            'lgID': 'str',
            'note': 'str',
            }, 
            'primaryKey': ['id'], 
            'ForgeinKey': [
            {
            'attributeName': 'coachID',
            'ForignKeyTable': 'coaches', 
            'ForignKeyTableAttributeName': 'coachID', 
            'patricipaction': 'partial', 
            'dataType': 'str'},
            ], 
            'isWeak': False
        },
        2: 
        {
            'TableName': 'awards_players', 
            'TableType':'',
            'attributes': {
            'playerID': 'str', 
            'award': 'str',
            'year': 'int',
            'lgID': 'str',
            'note': 'str',
            'pos': 'str'
            }
            , 
            'primaryKey': ['name','year','lgID']
            , 
            'ForgeinKey': [
            {
            'attributeName': 'playerID',
            'ForignKeyTable': 'players', 
            'ForignKeyTableAttributeName': 'playerID', 
            'patricipaction': 'partial', 
            'dataType': 'str'
            }
            ], 
            'isWeak': False
        },
        5:
        {
            'TableName': 'player_allstar', 
            'TableType':'',
            'attributes': {
            'playerID': 'str', 
            'last_name': 'datetime',
            'first_name': 'str',
            'season_id': 'str',
            'conference': 'str',
            'league_id': 'str',
            'games_played': 'str',
            'minutes': 'str',
            'points': 'str',
            'o_rebounds': 'str',
            'd_rebounds': 'str',
            'rebounds': 'str',
            'assists': 'str',
            'steals': 'str',
            'blocks': 'str',
            'turnovers': 'str',
            'personal_fouls': 'str',
            'fg_attempted': 'str',
            'fg_made': 'str',
            'ft_attempted': 'str',
            'ft_made': 'str',
            'three_attempted':  'str',
            'three_made': 'str',
            }, 
            'primaryKey': ['playerID'], 
            'ForgeinKey': [
            {
            'attributeName': 'playerID',
            'ForignKeyTable': 'players', 
            'ForignKeyTableAttributeName': 'playerID', 
            'patricipaction': 'partial', 
            'dataType': 'str'},
            ], 
            'isWeak': False
        },
        3:
        {
            'TableName': 'players', 
            'TableType':'',
            'attributes': {
            'playerID' : 'str',
            'useFirst' : 'str',
            'firstName' : 'str',
            'middleName' : 'str',
            'lastName' : 'str',
            'nameGiven' : 'str',
            'fullGivenName' : 'str',
            'nameSuffix' : 'str',
            'nameNick' : 'str',
            'pos' : 'str',
            'firstseason' : 'int',
            'lastseason' : 'int',
            'height' :'float',
            'weight' : 'int',
            'college' : 'str',
            'collegeOther' : 'str',
            'birthDate': 'datetime',
            'birthCity' : 'str',
            'birthState' : 'str',
            'birthCountry' : 'str',
            'highSchool' : 'str',
            'hsCity' : 'str',
            'hsState' : 'str',
            'hsCountry' : 'str',
            'deathDate': 'datetime',
            'race' : 'str',
            }
            , 
            'primaryKey': ['playerID']
            , 
            'ForgeinKey': [], 
            'isWeak': False
        },
        4:{
            'TableName': 'coaches',
            'TableType':'',
            'attributes': {
            'coachID': 'str', 
            'year': 'int',
            'tmID': 'str',
            'lgID': 'str',
            'stint': 'int',
            'won': 'int',
            'lost': 'int',
            'post_wins': 'int',
            'post_losses': 'int'},
            'primaryKey': ['coachID','year','tmID','stint'],
            'ForgeinKey': [
            # {
            # 'attributeName': 'tmID',
            # 'ForignKeyTable': 'teams', 
            # 'ForignKeyTableAttributeName': 'tmID', 
            # 'patricipaction': 'partial', 
            # 'dataType': 'str'}
            ]
        },
        6: 
        {
            'TableName': 'players_teams', 
            'TableType':'',
            'attributes': {
            'id' : 'int',
            'playerID' : 'str',
            'year' : 'int',
            'stint' : 'int',
            'tmID' : 'str',
            'lgID' : 'str',
            'GP' : 'int',
            'GS' : 'int',
            'minutes' : 'int',
            'points' : 'int',
            'oRebounds' : 'int',
            'dRebounds' : 'int',
            'rebounds' : 'int',
            'assists' : 'int',
            'steals' : 'int',
            'blocks' : 'int',
            'turnovers' : 'int',
            'PF' : 'int',
            'fgAttempted' : 'int',
            'fgMade' : 'int',
            'ftAttempted' : 'int',
            'ftMade' : 'int',
            'threeAttempted' : 'int',
            'threeMade' : 'int',
            'PostGP' : 'int',
            'PostGS' : 'int',
            'PostMinutes' : 'int',
            'PostPoints' : 'int',
            'PostoRebounds' : 'int',
            'PostdRebounds' : 'int',
            'PostRebounds' : 'int',
            'PostAssists' : 'int',
            'PostSteals' : 'int',
            'PostBlocks' : 'int',
            'PostTurnovers' : 'int',
            'PostPF' : 'int',
            'PostfgAttempted' : 'int',
            'PostfgMade' : 'int',
            'PostftAttempted' : 'int',
            'PostftMade' : 'int',
            'PostthreeAttempted' : 'int',
            'PostthreeMade' : 'int',
            'note' : 'str',
                }
                , 
                'primaryKey': ['id']
                , 
                'ForgeinKey': [
                {
                'attributeName': 'playerID',
                'ForignKeyTable': 'players', 
                'ForignKeyTableAttributeName': 'playerID', 
                'patricipaction': 'partial', 
                'dataType': 'str'
                },
                {
                'attributeName': 'tmID',
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'tmID',
                'patricipaction': 'partial', 
                'dataType': 'str'
                }
                ], 
                'isWeak': False
        },
        7: 
        {
            'TableName': 'draft', 
            'TableType':'',
            'attributes': 
            {'id': 'str', 
            'draftYear': 'datetime',
            'draftRound': 'str',
            'draftSelection':'str',
            'draftOverall': 'datetime',
            'tmID': 'str',
            'firstName':'str',
            'lastName':'str',
            'suffixName':'str',
            'playerID':'str',
            'draftForm':'str',
            'lgID':'str',
            }, 
            'primaryKey': ['id'], 
            'ForgeinKey': 
                [{'attributeName': 'tmID',
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'tmID', 
                'patricipaction': 'partial', 
                'dataType': 'str'},
                {'attributeName': 'draftYear',
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'year', 
                'patricipaction': 'partial', 
                'dataType': 'str'}
                ], 
            'isWeak': False
        },
        8: 
        {
            'TableName': 'series_post', 
            'TableType':'',
            'attributes': 
                {'id': 'str',
                'year': 'str',
                'round': 'str',
                'series': 'str',
                'tmIDWinner': 'str',
                'lgIDWinner': 'str',
                'tmIDLoser': 'str',
                'lgIDLoser': 'str',
                'w': 'str',
                'L': 'str',}, 
            'primaryKey': ['id'], 
            'ForgeinKey': 
                [{'attributeName': 'tmIDWinner', 
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'tmID', 
                'patricipaction': 'full', 
                'dataType': 'str'},
                {'attributeName': 'tmIDLoser', 
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'tmID', 
                'patricipaction': 'full', 
                'dataType': 'str'},
                {'attributeName': 'year', 
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'year', 
                'patricipaction': 'full', 
                'dataType': 'str'},
                ], 
            'isWeak': False
        },
        9:{
            'TableName': 'teams',
            'TableType':'',
            'attributes': {
                'year': 'int',
            'lgID' :'str',
            'tmID' : 'str',
            'franchID' : 'str',
            'confID': 'str',
            'divID': 'str',
            'rank' :'int',
            'confRank': 'int',
            'playoff': 'str',
            'name' : 'str',
                    },
                    'primaryKey': ['year','tmID'],
                    'ForgeinKey': []
        }
}
