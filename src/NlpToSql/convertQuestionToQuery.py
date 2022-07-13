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
        'age': 'int',
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
  
import json
import spacy
nlp = spacy.load('en_core_web_sm')
from nlpUtils import *
from collections import deque

conjunctions = ['and','or',',','and/or','also']
whQuestions = [ "what", "when", "where", "who", "whom", "which", "whose", "why" , "how"]
notList = ["doesnot" , "doesn't" , "donot" , "don't" , "havenot" , "haven't" , "hasnot" , "hasn't", "isnot" , "isn't" , "arenot" , "aren't", "didnot" , "didn't" , "willnot" , "willn't" , "cannot" , "can't" , "couldnot" , "couldn't" , "wouldnot" , "wouldn't"]

def cleanup_question(question):
    '''
    tokensize / lemmetization / ..... (question)
    '''
    global conjunctions
    tokensDict = {}
    tokens = []
    nlpQuestion = nlp(question)
    for token in nlpQuestion:
      if token.is_punct and token.text != ',':continue
      if (token.text not in stop_words):
        if token.pos_ == 'NOUN' or token.pos_ == 'VERB':
          tokens.append(token.lemma_)
        else:
          tokens.append(token.text)
        tokensDict[token.text] = (token.lemma_,token.pos_)
    return tokensDict,tokens

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
    attr_copy =  query_dict["attributes"][:]
    for lemma,entity,attr in attr_copy:
        # print(entity)
        if entity not in detectedEntities:
          # delete the irrelevant attribute
          query_dict["attributes"].remove((lemma,entity,attr))

#get minimum and maximum and average of salary and age of the employee where salary greater than (250)
def separate_values_in_question(question):
  values_list = []
  temp_list = re.findall('\\(.*?\\)', question)
  values_list = [v[1:-1] for v in temp_list if len(v)]
  return values_list  

def get_conjunction_set_type(conjunctions_set,query_dict\
          ,values_list,conditions_dict,where_dict):
  typesCount = {
    "g": 0,
    "a" : 0,
    "e" : 0,
    "v": 0,
    "c": 0,
    "w": 0
  }
  setType = "garbage"
  tempConjunctions = conjunctions_set
  for idx,item in enumerate(conjunctions_set):
    if item.lower() in agg_dict["MAX"]:
      tempConjunctions[idx] = "MAX"
      typesCount["g"] += 1
    elif item.lower() in agg_dict["MIN"]:
      tempConjunctions[idx] = "MIN"
      typesCount["g"] += 1
    elif item.lower() in agg_dict["AVG"]:
      tempConjunctions[idx] = "AVG"
      typesCount["g"] += 1
    elif item.lower() in agg_dict["SUM"]:
      tempConjunctions[idx] = "SUM"
      typesCount["g"] += 1
    elif item.lower() in agg_dict["COUNT"]:
      tempConjunctions[idx] = "COUNT"
      typesCount["g"] += 1

    for attr_lemma,_,_ in query_dict["attributes"]:
      if item.lower() == attr_lemma.lower():
        typesCount["a"] += 1
    for entt_lemma,_ in query_dict["entities"]:
      if item.lower() == entt_lemma.lower():
        typesCount["e"] += 1

    if item in where_dict:typesCount["w"] += 1

    if item in values_list:typesCount["v"] += 1
      
    if item in conditions_dict: typesCount["c"] += 1
      
    for k in typesCount.keys():
      if typesCount[k] == len(list(conjunctions_set)):
        setType = k
  return setType,tempConjunctions

def get_conjunctions_sets(tokens,query_dict,values_list,conditions_dict,where_dict):
  #tokens without stopwords and prepositions except conjunctions and negations
  sets_count = {'g':0,'a':0,'e':0,'garbage':0,'w':0,'v':0,'c':0}
  reconstructed_question = tokens[0]
  global conjunctions
  conjunctions_sets = {}
  cur_set = []
  i = 1
  while i <= len(tokens)-1:
    if tokens[i] in conjunctions:
      #TODO:check if tokens[i-1] and tokens[i+1] belong to same type (attributes / entities / aggregations)
      if tokens[i-1] not in cur_set: cur_set.append(tokens[i-1])
      if tokens[i+1] not in cur_set: cur_set.append(tokens[i+1])
      i+=1
    elif len(cur_set) > 0:
      conj_type,new_names = get_conjunction_set_type(cur_set,query_dict,values_list,conditions_dict,where_dict)
      if conj_type == 'garbage':
        for el in cur_set :
          conj_type,new_names = get_conjunction_set_type([el],query_dict,values_list,conditions_dict,where_dict)
          set_name = conj_type +'_'+str(sets_count[conj_type])
          reconstructed_question += " " + set_name
          sets_count[conj_type] += 1
          conjunctions_sets[set_name] = new_names
      else:   
        set_name = conj_type +'_'+str(sets_count[conj_type])
        reconstructed_question += " " + set_name
        sets_count[conj_type] += 1
        conjunctions_sets[set_name] = cur_set
      cur_set = []
      continue
    if len(cur_set)==0 and i+1 < len(tokens) and tokens[i+1] not in conjunctions:
      # reconstructed_question  += " " + tokens[i]
      conj_type,new_names = get_conjunction_set_type([tokens[i]],query_dict,values_list,conditions_dict,where_dict)
      set_name = conj_type  + '_' + str(sets_count[conj_type])
      reconstructed_question += " " + set_name
      sets_count[conj_type] += 1
      conjunctions_sets[set_name] = new_names
    i+=1
  if tokens[-2] not in conjunctions:
    conj_type,new_names = get_conjunction_set_type([tokens[-1]],query_dict,values_list,conditions_dict,where_dict)
    set_name = conj_type + '_' + str(sets_count[conj_type])
    reconstructed_question += " " + set_name
    sets_count[conj_type] += 1
    conjunctions_sets[set_name] = new_names
    # reconstructed_question += " " + tokens[-1]
  return conjunctions_sets,reconstructed_question

def get_aggregates_in_question(query_dict,new_question,conjunctions_sets):
    '''
    get aggregates in question
    return list of aggregates
    '''
    aggrFound = False
    aggrList = []
    totalRelations = []
    for word in new_question.split():
      tempLetter = ""
      if 'a_' in word or 'g_' in word or 'e_' in word:
        tempLetter = word.split('_')[0]
      else: continue
      if (tempLetter == 'g'):
        aggrList.append(word)
        aggrFound = True
      if (tempLetter == 'a'):
        aggrList.append(word)
        totalRelations.append(aggrList)
        aggrList = []
        if aggrFound == True:
          aggrFound = False

    for rel in totalRelations:
      if (len(rel) == 2):
        for aggr in list(conjunctions_sets[rel[0]]):
          for attr in list(conjunctions_sets[rel[1]]):
            query_dict["agg"].append([aggr,attr])
      elif (len(rel) == 1):
        if rel[0].split('_')[0] == 'a':
          query_dict["selectAttrs"] =  conjunctions_sets[rel[0]]

def get_conditions_filters(tokens,conditions_dict):
  joinedQuestion = " ".join(tokens)
  #in case of the word written as doesnot / donot / ...
  #joinedQuestion = re.sub("n\'t|not",' not',joinedQuestion)
  for word in joinedQuestion.split():
    if word.endswith('not') or word.endswith("n\'t"):
      joinedQuestion = joinedQuestion.replace(word , "not")

  for key,value in conditions_dict.items():
    for c in value:
      joinedQuestion = joinedQuestion.replace(' '+c,' '+key)

  return joinedQuestion.split()

def get_where_filters(reconstructed_question,query_dict,conjunctions_sets):
    '''
    get where conditions in question
    return list of aggregates
    '''
    print("reconstructed_question",reconstructed_question)
    contitions = []
    inWhere = False
    words = reconstructed_question.split()
    for idx,word in enumerate(words):
      if 'w_' in word:inWhere = True;continue
      if inWhere:
        if 'a_' in word:
          contitions.append([word])
        elif 'v_' in word or 'c_' in word:
          if len(contitions) == 0:
            i = idx-1
            while i >= 0:
              if 'a_' in words[i]:
                contitions.append([words[i]])
                break
              i-=1
          if len(contitions) > 0: contitions[-1].append(word)
    for condition in contitions:
      where_clause = {
        "attr":[],
        "op":[],
        "val":[]
      }
      for idx,word in enumerate(condition):
        if 'a_' in word:
          where_clause['attr'].extend(conjunctions_sets[word])
        elif 'v_' in word:
          where_clause['val'].extend(conjunctions_sets[word])
        elif 'c_' in word:
          where_clause['op'].extend(conjunctions_sets[word])
      where_clause['op_val'] = list(zip(where_clause['op'],where_clause['val']))
      query_dict['where'].append(where_clause)

def get_query_from_question(query_dict):
    '''
    get query from question
    return query
    '''
    finalPredictedQuery = "SELECT "
    if len(query_dict["agg"]) > 0:
      for aggList in query_dict["agg"]:
        finalPredictedQuery += aggList[0] + ' ( ' + aggList[1] + ' ), '
    attr = list(list(zip(*query_dict["attributes"]))[2])
    print(attr)
    finalPredictedQuery += ",".join(attr)
    
    finalPredictedQuery += " FROM " + query_dict["entities"][0][1] + " WHERE "
    
    for where_clause in query_dict["where"]:
      finalPredictedQuery += "("
      for idx,attr in enumerate(where_clause["attr"]):
        for op,val in where_clause["op_val"]:
          finalPredictedQuery += attr + " " + op + " " + val
          finalPredictedQuery += " AND "
        finalPredictedQuery = finalPredictedQuery[:-5]
      finalPredictedQuery += ")"
      if where_clause != query_dict["where"][-1]: finalPredictedQuery += " AND "
    finalPredictedQuery += ";"
    return finalPredictedQuery
    


# load json file
with open('done_dict/agg_dict.json') as f:
  agg_dict = json.load(f)

with open('stop_words.json') as f:
  stop_words = json.load(f)

with open('done_dict/where_dict.json') as f:
  where_dict = json.load(f)

with open('done_dict/conditions_dict.json') as f:
  conditions_dict = json.load(f)

# print("conditions_dict",conditions_dict)

# sentence = "get names of employees who are in the department of sales"
sentence = "get minimum and maximum and average of salary and age of the employee"
sentence = "get minimum and maximum and average of salary and age of the employee where first_name and last_name not equal (mona)"
sentence = "get minimum and maximum and average of salary and age of the employee where salary greater than (250) and age greater than (25)"
# sentence = "get salary of employee which is greater than (200) and less than (500)"
# sentence = "get salary and age of the employee where salary greater than (250)"
# sentence = "get employees names with the greatest salary"


query_dict = {
  "entities":[],
  "attributes": [],
  "where": [],
  "agg": [],
  "groupby": [],
  "orderby": []
}
values = separate_values_in_question(sentence)
tokens_dict,tokens = cleanup_question(sentence)
match_tokens_to_schema(tokens_dict,test_schema[0],query_dict)
# print(tokens)
tokens = get_conditions_filters(tokens,conditions_dict)
# print("gggggggggggggggggggggggggggggg",tokens)
conjunctions_sets,reconstructed_question = get_conjunctions_sets(tokens,query_dict,values,conditions_dict,where_dict)
# print(conjunctions_sets,reconstructed_question)
get_where_filters(reconstructed_question,query_dict,conjunctions_sets)
print(conjunctions_sets)
print("----------------------------------")
get_aggregates_in_question(query_dict,reconstructed_question,conjunctions_sets)
print(query_dict)
finalQuery = get_query_from_question(query_dict)
print("----------------------------------")
print("finalQuery =>>>> ", finalQuery)
# print("query_dict",query_dict)
# print("values",values)
# displacy.render(doc, style='dep')
# print(treeRoot,tree)


# print("tokens ",tokens_dict)
# print("--------------------------------------------")
# print("after matching",query_dict)


# doc = nlp(sentence)
# # print(f"{'Node (from)-->':<15} {'Relation':^10} {'-->Node (to)':>15}\n")
# tree = {token.text:[] for token in doc}
# treeRoot = None
# for token in doc:
#     print("{:<15} {:^10} {:>15}".format(str(token.head.text), str(token.dep_), str(token.text)))
#     if token.dep_ == 'ROOT':
#         treeRoot = token.text
#         continue
#     tree[token.head.text].append((token.dep_,token.text))

# DFS(tree, treeRoot, query_dict)

'''
at the beginig (from user) values and numbers in () and we separate 
1- replace from dictionaries (groupby / orderby / where) by verbs
2- TODO:tokenize (without cleaning words) to detect entities and attributes => (belong to detected entities)
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

'''
#TODO: don't use all attributes in select
#TODO: (Having) -> aggregate in where clause
#TODO: groupby and order by
#TODO: testing to get different cases
#TODO: SELECT keyword 
'''
