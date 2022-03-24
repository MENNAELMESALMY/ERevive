from tkinter.tix import Tree
from utilities import flattenList
import random

def constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,id, goals,origQuery,bestJoin):
    query = {}
    mappedAttributesDict = {attr[4]:attr[1] if attr[0] is None else attr[0]+"."+attr[1] for attr in mappedAttributes if attr[1] is not None}
    query["coverage"] = coverage
    query["id"] = id
    query["entities"] = [ent for ent in mappedEntitesDict.values()]
    query["cleanedEntities"] = [ent[1] for ent in mappedEntites]
    query["goals"] = list(goals)
    query["mappedEntites"] = list(mappedEntites)
    query["mappedAttributes"] = list(mappedAttributes)
    query["mappedAttributesDict"] = mappedAttributesDict
    query["mappedEntitesDict"] = mappedEntitesDict
    query["bestJoin"] = bestJoin
    query["origQuery"] = origQuery
    attrKeys = ['selectAttrs','groupByAttrs','aggrAttrs','orderByAttrs','whereAttrs','havingAttrs']
    for key in attrKeys:
        query[key] = []
        currentAttributes = origQuery[key]
        if currentAttributes == []:
            continue
        ## take same tuples but instead replace attributes by their mapped attributes to schema
        if key == "aggrAttrs" or key == "orderByAttrs":
            for attr in currentAttributes:
                ## [attr,count]
                if mappedAttributesDict.get(attr[0]) is not None:
                    attr[0] = mappedAttributesDict[attr[0]]
                    query[key].append(attr)
        elif key == "whereAttrs":
            ## [attr,condition,attr,...] or [attr,condition,value,...]
            firstAttrIsUpdated = False 
            for attr in currentAttributes:
                if mappedAttributesDict.get(attr[0]) is not None:
                    attr[0] = mappedAttributesDict[attr[0]]
                    firstAttrIsUpdated = True
                if firstAttrIsUpdated:
                    if attr[2] != "value":
                        if mappedAttributesDict.get(attr[2]) is not None:
                            attr[2] = mappedAttributesDict[attr[2]]
                            query[key].append(attr)
                            firstAttrIsUpdated = False
                    else:
                        firstAttrIsUpdated = False
                        query[key].append(attr)
        elif key == "havingAttrs":
            ## [aggr,attr,operation]
            for attr in currentAttributes:
                if mappedAttributesDict.get(attr[1]) is not None:
                    attr[1] = mappedAttributesDict[attr[1]]
                    query[key].append(attr)
        else:
            for attr in currentAttributes:
                if mappedAttributesDict.get(attr) is not None:
                    query[key].append(mappedAttributesDict[attr])
        if key == "selectAttrs" or key == "groupByAttrs":
            query[key] = list(set(query[key]))
        else:
            query[key] = [list(x) for x in set(tuple(x) for x in query[key])]
    return query

def addJoinAttrs(joins,whereAttrs):
    pass

def queryStructure(queryDict):
    query = "SELECT "
    ## concatenate aggregation functions
    if len(queryDict["aggrAttrs"]) > 0:
        for aggrAttr in queryDict["aggrAttrs"]:
            query += aggrAttr[1] + ' ( ' + aggrAttr[0] + ' ), '

    ## concatenate select attributes
    if len(queryDict["selectAttrs"]) > 0:
        for selectAttr in queryDict["selectAttrs"]:
            query += selectAttr + ', '
        query = query[:-2]
    else:
        query += '*'

    ## concatenate from attributes
    if len(queryDict["mappedEntitesDict"].values()) > 0:
        query += " FROM "
        for entity in queryDict["mappedEntitesDict"].values():
            query += entity + ', '
        query = query[:-2]

    ## concatenate joins
    if len(list(queryDict["bestJoin"])) > 0 or len(queryDict["whereAttrs"]) > 0:
        query += " WHERE "

    whereConditions = addJoinAttrs(list(queryDict["bestJoin"]),queryDict["whereAttrs"])
    
    ## concatenate where attributes
    if len(whereConditions) > 0:
        whereConditions.sort(key=lambda x: x[3] in ["and","or","in"], reverse=True)
        keepEnd = ""
        for whereAttr in whereConditions:
            keepEnd = whereAttr[3]
            if whereAttr[3] == "None":
                whereAttr[3] = ""
            whereAttr = ' '.join(whereAttr)
            if query[-1] == " ":
                query = query[:-1]
            query = query + " " + whereAttr
            # query = query[:-1]
        if keepEnd == "and":
            query = query[:-3]
        elif keepEnd in ["or","in"]:
            query = query[:-2]

    ## concatenate group by attributes
    if len(queryDict["groupByAttrs"]) > 0:
        query += " GROUP BY "
        for groupbyAttr in queryDict["groupByAttrs"]:
            query += groupbyAttr + ', '
        query = query[:-2]

    ## concatenate order by attributes
    if len(queryDict["orderByAttrs"]) > 0:
        query += " ORDER BY "
        orderFunction = ["ASC","DESC"]
        for orderbyAttr in queryDict["orderByAttrs"]:
            index = round(random.random())
            if orderbyAttr[1] != '':
                query += orderbyAttr[1] + ' ( ' + orderbyAttr[0] + ' ) ' + orderFunction[index] + ', '
            else:
                query += orderbyAttr[0] + ' ' + orderFunction[index] + ', '
        query = query[:-2]

    ## concatenate having attributes
    ## [aggr,attr,operation]
    if len(queryDict["havingAttrs"]) > 0:
        query += " HAVING "
        for havingAttr in queryDict["havingAttrs"]:
            query += havingAttr[0] + ' ( ' + havingAttr[1] + ' ) ' + havingAttr[2] + " value " + " AND "
        query = query[:-5]

    query = query.strip()
    query += ";"
    return query
