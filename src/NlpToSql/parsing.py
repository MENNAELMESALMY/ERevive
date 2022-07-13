import spacy 
from spacy import displacy 
# import en_core_web_sm
# nlp = en_core_web_sm.load()
nlp = spacy.load('en_core_web_sm')
sentence = "Which month has the most happy hours?"
sentence = "List all the username and passwords of users with the most popular role."
#sentence = 'get first and last name of employees who owns maximum salary '
sentence = "How much is the maximum salary of employees"
sentence = "what is the name of employee with maximum salary"
sentence = "what is the name of department for each employee"
sentence = "what is the department name of each employee"
sentence = "get grades or names of all students"
sentence = "get students grades in range of 90 to 100 and their names starts with 'M'"
sentence = "what is name of the employee ordered by salary"
# sentence = "get employee name who works in sales department"
sentence = "get minimum and maximum and average salary and age of the employee"
sentence = "get salary of employee which is greater than (200) and less than (500)"


from collections import deque

def BFS(graph, start):
    visited, queue = set(), deque()
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            for rel,to in graph[vertex]:
                if to not in visited:
                    queue.append(to)
    return visited
doc = nlp(sentence)
print(f"{'Node (from)-->':<15} {'Relation':^10} {'-->Node (to)':>15}\n")
tree = {token.text:[] for token in doc}
treeRoot = None
for token in doc:
    print("{:<15} {:^10} {:>15}".format(str(token.head.text), str(token.dep_), str(token.text)))
    if token.dep_ == 'ROOT':
        treeRoot = token.text
        continue
    tree[token.head.text].append((token.dep_,token.text))
displacy.render(doc, style='dep')
# print(treeRoot,tree)
BFS(tree, treeRoot)


# def DFS(graph, start,query_dict):
#     '''
#     return list of aggregate
#     '''
#     aggregate_list = []
#     conjunction_set = set()
#     visited, queue = set(), deque()
#     queue.append(start)
#     while queue:
#         vertex = queue.pop()
#         print(vertex)
#         if vertex not in visited:
#             visited.add(vertex)
#             for rel,to in graph[vertex]:
#                 if to not in visited:
#                     if rel == "amod": 
#                         aggregate_list.append([vertex,to])
#                     if rel == "conj":
#                         conjunction_set.add(vertex)
#                         conjunction_set.add(to)
#                     queue.append(to)
#     # check for aggregation
#     for v1,v2 in aggregate_list:
#       if v1 in agg_dict["MAX"]:
#         query_dict["agg"].append((v2,"MAX","attributes"))
#         if v1 in list(conjunction_set):pass

#       elif v2 in agg_dict["MAX"]:
#         query_dict["agg"].append((v1,"MAX","attributes"))

#       if v1 in agg_dict["MIN"]:
#         query_dict["agg"].append((v2,"MIN","attributes"))
#       elif v2 in agg_dict["MIN"]:
#         query_dict["agg"].append((v1,"MIN","attributes"))

#       if v1 in agg_dict["AVG"]:
#         query_dict["agg"].append((v2,"AVG","attributes"))
#       elif v2 in agg_dict["AVG"]:
#         query_dict["agg"].append((v1,"AVG","attributes"))

#       if (v1 in agg_dict["SUM"]) or (v1 in agg_dict["COUNT"]):
#         if v2 in query_dict["entities"]:
#           query_dict["agg"].append((v2,"COUNT","entities"))
#         elif v2 in query_dict["attributes"]:
#           query_dict["agg"].append((v2,"SUM","attributes"))
#       elif v2 in agg_dict["SUM"]:
#         if v1 in query_dict["entities"]:
#           query_dict["agg"].append((v1,"COUNT","entities"))
#         elif v1 in query_dict["attributes"]:
#           query_dict["agg"].append((v1,"SUM","attributes"))        
#     return visited

