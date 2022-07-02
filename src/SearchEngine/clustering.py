from .utilities import flattenList
from .searchIndexer import *
from .joiner import *

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



def getMergdClusters(clusteredQueries,queries):
    mergedClusters = []
    for cluster in clusteredQueries:
        mergedQueries = {}
        newCluster = []
        for i in cluster:
            query = queries[i]

            ## extracting where attributes from where tuples ##
            currentWhereAttrs = []
            #print(query["whereAttrs"],query["groupByAttrs"],query["orderByAttrs"])
            currentWhereAttrs = [[atr[0],atr[2]] if atr[2]!="value" else [atr[0]]  for atr in query["whereAttrs"]]
            currentWhereAttrs = flattenList(currentWhereAttrs)

            #Todo : Check if where condition is same for merging , should split on _
            queryWhereKey = flattenList([re.split(r"[.|_]",q[0]) for q in currentWhereAttrs])
            queryGroupKey = flattenList([re.split(r"[.|_]",q) for q in query["updatedGroupByAttrs"]])
            queryOrderKey = flattenList([re.split(r"[.|_]",q[0][0]) for q in query["orderByAttrs"]])
            queryKeys = queryWhereKey+queryGroupKey+queryOrderKey
            queryKeysVector = getKeyWordsVector(queryKeys)
            queryKeysVector = (queryKeysVector.T).tostring()+bytes(len(queryWhereKey))+bytes(len(queryGroupKey))+bytes(len(queryOrderKey))
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
                if slct[0]=="*": 
                    selectAttrs = [("*",None)]
                    break   
            selectAttrs = list(set(selectAttrs))
            aggrAttrs = [list(x) for x in set(tuple(x) for x in aggrAttrs)]
            queries[whereCluster[0]]["selectAttrs"] = selectAttrs
            queries[whereCluster[0]]["aggrAttrs"] = aggrAttrs
            newCluster.append(whereCluster[0])
        mergedClusters.append(newCluster)
    return mergedClusters


# clusters=[]
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
