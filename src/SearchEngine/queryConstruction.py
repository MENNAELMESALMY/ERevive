def constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage,compactness):
    query = {}
    query["coverage"] = coverage
    query["compactness"] = compactness
    query["entities"] = [ent for ent in mappedEntitesDict.values()]
    query["cleanedEntities"] = [ent[1] for ent in mappedEntites]
    query["selectAttrs"] = []
    for attr in mappedAttributes:
        if attr[1] is not None:
            query["selectAttrs"].append(attr[0]+"."+attr[1] if attr[0] is not None else attr[1])
    return query