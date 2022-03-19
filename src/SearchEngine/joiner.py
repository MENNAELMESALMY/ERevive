from collections import deque
import copy
# import pickle

class pathEdge():
    def __init__(self,edge,hasGoal):
        self.edge = edge
        self.hasGoal = hasGoal

class entitiesGroup():
    def __init__(self,entities,paths):
        self.entities = entities
        self.paths = paths


def constructGroups(paths,mappedEntities):
    groups = []
    for path in paths:
        joins = ' ,'.join(path)
        entities = { entity for entity in mappedEntities if " "+entity+"." in joins}
        if len(groups) == 0:
            groups.append(entitiesGroup(entities,[path]))
            continue
        hasGroup = False
        for group in groups:
            if not group.entities.isdisjoint(entities):
                hasGroup
                group.entities.update(entities)
                group.paths.append(path)
                hasGroup = True
                break
        if not hasGroup: groups.append(entitiesGroup(entities,[path]))   
    return groups 


def bestJoins(paths,mappedEntities):
    groups = constructGroups(paths,mappedEntities)
    print("Groups count",len(groups))
    joins = set()
    for group in groups:
        minJoins = float("inf")
        Join = None
        for path in group.paths:
            joinsCount = len(path)
            if joinsCount < minJoins:
                minJoins = joinsCount
                Join = path
        joins.update(Join)
        print("NEW JOINS ADDED",Join)
    print("best join: ",joins)
    return joins
    
#TODO:give to this function only a connected component graph
def findPathsBFS(source,goals,graph):
    queue = deque()
    queue.append((source,[]))
    joins = set()
    visited = set()
    visited.add(source)
    while queue:
        curEntityName,path = queue.popleft()
        hasNeighbor = False
        for neighbor in graph[curEntityName]:
            if neighbor['ForignKeyTable'] not in visited:
                hasNeighbor = True
                
                neighborJoin = neighbor['ForignKeyTable']+'.'+neighbor['ForignKeyTableAttributeName']
                join = ' '+curEntityName +'.'+neighbor["attributeName"]+ ' = ' +neighborJoin
                joinHasGoal = neighbor['ForignKeyTable'] in goals
                
                new_path_edge = pathEdge(join,joinHasGoal)
                newPath = copy.deepcopy(path)
                newPath.append(new_path_edge)
                visited.add(neighbor['ForignKeyTable'])
                queue.append((neighbor['ForignKeyTable'],newPath))
                
        if not hasNeighbor:
            #backtrack
            usefulPath = False
            while len(path):
                path_edge = path.pop()
                usefulPath  |= path_edge.hasGoal
                if usefulPath: joins.add(path_edge.edge)
    return joins

def constructGraph(schema):
    graph = {}
    for key in schema.keys():
        entity = schema[key]["TableName"]
        if entity not in graph.keys():
            graph[entity] = []
        for FK in schema[key]["ForgeinKey"]:
            if FK["ForignKeyTable"] not in graph.keys():
                graph[FK["ForignKeyTable"]] = []
        
            #if entity != FK["ForignKeyTable"]:
            graph[entity].append({
                "ForignKeyTableAttributeName":FK["ForignKeyTableAttributeName"],
                "attributeName":FK["attributeName"],
                "ForignKeyTable":FK["ForignKeyTable"]
            })

            
            graph[FK["ForignKeyTable"]].append({
                "ForignKeyTableAttributeName":FK["attributeName"],
                "attributeName":FK["ForignKeyTableAttributeName"],
                "ForignKeyTable":entity
            })
            
    return graph



#Best Joins 
def connectEntities(schema,mappedEntities):
    if len(set(mappedEntities)) == 1:
        return [],set(mappedEntities)
    graph= constructGraph(schema)
    paths = []
    goals = set()
    bestJoin = None
    
    for entity in mappedEntities:
        ###BFS from entity if entities in mapped entites that can be reached from entity
        paths.append(findPathsBFS(entity,mappedEntities,graph))
    print("////////////////////////////////////////////")
    print(mappedEntities)
    #print(paths)
    bestJoin = bestJoins(paths,mappedEntities)
    
    if bestJoin is None: return [],goals
    for join in bestJoin:
        join = join.split('=')
        goals.update({entity.split('.')[0].strip() for entity in join})
    return bestJoin,goals


