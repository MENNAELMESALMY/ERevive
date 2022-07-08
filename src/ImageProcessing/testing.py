
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
    return {"detected shapes":detected ,
            "detected keys":keys ,
            "detected relations":relation ,
            "dataTypes":datatype , 
            "total time":total_time}


def relation_statistics(relations):
    detected = {"1 to 1":0,
                "1 to N":0,
                "N to M":0,
                "nary relation":0,
                "full participation":0,
                "partial participation":0}
    
    for r in relations.values():
        cardenality = []
        for e in r["entities"]:
            if e["participation"] == "partial":
                detected["partial participation"]+=1
            else:
                detected["full participation"]+=1
            cardenality.append(e["cardinality"].upper())

        if len(cardenality) > 2:
            detected["nary relation"]+=1
        elif len(cardenality) == 2:
            if "1" in cardenality and ("N" in cardenality or "M" in cardenality):
                detected["1 to N"]+=1
            elif cardenality[0] in ["N","M"] and cardenality[1] in ["N","M"]:
                detected["N to M"]+=1
            else:
                detected["1 to 1"]+=1
        
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
    

