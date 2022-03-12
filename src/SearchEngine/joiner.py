from collections import deque
import copy
import pickle

class pathEdge():
    def __init__(self,edge,hasGoal):
        self.edge = edge
        self.hasGoal = hasGoal

def bestJoins(paths,mappedEntities):
    minJoins = float("inf")
    Join = None
    for path in paths:
        joinsCount = len(path)
        joins = ' ,'.join(path)
        if joinsCount < minJoins and all(" "+entity+"." in joins for entity in mappedEntities):
            minJoins = joinsCount
            Join = path
    
    return Join
    
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
    graph= constructGraph(schema)
    paths = []
    goals = set()
    bestJoin = None
    for entity in mappedEntities:
        paths.append(findPathsBFS(entity,mappedEntities,graph))
        bestJoin = bestJoins(paths,mappedEntities)
    if bestJoin is None: return [],goals
    for join in bestJoin:
        join = join.split('=')
        goals.update({entity.split('.')[0].strip() for entity in join})
    return bestJoin,goals

# with open('/home/hager/college/GP/GP/src/SearchEngine/testSchema.pickle', 'rb') as file:
#    schema = pickle.load(file)
# mappedEntities = ["EMPLOYEE", "DEPENDENT", "PROJECT","DEPARTMENT_Clocation"]

# print("-------------------getting paths-------------------")
# paths = connectEntities(schema,mappedEntities)
# # print("----------------graph----------------")
# # print(graph)
# print("----------------paths----------------")
# for path in paths:  
#     print(path)


