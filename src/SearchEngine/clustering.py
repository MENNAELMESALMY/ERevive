from utilities import flattenList
from searchIndexer import *
from joiner import *
from globalVars import *    

def getClusteredQueries(queries):
    clusteredQueries = {}
    for i,query in enumerate(queries):
        queryEntityKey = getKeyWordsVector(flattenList(query["cleanedEntities"]))
        if clusteredQueries.get((queryEntityKey.T).tostring()) is None: #if key not exist
            clusteredQueries[(queryEntityKey.T).tostring()] = [i]
        else:
            clusteredQueries[(queryEntityKey.T).tostring()].append(i)
    return list(clusteredQueries.values())

def getUniqueSelectAttrs(attrs):
    selectAttrs = []
    outAttrs=[]
    attrsCleaned = [re.split(r"[.|_]",attr) for attr in attrs]
    for i,attr in enumerate(attrsCleaned):
        attrOneHot = getKeyWordsVector(attr)
        if attrOneHot.tostring() not in selectAttrs:
            selectAttrs.append(attrOneHot.tostring())
            outAttrs.append(attrs[i])
    return outAttrs
def getMergdClusters(clusteredQueries,queries):
    mergedClusters = []
    for cluster in clusteredQueries:
        mergedQueries = {}
        newCluster = []
        for i in cluster:
            query = queries[i]
            #Todo : Check if where condition is same for merging , should split on _
            queryWhereKey = flattenList([re.split(r"[.|_]",q) for q in query["whereAttrs"]])
            queryGroupKey = flattenList([re.split(r"[.|_]",q) for q in query["groupByAttrs"]])
            queryOrderKey = flattenList([re.split(r"[.|_]",q[0]) for q in query["orderByAttrs"]])
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
            #selectAttrs = getUniqueSelectAttrs(selectAttrs)
            selectAttrs = list(set(selectAttrs))
            aggrAttrs = list(set(aggrAttrs))
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
