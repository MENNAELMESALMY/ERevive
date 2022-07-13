
def shapes_statistics(shapes,weak,keys,relations,total_time,datatypes):
    detected  = {"oval":{"totalCount":0,
                        "multivaluedAttrCount":0,
                        "AttrCount":0},

                "diamond":{"totalCount":0,
                        "IdentifyingRelationCount":0,
                        "RelationCount":0},

                "rectangle":{"totalCount":0,
                        "weakCount":0,
                        "strongCount":0},
                }

    for i,shape in enumerate(shapes):
        detected[shape]["totalCount"] += 1
        if weak[i]:
            key = list(detected[shape].keys())[1]
        else:
            key = list(detected[shape].keys())[2]
        detected[shape][key] += 1

    relation = relation_statistics(relations)
    print("finished rel")
    datatype = datatypes_statistics(datatypes,shapes)
    print("data")

    #primary key
    keys = sum([1 for i in keys if i == True ])
    return {"detectedShapes":detected ,
            "detectedKeys":keys ,
            "detectedRelations":relation ,
            "dataTypes":datatype , 
            "totalTime":"{:.2f}".format(total_time)}


def relation_statistics(relations):
    detected = {"oneToOne":0,
                "oneToMany":0,
                "manyToMany":0,
                "naryRelation":0,
                "fullParticipation":0,
                "partialParticipation":0}
    
    cardenality_count = 0
    partici_count = 0
    for r in relations.values():
       
        cardenality = []
        for e in r["entities"]:
            if e["participation"] == "partial":
                detected["partialParticipation"]+=1
            else:
                detected["fullParticipation"]+=1
            cardenality.append(e["cardinality"].upper())
            partici_count += 1

        if len(cardenality) > 2:
            detected["naryRelation"]+=1
        elif len(cardenality) == 2:
            cardenality_count += 1
            if "1" in cardenality and ("N" in cardenality or "M" in cardenality):
                detected["oneToMany"]+=1
            elif cardenality[0] in ["N","M"] and cardenality[1] in ["N","M"]:
                detected["manyToMany"]+=1
            else:
                detected["oneToOne"]+=1


    if partici_count == 0: partici_count = 1

    detected["partialParticipation"] = int((detected["partialParticipation"] /  partici_count) * 100)
    detected["fullParticipation"] = int((detected["fullParticipation"] /  partici_count) * 100)

    if cardenality_count == 0:cardenality_count=1

    detected["oneToOne"] = int((detected["oneToOne"]/cardenality_count)*100)
    detected["oneToMany"] = int((detected["oneToMany"]/cardenality_count)*100)
    detected["manyToMany"] = int((detected["manyToMany"]/cardenality_count)*100)
    #detected["naryRelation"] = int((detected["naryRelation"]/cardenality_count)*100)

    return detected

def datatypes_statistics(datatypes,shapes):
    detected = {"str":0,"int":0,"datetime":0,"float":0,"bool":0}
    total_count = 0
    for i,shape in enumerate(shapes):
        if shape == "oval":
            detected[datatypes[i]] += 1
            total_count += 1
    
    total_count = 1 if total_count == 0 else total_count
    for i in detected.keys():
        detected[i] = int((detected[i] / total_count) *100)
    return detected
    

