from select import select
from .utilities import flattenList
from .searchIndexer import *
from .joiner import *

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

def getClusteredQueries(queries):
    clusteredQueries = {}
    for i,query in enumerate(queries):
        sorted_entities = sorted(query["entities"])
        queryEntityKey = "_".join(sorted_entities)
        if clusteredQueries.get(queryEntityKey) is None: #if key not exist
            clusteredQueries[queryEntityKey] = [i]
        else:
            clusteredQueries[queryEntityKey].append(i)
    return list(clusteredQueries.values())


def getQueryKey(query):
    whereAttrs =[atr[0][0]+"_"+atr[2][0] if atr[2]!="value" else atr[0][0] for atr in query["whereAttrs"]]
    groupBy = query.get("updatedGroupByAttrs") if query.get("updatedGroupByAttrs") else query["groupByAttrs"]
    groupByAttrs = [atr if query.get("updatedGroupByAttrs") else atr[0] for atr in groupBy]
    orderByAttrs = [atr[0][0]+"_"+atr[1] if (atr[1] and atr[1]!="") else atr[0][0] for atr in query["orderByAttrs"]]
    #sort the attributes in order to make the key unique 
    whereAttrs.sort()
    groupByAttrs.sort()
    orderByAttrs.sort()
    return "_".join(whereAttrs)+"_"+"_".join(groupByAttrs)+"_"+"_".join(orderByAttrs)


def getMergdClusters(clusteredQueries,queries,testSchema):
    mergedClusters = []
    for cluster in clusteredQueries:
        mergedQueries = {}
        newCluster = []
        for i in cluster:
            query = queries[i]

            #currentWhereAttrs = []
            #currentWhereAttrs = [[atr[0],atr[2]] if atr[2]!="value" else [atr[0]]  for atr in query["whereAttrs"]]
            #currentWhereAttrs = flattenList(currentWhereAttrs)

            #queryWhereKey = flattenList([re.split(r"[.|_]",q[0]) for q in currentWhereAttrs])
            #groupBy = query.get("updatedGroupByAttrs") if query.get("updatedGroupByAttrs") else query["groupByAttrs"]
            #queryGroupKey = flattenList([re.split(r"[.|_]",q) if query.get("updatedGroupByAttrs") else re.split(r"[.|_]",q[0]) for q in groupBy])
            #queryOrderKey = flattenList([re.split(r"[.|_]",q[0][0]) for q in query["orderByAttrs"]])
            #queryKeys = queryWhereKey+queryGroupKey+queryOrderKey
            #queryKeysVector = getKeyWordsVector(queryKeys)
            #queryKeysVector = (queryKeysVector.T).tostring()+bytes(len(queryWhereKey))+bytes(len(queryGroupKey))+bytes(len(queryOrderKey))
            queryKeysVector = getQueryKey(query)
            if mergedQueries.get(queryKeysVector) is None: #if key not exist
                mergedQueries[queryKeysVector] = [i]
            else:
                mergedQueries[queryKeysVector].append(i)

        mergedQueries = list(mergedQueries.values())
        for whereCluster in mergedQueries:
            selectAttrs = []
            aggrAttrs = []  
            for i in whereCluster:
                query = queries[i]
                selectAttrs.extend(query["selectAttrs"])
                aggrAttrs.extend(query["aggrAttrs"][0:])
            for slct in selectAttrs:
                if slct[0]=="*" or slct[0].find("*")!=-1: 
                    selectAttrs = [("*",None)]
                    aggrAttrs = []
                    break   
            selectAttrs = list(set(selectAttrs))
            aggrAttrs = [list(x) for x in set(tuple(x) for x in aggrAttrs)]
            queries[whereCluster[0]]["selectAttrs"] = selectAttrs
            queries[whereCluster[0]]["aggrAttrs"] = aggrAttrs
            selectAttrsNames = [slct[0] for slct in selectAttrs]
            aggrAttrsNames = [aggr[0][0]+"_"+aggr[1] for aggr in aggrAttrs]
            newOrderByAttrs = []
            for order in queries[whereCluster[0]]["orderByAttrs"]:
                if (not order[1] or order[1]==""):  
                    if order[0][0] in selectAttrsNames:
                        newOrderByAttrs.append(order)
                else:
                    if order[0][0]+"_"+order[1] in aggrAttrsNames:
                        newOrderByAttrs.append(order)
            queries[whereCluster[0]]["orderByAttrs"] = newOrderByAttrs

            if len(queries[whereCluster[0]]["aggrAttrs"])>0:
                newGroupByAttrs = []
                for group in query["groupByAttrs"]:
                    if group[0] in selectAttrsNames:
                        newGroupByAttrs.append(group)
                queries[whereCluster[0]]["groupByAttrs"] = newGroupByAttrs
            else:
                queries[whereCluster[0]]["groupByAttrs"] = []
            if len(queries[whereCluster[0]]["entities"])==1:
                if len(queries[whereCluster[0]]["selectAttrs"])==1 and queries[whereCluster[0]]["selectAttrs"][0][0]=="*"\
                    and len(queries[whereCluster[0]]["aggrAttrs"])==0 and len(queries[whereCluster[0]]["groupByAttrs"])==0 \
                        and len(queries[whereCluster[0]]["orderByAttrs"])==0 and len(queries[whereCluster[0]]["havingAttrs"])==0:
                        continue
            if queries[whereCluster[0]].get("updatedGroupByAttrs") is None:
                updateQueryGroupBy(queries[whereCluster[0]],testSchema)
            newCluster.append(whereCluster[0])
        if len(newCluster)>0:
            mergedClusters.append(newCluster)
    return mergedClusters

# for cluster in clusteredQueries:
#     #create new thread for each cluster
#     #sort cluster by queryHits
#     cluster = sorted(cluster,key=lambda x:queryHits[x],reverse=True)
#     #take top 100 queries
#     cluster = cluster[:100]
#     clusters.append(cluster)

#def startClusterThreads(clusters):
    #clustersThreads = []
    #for cluster in clusters:
    #    getClusterFeatures(cluster)
    ##    clusterThread = threading.Thread(target=getClusterFeatures,args=(cluster,))
    ##    clustersThreads.append(clusterThread)
    #for clusterThread in clustersThreads:
    ##clustersThreads[0].start()
    #for clusterThread in clustersThreads:
    ##clustersThreads[0].join()
#startClusterThreads(clusters)
