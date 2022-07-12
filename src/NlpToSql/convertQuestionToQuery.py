test_schema = {
    11: {
      "TableName": "DEPARTMENT",
      "attributes": {
        "name": "str",
        "start_date": "datetime",
        "EMPLOYEE_Manages_attr_1": "str",
      },
      "primaryKey": ["name"],
      "ForgeinKey": [
        {
          "attributeName": "EMPLOYEE_Manages_attr_1",
          "ForignKeyTable": "EMPLOYEE",
          "ForignKeyTableAttributeName": "attr_1",
          "patricipaction": "partial",
          "dataType": "str",
        },
      ],
      "isWeak": False,
    },
    34: {
      "TableName": "DEPARTMENT_Clocation",
      "attributes": { "Clocation": "str", "DEPARTMENT_name": "str" },
      "primaryKey": ["Clocation", "DEPARTMENT_name"],
      "ForgeinKey": [
        {
          "attributeName": "DEPARTMENT_name",
          "ForignKeyTable": "DEPARTMENT",
          "ForignKeyTableAttributeName": "name",
          "patricipaction": "full",
          "dataType": "str",
        },
      ],
      "isWeak": False,
    },
    12: {
      "TableName": "EMPLOYEE",
      "attributes": {
        "last_name": "str",
        "middle_initis": "str",
        "first_name": "str",
        "addres": "str",
        "salary": "float",
        "sex": "str",
        "status": "str",
        "birth_date": "str",
        "attr_1": "str",
        "start_date": "datetime",
        "DEPARTMENT_Employed_name": "str",
        "EMPLOYEE_Supervision_attr_1": "str",
      },
      "primaryKey": ["attr_1"],
      "ForgeinKey": [
        {
          "attributeName": "DEPARTMENT_Employed_name",
          "ForignKeyTable": "DEPARTMENT",
          "ForignKeyTableAttributeName": "name",
          "patricipaction": "full",
          "dataType": "str",
        },
        {
          "attributeName": "EMPLOYEE_Supervision_attr_1",
          "ForignKeyTable": "EMPLOYEE",
          "ForignKeyTableAttributeName": "attr_1",
          "patricipaction": "partial",
          "dataType": "str",
        },
      ],
      "isWeak": False,
    },
    24: {
      "TableName": "PROJECT",
      "attributes": {
        "location": "str",
        "attr_2": "str",
        "budget": "float",
        "DEPARTMENT_Assigned_name": "str",
      },
      "primaryKey": ["attr_2"],
      "ForgeinKey": [
        {
          "attributeName": "DEPARTMENT_Assigned_name",
          "ForignKeyTable": "DEPARTMENT",
          "ForignKeyTableAttributeName": "name",
          "patricipaction": "partial",
          "dataType": "str",
        },
      ],
      "isWeak": False,
    },
    25: {
      "TableName": "DEPENDENT",
      "attributes": {
        "90x": "str",
        "relatlonship": "str",
        "name": "str",
        "birth_date": "datetime",
        "Dependents_EMPLOYEE_attr_1": "str",
      },
      "primaryKey": ["Dependents_EMPLOYEE_attr_1"],
      "ForgeinKey": [
        {
          "attributeName": "Dependents_EMPLOYEE_attr_1",
          "ForignKeyTable": "EMPLOYEE",
          "ForignKeyTableAttributeName": "attr_1",
          "patricipaction": "partial",
          "dataType": "str",
        },
      ],
      "isWeak": True,
    },
    35: {
      "TableName": "Works_EMPLOYEE_PROJECT",
      "attributes": {
        "start_date": "datetime",
        "hours": "int",
        "EMPLOYEE_attr_1": "str",
        "PROJECT_attr_2": "str",
      },
      "primaryKey": ["EMPLOYEE_attr_1", "PROJECT_attr_2"],
      "ForgeinKey": [
        {
          "attributeName": "EMPLOYEE_attr_1",
          "ForignKeyTable": "EMPLOYEE",
          "ForignKeyTableAttributeName": "attr_1",
          "patricipaction": "full",
          "dataType": "str",
        },
        {
          "attributeName": "PROJECT_attr_2",
          "ForignKeyTable": "PROJECT",
          "ForignKeyTableAttributeName": "attr_2",
          "patricipaction": "full",
          "dataType": "str",
        },
      ],
      "isWeak": False,
    },
  },
  
import spacy
nlp = spacy.load('en_core_web_sm')
from nlpUtils import *
from collections import deque


'''
query_dict = {
  entities:[],
  attributes: [],
  where: [],
  agg: [(),()],
  groupby: [()],
  orderby: [()],
}
'''

def cleanup_question(question):
    '''
    tokensize / lemmetization / ..... (question)
    '''
    tokensDict = {}
    nlpQuestion = nlp(question)
    for token in nlpQuestion:
      tokensDict[token.text] = (token.lemma_,token.pos_)
    return tokensDict

def match_tokens_to_schema(tokens_dict,sql_schema,query_dict):
    '''
    match tokens to schema
    update query_dict
    return None
    TODO:
    1. Synonyms, abbreviations
    2. Coverage -> how many tokens are matched to the schema || combinations
    '''
    detectedEntities = []
    for _,value in tokens_dict.items():
      isEntity = False
      lemma,pos = value
      if pos == "NOUN":
        # print("my schema",sql_schema)
        # first check if noun matches any of the entities
        for ob in sql_schema.values():
          entityName = ob["TableName"]
          if lemma.lower() in entityName.lower():
            query_dict["entities"].append((lemma,entityName))
            detectedEntities.append(entityName)
            isEntity = True
            break
           
        # if not matched with any entity try to match with attributes
        if not isEntity: 
          for ob in sql_schema.values():
            entityName = ob["TableName"]
            for attr in ob["attributes"].keys():
              if lemma.lower() in attr.lower():
                query_dict["attributes"].append((lemma,entityName,attr))
    # detecting attributes belong to entities detected only 
    print("before",query_dict["attributes"])
    print("detectedEntities" , detectedEntities)
    attr_copy =  query_dict["attributes"][:]
    for lemma,entity,attr in attr_copy:
        print(entity)
        if entity not in detectedEntities:
          # delete the irrelevant attribute
          query_dict["attributes"].remove((lemma,entity,attr))

        

def get_aggregates_in_question(query_dict):
    '''
    get aggregates in question
    return list of aggregates
    '''
    pass

def get_where_filters():
    '''
    get aggregates in question
    return list of aggregates
    '''
    pass

def get_query_from_question(sql_schema,question):
    '''
    get query from question
    return query
    '''
    pass

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

sentence = "get names of employees who are in the department of sales"
# sentence = "get employees names with the heighest salary"

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
# displacy.render(doc, style='dep')
# print(treeRoot,tree)
BFS(tree, treeRoot)

question = 'get names of employees who are in the department of sales'

query_dict = {
  "entities":[],
  "attributes": [],
  "where": [],
  "agg": [],
  "groupby": [],
  "orderby": [],
}
tokens_dict = cleanup_question(sentence)
print("tokens ",tokens_dict)
print("--------------------------------------------")
match_tokens_to_schema(tokens_dict,test_schema[0],query_dict)
print("after matching",query_dict)


'''
at the beginig (from user) values and numbers in () and we separate 
1- replace from dictionaries (groupby / orderby / where) by verbs
2- tokenize (without cleaning words) to detect entities and attributes => (belong to detected entities)
3- if more than one entity => use tree (to get relations)
4- if aggreggation => use tree ,having => on same attributes of aggregation
5- replace groupby / orderby / where conditions with verbs and use tree to detect their attributes
6- construct query



1- traverse branches to get all nouns related to each other , 
store level (also where keyword existed before)(to detect where attributes) ,
relation (conj) => attributes
relation (amod) => aggregation (with checking aggregation dictionary),
try to find our values belong to which attribute
2- loop over all nouns detected to detect our entity, attributes, where attributes, aggregation
3- having => on same attributes of aggregation
4- groupby 
5- orderby , sort => see dictionary for keywords (asecnding , descending)  ==> attributes ?????


TODO later:
see if there is attribute mapped to more than one entity (use tree to detect the related one to question)
'''