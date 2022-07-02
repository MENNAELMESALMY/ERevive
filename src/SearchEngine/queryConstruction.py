import random

def constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,id, goals,origQuery,bestJoin,testSchema):
    mappedEntitesNames = mappedEntitesDict.values()
    mappedEntitesDict.update({entity:entity for entity in goals if entity not in mappedEntitesNames})
    query = {}
    mappedAttributesDict = {}
    #print(mappedAttributes)
    for attr in mappedAttributes:
        if attr[1] is not None:
            if attr[0] is None:
                if "*" == attr[3]:
                    mappedAttributesDict.update({
                        "*":("*",None)
                    })
                else:
                    mappedAttributesDict.update({
                        attr[4]:(attr[1],attr[5])
                    })
            else:
                if "*" in attr[3]:
                    mappedAttributesDict.update({
                        attr[4]:(attr[0]+"."+"*",None)
                    })
                else:
                    mappedAttributesDict.update({
                        attr[4]:(attr[0]+"."+attr[1],attr[5])
                    })
    #print(mappedAttributesDict)
    query["coverage"] = coverage
    query["id"] = id
    query["entities"] = [ent for ent in mappedEntitesDict.values()]
    query["cleanedEntities"] = [ent[1] for ent in mappedEntites]
    query["goals"] = list(goals)
    query["mappedEntites"] = list(mappedEntites)
    query["mappedAttributes"] = list(mappedAttributes)
    query["mappedAttributesDict"] = mappedAttributesDict
    query["mappedEntitesDict"] = mappedEntitesDict
    query["bestJoin"] = list(bestJoin)
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
    query = updateQueryGroupBy(query,testSchema)
    return query

def is_agg_in_orderby(aggr_attrs):
    for attr in aggr_attrs:
        if attr[1]:
            return True
    return False

def getModelsObj(testSchema):
    models_obj = {}
    for model in testSchema.values():
        models_obj.update({
            model["TableName"]:model["attributes"].keys()
        })
    return models_obj
def updateQueryGroupBy(query,testSchema):
    agg_in_orderby = is_agg_in_orderby(query["orderByAttrs"])
    groupByAttrs = set([attr[0] for attr in query["groupByAttrs"]])
    models_obj = getModelsObj(testSchema)
    if len(query["aggrAttrs"]) or agg_in_orderby:
        selectAttrs = set()
        for attr in query["selectAttrs"]:
            if attr[0] == '*':
                for entity in query["entities"]:
                    attrs = models_obj[entity]
                    attrs = [entity+'.'+attr for attr in attrs]
                    selectAttrs.update(attrs)
                    #print("attrs: ",attrs)
                    #print()
            else:
                selectAttrs.add(attr[0])
            #selectAttrs = [attr[0] for attr in query["selectAttrs"] if "*" not in attr[0]]
        #print("final Attrs: ",selectAttrs)
        groupByAttrs.update(selectAttrs)
    query["updatedGroupByAttrs"] = list(groupByAttrs)
    return query
def addJoinAttrs(joins,whereAttrs):
    sep = 'and'
    for idx,join in enumerate(joins):
        join = join.strip()
        join = join.split(" ")
        if idx == len(joins)-1 and len(whereAttrs)==0:
            sep = ''
        joins[idx] =[join[0],join[1],join[2],sep]
    for attr in whereAttrs:
        for join in joins:
            if join[0] == attr[0] and join[1] == attr[1] and join[2] == attr[2]:
                join[3] = attr[3]
                whereAttrs.remove(attr)
    joins.extend(whereAttrs)
    return joins

def queryStructure(queryDict):
    query = "SELECT "
    ## concatenate aggregation functions
    if len(queryDict["aggrAttrs"]) > 0:
        for aggrAttr in queryDict["aggrAttrs"]:
            query += aggrAttr[1] + ' ( ' + aggrAttr[0][0] + ' ), '

    ## concatenate select attributes
    if len(queryDict["selectAttrs"]) > 0:
        for selectAttr in queryDict["selectAttrs"]:
            query += selectAttr[0] + ', '
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
            if whereAttr[2]!="value":
                whereAttr[2] = whereAttr[2][0]
            whereAttr = [whereAttr[0][0],whereAttr[1],whereAttr[2],whereAttr[3]]
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
            query += groupbyAttr[0] + ', '
        query = query[:-2]

    ## concatenate order by attributes
    if len(queryDict["orderByAttrs"]) > 0:
        query += " ORDER BY "
        orderFunction = ["ASC","DESC"]
        for orderbyAttr in queryDict["orderByAttrs"]:
            index = round(random.random())
            if orderbyAttr[1] != '':
                query += orderbyAttr[1] + ' ( ' + orderbyAttr[0][0] + ' ) ' + orderFunction[index] + ', '
            else:
                query += orderbyAttr[0][0] + ' ' + orderFunction[index] + ', '
        query = query[:-2]

    ## concatenate having attributes
    ## [aggr,attr,operation]
    if len(queryDict["havingAttrs"]) > 0:
        query += " HAVING "
        for havingAttr in queryDict["havingAttrs"]:
            query += havingAttr[0] + ' ( ' + havingAttr[1][0] + ' ) ' + havingAttr[2] + " value " + " AND "
        query = query[:-5]

    query = query.strip()
    query += ";"
    return query
