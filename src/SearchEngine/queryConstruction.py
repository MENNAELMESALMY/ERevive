from utilities import flattenList


def constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,id, goals,origQuery):
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
    #query["origQuery"] = origQuery
    attrKeys = ['selectAttrs','groupByAttrs','aggrAttrs','orderByAttrs','whereAttrs']
    attrKeysTuple = ['orderByAttrs','aggrAttrs']
    for key in attrKeys:
        query[key] = []
        currentAttributes = origQuery[key]
        if currentAttributes == []:
            continue
        if key=='whereAttrs':
            currentAttributes = [[atr[0],atr[2]] if atr[2]!="value" else [atr[0]]  for atr in currentAttributes]
            currentAttributes = flattenList(currentAttributes)
        isTuple = key in attrKeysTuple
        for attr in currentAttributes:
            attr = attr[0] if isTuple else attr
            if mappedAttributesDict.get(attr) is not None:
                query[key].append(mappedAttributesDict[attr])
        query[key] = list(set(query[key]))
    return query

            
                
