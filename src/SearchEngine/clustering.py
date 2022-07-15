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
    datatypes={}
    if len(query["aggrAttrs"]) or agg_in_orderby or len(query["havingAttrs"])>1:
        orderByAttrs = [atr[0] for atr in query["orderByAttrs"] if not atr[1] or atr[1]==""]
        groupAttrs = orderByAttrs + query["selectAttrs"]
        selectAttrs = set()
        for attr in groupAttrs:
            if attr[0] == '*':
                for entity in query["entities"]:
                    attrs = models_obj[entity]
                    attrs = [entity+'.'+attr for attr in attrs]
                    selectAttrs.update(attrs)
            else:
                selectAttrs.add(attr[0])
                datatypes[attr[0]] = attr[1]
        groupByAttrs.update(selectAttrs)
    groupByAttrs = list(groupByAttrs)
    query["updatedGroupByAttrs"] = list(groupByAttrs)
    query["groupByAttrs"] = [(attr,datatypes.get(attr,None)) for attr in groupByAttrs]
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
                if slct[0]=="*" or slct[0].find("*")!=-1: #if * and aggr has more than one 
                    selectAttrs = [("*",None)]
                    aggrAttrs = []
                    break

            selectAttrs = list(set(selectAttrs))
            aggrAttrs = [list(x) for x in set(tuple(x) for x in aggrAttrs)]
            queries[whereCluster[0]]["selectAttrs"] = selectAttrs
            queries[whereCluster[0]]["aggrAttrs"] = aggrAttrs
            

            if len(queries[whereCluster[0]]["entities"])==1:
                if len(queries[whereCluster[0]]["selectAttrs"])==1 and queries[whereCluster[0]]["selectAttrs"][0][0]=="*"\
                    and len(queries[whereCluster[0]]["aggrAttrs"])==0 and len(queries[whereCluster[0]]["groupByAttrs"])==0 \
                        and len(queries[whereCluster[0]]["orderByAttrs"])==0 and len(queries[whereCluster[0]]["havingAttrs"])==0\
                            and len(queries[whereCluster[0]]["whereAttrs"])==0:
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
