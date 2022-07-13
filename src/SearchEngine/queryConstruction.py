import random

from SearchEngine.clustering import updateQueryGroupBy

def constructQuery(mappedEntitesDict,mappedEntites,mappedAttributes,coverage, goals,origQuery,bestJoin):
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
        currentAttributes = list(origQuery[key])
        if currentAttributes == []:
            continue
        ## take same tuples but instead replace attributes by their mapped attributes to schema
        if key == "aggrAttrs" or key == "orderByAttrs":
            for attr in currentAttributes:
                ## [attr,count]
                attr = list(attr)
                if mappedAttributesDict.get(attr[0]) is not None:
                    attr[0] = mappedAttributesDict[attr[0]]
                    query[key].append(attr)
        elif key == "whereAttrs":
            ## [attr,condition,attr,...] or [attr,condition,value,...]
            firstAttrIsUpdated = False 
            for attr in currentAttributes:
                attr = list(attr)
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
                attr = list(attr)
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

import json
def queryStructure(queryDict):
    # ob = {}
    # ob["query"] = queryDict
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

            if isinstance(whereAttr[2], str) and whereAttr[2]!="value":
                whereAttr = [whereAttr[0],whereAttr[1],whereAttr[2],whereAttr[3]]
                whereAttr = ' '.join(whereAttr)

            else:
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
    # ob["constructed"] = query
    # with open("debugConstructedQueries.json","a+") as file:
    #     json.dump(ob,file)

    return query

def getModelsObj(testSchema):
    models_obj = {}
    for model in testSchema.values():
        models_obj.update({
            model["TableName"]:model["attributes"]
        })
    return models_obj
def create_response_model(selectAttrs,aggrAttrs,entities,modelsObject):
    pythondtypes_restmapping = {
    "str":"fields.String",
    "int":"fields.Integer",
    "float":"fields.Float",
    "bool":"fields.Boolean",
    "datetime":"fields.DateTime"
    }
    response_model = ""
    ui_response_model = {}
    db_selects= []

    if (len(selectAttrs)==1 and selectAttrs[0][0]=="*") or (len(selectAttrs)==0 and len(aggrAttrs)==0):
        response_model,ui_response_model =  get_astrisk_models(entities,modelsObject)
        response_model+=","
        selectAttrs=[]

    all_entities_astrisk=[]
    sel_len=0
    for attr in selectAttrs:   
        if "*" in attr[0]:
            all_entities_astrisk.append(attr[0].split('.')[0])
        else:
            sel_len+=1
    all_entities_astrisk = list(set(all_entities_astrisk))
    if len(all_entities_astrisk):
        response_model,ui_response_model =  get_astrisk_models(all_entities_astrisk,modelsObject)
        response_model+=","
    for attr in selectAttrs:
        attr_name = attr[0]
        attr_type = attr[1]
        if "*" in attr:
            continue
        db_selects.append((attr_name,attr_type,None))

        if attr_type in pythondtypes_restmapping:
            response_model+= "'"+attr_name+"' : "+pythondtypes_restmapping[attr_type]+","
            ui_response_model[attr_name] = attr_type
        else:
            response_model+=  "'"+attr_name+"' : fields.String,"
            ui_response_model[attr_name] = "str"
            
    for attr in aggrAttrs:
        attr_aggregation = attr[1]
        attr_name = attr[0][0]
        attr_type = attr[0][1] if ("*" not in attr[0][0] and attr[1] != "count") else "int"
        db_selects.append((attr_name,attr_type,attr_aggregation))
        attr_name = attr_aggregation+"_"+ (attr_name if "*" not in attr_name else "all")
        if attr_name == "count_awards_players.playerID":print(attr)
        if attr_type in pythondtypes_restmapping:
            response_model+= "'"+attr_name+"' : "+pythondtypes_restmapping[attr_type]+","
            ui_response_model[attr_name] = attr_type
        else:
            response_model+=  "'"+attr_name+"' : fields.String ,"
            ui_response_model[attr_name] = "str"
    response_model = response_model[:-1]
    return response_model , ui_response_model ,db_selects

def get_astrisk_models(entities,modelsObjects):
    all_models_response=''
    all_models_ui_response = {}
    for entity in entities:
        attrs = modelsObjects[entity].items()
        attrs = [(entity+'.'+attr[0],attr[1]) for attr in attrs]        
        entity_model,entity_ui_model,_ = create_response_model(attrs,[],entities,modelsObjects)
        all_models_response+=entity_model+","
        all_models_ui_response.update(entity_ui_model)
    all_models_response = all_models_response[:-1]
    return all_models_response , all_models_ui_response
def get_attr_name_type(attrs,attr_type=None):
    attr_names = []
    for attr in attrs:
        if type(attr[0])!=str:
            attr_name = attr[0][0] 
            if attr_type and attr[1] and attr[1] !="":
                attr_name = attr_name.split('.')[0]+'.'+attr[1]+'_'+attr_name.split('.')[-1]
        else:
            attr_name = attr[0]
            if attr[1] and attr[1] !="":
                attr_name = attr[1]+"_"+attr_name
        if attr_name.find('*')!=-1:   
            attr_name = attr_name.replace('*','all')

        if type(attr[0])!=str and len(attr) > 2 and attr[2] != "value":
            attr_names.append(attr[2])    
        attr_names.append(attr_name)
    return attr_names

def query_renaming(entities,whereAttrs,groupAttrs,orderAttrs,isUpdate=False,is_group_all=False):
    where_attr = get_attr_name_type(whereAttrs)
    if not isUpdate:
        group_attr = get_attr_name_type(groupAttrs)
    else:
        group_attr = groupAttrs
    if is_group_all:
        group_attr = ["all"]

    order_attr = get_attr_name_type(orderAttrs,"order")
    where_attr = set([attr[attr.find(".")+1:] for attr in where_attr if attr != "*"])
    order_attr = set([attr[attr.find(".")+1:] for attr in order_attr if attr != "*"])
    group_attr = set([attr[attr.find(".")+1:] for attr in group_attr if attr != "*"])
    endpoint_name = "get"+"_"+"_".join(entities)
    ui_name = "get "+" ".join(entities)

    
    if len(where_attr) != 0:
        endpoint_name += "_filteredby"+"_"+"_".join(where_attr)
        ui_name += " filtered by "+" , ".join(where_attr)
    if len(group_attr) != 0:
        endpoint_name +="_groupedby"+ "_"+"_".join(group_attr)
        ui_name += " grouped by "+" , ".join(group_attr)
    if len(order_attr) != 0:
        endpoint_name +="_orderedby"+ "_"+"_".join(order_attr)
        ui_name += " ordered by "+" , ".join(order_attr)
    
    return endpoint_name,ui_name

def get_aggr_attrs(aggr_attrs):
    count_attrs = []
    final_aggr_attr = []
    remove_counts = False
    for attr in aggr_attrs:
        attr_aggregation = attr[1]
        if attr_aggregation != "count":
            final_aggr_attr.append(attr)
        else:
            count_attrs.append(attr)
            if "*" in attr[0][0]:
                final_aggr_attr.append(attr)
                remove_counts = True
    
    if not remove_counts:
        final_aggr_attr.extend(count_attrs)
    
    return final_aggr_attr

def create_query_ui_endpoint(q,modelsObjects):
    query = q[0]
    endpoint_name,ui_name = query_renaming(query["entities"],query["whereAttrs"],query["updatedGroupByAttrs"],query["orderByAttrs"],True)
    endpoint_url = '/'.join(query["entities"])+'/'+endpoint_name
    endpoint_method = "get"
    queryParams = []
    for attr in query["whereAttrs"]:
        if attr[2] != "value":
            continue
        attr_name = attr[0][0]
        attr_type = attr[0][1]
        attr_operator = attr[1]
    
        queryParams.append((attr_name,attr_type,attr_operator,None))

    for attr in query["havingAttrs"]:
     
        attr_name = attr[1][0] if "*" not in attr[1][0] else "having_value"
        attr_type = attr[1][1] if "*" not in attr[1][0] else "int"
        attr_operator = attr[2]
        attr_aggregation = attr[0]
        
        queryParams.append((attr_name,attr_type,attr_operator,attr_aggregation))

    for attr in query["orderByAttrs"]:
        if attr[0][0] == "*" and attr[1] is None:
            continue

        contain_aggr = len(query["aggrAttrs"]) > 0 or len(query["groupByAttrs"]) > 0
        attr_name = attr[0][0]
        attr_type = attr[0][1]
        attr_aggregation = attr[1]
        param_name = ""
        aggr = "_"+attr_aggregation +"_" if attr_aggregation and contain_aggr else ""
        if attr_name == "*":
            param_name = "is_order_of"+aggr+"of_rows_desc"
        else:
            attr_name = attr_name.split('.')[1]
            aggr = "_" if not aggr else aggr
            param_name = "is_order_of"+aggr+attr_name+"_desc"
        queryParams.append((param_name,"bool",None,attr_aggregation))

    aggrAttrs = get_aggr_attrs(query["aggrAttrs"])
    response_model , ui_response_model , db_selects = create_response_model(query["selectAttrs"],aggrAttrs,query["entities"],modelsObjects)
    response_model = "{ "+response_model+" }"
    endpoint = {
        "method": endpoint_method,
        "url": endpoint_url.lower(),
        "queryParams": queryParams,
        "bodyParams": [],
        "response": ui_response_model,
        "ui_name": ui_name.lower(),
        "cluster_name": ("_".join(query["entities"])).lower(),
        "endpoint_name":endpoint_name.lower()+"_"+str(query["idx"]),
        "is_single_entity":len(query["entities"])==1,
        "query": q[1],
        "queryObj":query,
        "is_updated":False,
    }
    return response_model , endpoint , db_selects
    
def prepareQuery(query,modelsObjects=None,testSchema=None):
    if modelsObjects is None:
        modelsObjects = getModelsObj(testSchema)
    updateQueryGroupBy(query[0],testSchema)
    resource_model , endpoint_object , _ = create_query_ui_endpoint(query,modelsObjects)  # return to frontend
    return  endpoint_object ,resource_model

def prepareClusters(clusters,testSchema):
    modelsObjects = getModelsObj(testSchema)
    finalClusters = []
    for cluster in clusters:
        errors = []
        finalCluster = []
        idx = 0
        for query in cluster:
            cartesian = len(query[0]["entities"]) > 1 and len(query[0]["bestJoin"]) == 0
            hasGroupBy = len(query[0]["groupByAttrs"]) != 0
            if cartesian and hasGroupBy:
                continue
            query[0]["idx"] = idx
            endpoint_object ,resource_model = prepareQuery(query,modelsObjects,testSchema)  # return to frontend
       
            if endpoint_object['endpoint_name'] not in errors:
                errors.append(endpoint_object['endpoint_name'])
            else:
                print("ENDPOINT ALREADY EXISTS\n",query[0],endpoint_object['endpoint_name'])   
                continue
            finalCluster.append([endpoint_object,resource_model])
            idx+=1
        finalClusters.append(finalCluster)
    return finalClusters
    