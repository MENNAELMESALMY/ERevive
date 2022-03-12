from SchemaGraph import *
import os
import re
def canJoin(R,T,schema_graph):
    if R in T: return False
    for t in T:
        for r_fk in schema_graph.node_map[R].foreign_keys:########
            if r_fk['ref_table']==t:
                return True

        for t_fk in schema_graph.node_map[t].foreign_keys:########
            if t_fk['ref_table']==R:
                return True
    return False
    
def ifDuplicate(Tn,T):
    tc = sorted(Tn)
    for ts in T:
        sortT = sorted(ts)
        if tc == sortT:
            return True
    return False
    

#GAMA is Max Entities in Template
def generateTemplates(schema_graph,gama=5):
    T=[[] for i in range(gama)]
    T_out = []
    entities = [node.name for node in schema_graph.nodes]
    current_size = 0
    INV={}
    FWD={}
    Tindex=1
    while current_size<gama:
        for entity in entities:
            if current_size==0:
                Tn = [entity]
                T_out.append(Tn)
                T[current_size].append(Tn)
                if INV.get(entity) is None:
                    INV[entity] = []
                INV[entity].append(Tindex)
                FWD[Tindex] = Tn
                Tindex+=1
            else:
                for ts in T[current_size-1]:
                    if canJoin(entity,ts,schema_graph):
                        Tn = ts+[entity]
                        if (not ifDuplicate(Tn,T[current_size])):
                            if INV.get(entity) is None:
                                INV[entity] = []
                            INV[entity].append(Tindex)
                            FWD[Tindex] = Tn
                            Tindex+=1
                            T_out.append(Tn)
                            T[current_size].append(Tn)
        current_size+=1

    return T_out , INV ,FWD

##################Testing##################
# path = './TestSchema/'
# files = [path+ f for f in os.listdir(path)]
# schema_graph = createGraphSchema(files)

# T_out , INV ,FWD = generateTemplates(schema_graph)
# print(T_out)