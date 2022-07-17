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
#from .nlpUtils import *
import re


conjunctions = ['and','or',',','addition','also']
order_direction = ["descending" ,"desc", "descendingly"] #as by default will sort ASC
order_dict = ["order" , "sort" , "arrange"]
group_by_dict = ["every", "each","group"]

def cleanup_question(question,stop_words):
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
    detectedEntities = []
    for _,value in tokens_dict.items():
      isEntity = False
      lemma,pos = value
      if pos == "NOUN" or pos == "VERB":
        # print("my schema",sql_schema)
        # first check if noun matches any of the entities
        print("//////////////////////////////")
        print(sql_schema)
        print(sql_schema.values())
        for ob in sql_schema.values():
          print(ob)
          entityName = ob["TableName"]
          entityLemma = nlp(entityName)
          if lemma.lower() == entityLemma[0].lemma_.lower():
            query_dict["entities"].append((lemma,entityName))
            detectedEntities.append(entityName)
            isEntity = True
            break
           
        # if not matched with any entity try to match with attributes
        if not isEntity: 
          for ob in sql_schema.values():
            entityName = ob["TableName"]
            for attr in ob["attributes"].keys():
              attrLemma = nlp(attr)
              if lemma.lower() == attrLemma[0].lemma_.lower():
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
          ,values_list,conditions_dict,where_dict,agg_dict):
  typesCount = {
    "g": 0,
    "a" : 0,
    "e" : 0,
    "v": 0,
    "c": 0,
    "w": 0,
    "o": 0,
    "d": 0,
    "gb":0,
    "j":0
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

    if item.lower() in where_dict:typesCount["w"] += 1

    if item in values_list:typesCount["v"] += 1
      
    if item in conditions_dict: typesCount["c"] += 1
    
    if item.lower() in order_dict: typesCount["o"] += 1

    if item.lower() in order_direction: 
      tempConjunctions[idx] = "DESC"
      typesCount["d"] += 1

    if item.lower() in group_by_dict: 
      tempConjunctions[idx] = "GROUP BY"
      typesCount["gb"] += 1
    
    if item.lower() in conjunctions:
      if item.lower() == "also" or item.lower() == "addition":
        tempConjunctions[idx] = "AND"
      else:
        tempConjunctions[idx] = item.upper()
      typesCount["j"] += 1

    for k in typesCount.keys():
      if typesCount[k] == len(list(conjunctions_set)):
        setType = k
  return setType,tempConjunctions

def get_conjunctions_sets(tokens,query_dict,values_list,conditions_dict,where_dict,agg_dict):
  #tokens without stopwords and prepositions except conjunctions and negations
  sets_count = {'g':0,'a':0,'e':0,'garbage':0,'w':0,'v':0,'c':0,'o':0,'d':0,"gb":0,"j":0}
  reconstructed_question = tokens[0]
  global conjunctions
  conjunctions_sets = {}
  cur_set = []
  i = 1
  while i <= len(tokens)-1:
    if tokens[i] in conjunctions:
      if tokens[i-1] not in cur_set: cur_set.append(tokens[i-1])
      # cur_set.append(tokens[i])
      if tokens[i+1] not in cur_set: cur_set.append(tokens[i+1])
      i+=1
    elif len(cur_set) > 0:
      conj_type,new_names = get_conjunction_set_type(cur_set,query_dict,values_list,conditions_dict,where_dict,agg_dict)
      if conj_type == 'garbage':
        for el in cur_set :
          conj_type,new_names = get_conjunction_set_type([el],query_dict,values_list,conditions_dict,where_dict,agg_dict)
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
      conj_type,new_names = get_conjunction_set_type([tokens[i]],query_dict,values_list,conditions_dict,where_dict,agg_dict)
      set_name = conj_type  + '_' + str(sets_count[conj_type])
      reconstructed_question += " " + set_name
      sets_count[conj_type] += 1
      conjunctions_sets[set_name] = new_names
    i+=1
  if tokens[-2] not in conjunctions:
    conj_type,new_names = get_conjunction_set_type([tokens[-1]],query_dict,values_list,conditions_dict,where_dict,agg_dict)
    set_name = conj_type + '_' + str(sets_count[conj_type])
    reconstructed_question += " " + set_name
    sets_count[conj_type] += 1
    conjunctions_sets[set_name] = new_names
  return conjunctions_sets,reconstructed_question

def get_aggregates_in_question(query_dict,new_question,conjunctions_sets):
    '''
    get aggregates in question
    return list of aggregates
    '''
    aggrFound = False
    aggrList = []
    totalRelations = []
    usedAggrAttrs = []
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
        usedAggrAttrs = list(conjunctions_sets[rel[1]])
        for aggr in list(conjunctions_sets[rel[0]]):
          for attr in list(conjunctions_sets[rel[1]]):
            query_dict["agg"].append([aggr,attr])
    return usedAggrAttrs

def get_conditions_filters(tokens,conditions_dict):
  joinedQuestion = " ".join(tokens)
  joinedQuestion = joinedQuestion.replace(' as well as ',' and ') 
  #in case of the word written as doesnot / donot / ...
  for word in joinedQuestion.split():
    if word.endswith('not') or word.endswith("n\'t"):
      joinedQuestion = joinedQuestion.replace(word , "not")

  for key,value in conditions_dict.items():
    for c in value:
      joinedQuestion = joinedQuestion.replace(' '+c,' '+key)

  return joinedQuestion.split()

def get_where_group_order_by_filters(reconstructed_question,query_dict,conjunctions_sets):
  ####################### get where #############################
  print("reconstructed_question",reconstructed_question)
  contitions = []
  tempGroupList = []
  tempOrderList = []
  whereAggrList = []
  finalWhereAggrsList = []
  inWhere = False
  groupbyFound = False
  orderbyFound = False
  aggrFound = False
  words = reconstructed_question.split()
  for idx,word in enumerate(words):
    if 'w_' in word:
      inWhere = True
      groupbyFound = False
      orderbyFound = False
      continue
    if inWhere:
      if 'a_' in word and aggrFound == False:
        contitions.append([word])
      elif 'c_' in word or 'v_' in word:
        if len(contitions) == 0:
          i = idx-1
          while i >= 0:
            if 'a_' in words[i]:
              contitions.append([words[i]])
              break
            i-=1
        if len(contitions) > 0: contitions[-1].append(word)
      if'g_' in word:
        whereAggrList.append(word)
        aggrFound = True
      if (aggrFound == True and 'a_' in word):
        whereAggrList.append(word)
        finalWhereAggrsList.append(whereAggrList)
        whereAggrList = []
        if aggrFound == True:
          aggrFound = False
      
          
    if 'o_' in word: 
      orderbyFound = True
      inWhere = False
      groupbyFound = False 
    if orderbyFound:
      if 'a_' in word:
        tempOrderList.extend(conjunctions_sets[word])
      if 'd_' in word and len(tempOrderList) > 0:
        tempOrderList.extend(conjunctions_sets[word])
    if 'gb_' in word: 
      groupbyFound = True
      orderbyFound = False
      inWhere = False
    if groupbyFound:
      if 'a_' in word:
        tempGroupList.extend(conjunctions_sets[word])
  ####################### get where aggrs #######################
  print("finalWhereAggrsList",finalWhereAggrsList)
  for rel in finalWhereAggrsList:
    if (len(rel) == 2):
      for aggr in list(conjunctions_sets[rel[0]]):
        for attr in list(conjunctions_sets[rel[1]]):
          query_dict["whereAggr"].append([aggr,attr])
  ################## get where #####################
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
    if where_clause['op'][0] == "BETWEEN":
      temp = []
      temp.extend(where_clause['op'])
      temp.extend(where_clause['val'])
      where_clause['op_val'] = [tuple(temp)]
    else:
      where_clause['op_val'] = list(zip(where_clause['op'],where_clause['val']))
    query_dict['where'].append(where_clause)

  #################### get order by #######################
  query_dict["orderby"].extend(tempOrderList)

  #################### get group by #######################
  query_dict["groupby"].extend(tempGroupList)


def get_select_attributes(query_dict,reconstructed_question,conjunctions_sets):
  words = reconstructed_question.split()
  isEntityDetected = False
  for _,word in enumerate(words):
    if isEntityDetected == True:
      break
    if 'a_' in word:
      query_dict["selectAttrs"].extend(conjunctions_sets[word])
    if 'e_' in word:
      isEntityDetected = True

def get_query_from_question(query_dict,usedAggrAttrs):
    '''
    get query from question
    return query
    '''
    foundAggBeforeWhere = False
    finalPredictedQuery = "SELECT "
    if len(query_dict["agg"]) > 0:
      if len(query_dict["whereAggr"]) > 0:
        for aggList in query_dict["agg"]:
          for whereAggList in query_dict["whereAggr"]:
            if aggList[0] != whereAggList[0] and aggList[1] != whereAggList[1]:
              finalPredictedQuery += aggList[0] + ' ( ' + aggList[1] + ' ), '
              foundAggBeforeWhere = True
        #finalPredictedQuery = finalPredictedQuery[:-2]
      else:
        for aggList in query_dict["agg"]:
          finalPredictedQuery += aggList[0] + ' ( ' + aggList[1] + ' ), '
          foundAggBeforeWhere = False
        #finalPredictedQuery = finalPredictedQuery[:-2]
   
    if len(usedAggrAttrs) > 0:
      # delete attributes already taken in aggregation from the selection statment
      firstTimeAfterAggr = True
      # for selectAttr in list(list(zip(*query_dict["attributes"]))[2]):
      for selectAttr in query_dict["selectAttrs"]:
        if selectAttr not in usedAggrAttrs:
          if firstTimeAfterAggr == True and foundAggBeforeWhere:
            finalPredictedQuery += ", "
            firstTimeAfterAggr = False
          finalPredictedQuery += selectAttr + ', '

      finalPredictedQuery = finalPredictedQuery[:-2]
    else:
      finalPredictedQuery += ",".join(query_dict["selectAttrs"])
    
    finalPredictedQuery += " FROM " + query_dict["entities"][0][1]
    
    isLike = False
    firstTurn = False
    for where_clause in query_dict["where"]:
      if firstTurn == False:
          finalPredictedQuery += " WHERE "
          firstTurn = True
      if len(where_clause["op_val"]) > 0:
        # if firstTurn == False:
        #   finalPredictedQuery += " WHERE "
        #   firstTurn = True
        finalPredictedQuery += "( "
        for idx,attr in enumerate(where_clause["attr"]):
          if where_clause["op"][0] == "BETWEEN":
            finalPredictedQuery += attr + " " + where_clause["op"][0] + " " + where_clause["val"][0] + " AND " + where_clause["val"][1]
          else:
            for op,val in where_clause["op_val"]:
              if op == "LIKE_S":
                finalPredictedQuery += attr + " LIKE '" + val + "%' AND "
                isLike = True
              if op == "LIKE_C":
                finalPredictedQuery += attr + " LIKE '%" + val + "%' AND "
                isLike = True
              if op == "LIKE_E":
                finalPredictedQuery += attr + " LIKE '%" + val + "' AND "
                isLike = True
              if op == "NOT_LIKE_S":
                finalPredictedQuery += attr + " NOT LIKE '" + val + "%' AND "
                isLike = True
              if op == "NOT_LIKE_C":
                finalPredictedQuery += attr + " NOT LIKE '%" + val + "%' AND "
                isLike = True
              if op == "NOT_LIKE_E":
                finalPredictedQuery += attr + " NOT LIKE '%" + val + "' AND "
                isLike = True
              if isLike == False:
                finalPredictedQuery += attr + " " + op + " " + val
                finalPredictedQuery += " AND "
            finalPredictedQuery = finalPredictedQuery[:-5]
          finalPredictedQuery += " )"
          if where_clause != query_dict["where"][-1]: finalPredictedQuery += " AND "
      elif len(query_dict["whereAggr"]) > 0:
        for attr,op in zip(where_clause["attr"],where_clause["op"]):
          finalPredictedQuery += attr + " " + op + " "
        for whereAggrList in query_dict["whereAggr"]:
          finalPredictedQuery += whereAggrList[0] + ' ( ' + whereAggrList[1] + ' ), '
        finalPredictedQuery = finalPredictedQuery[:-2]

    if len(query_dict["orderby"]) > 0:
      finalPredictedQuery += " ORDER BY"
      for index,orderItem in enumerate(query_dict["orderby"]):
        if orderItem != "DESC" and index != 0:
          finalPredictedQuery += ','
        finalPredictedQuery += " " + orderItem
        
    if len(query_dict["groupby"]) > 0:
      finalPredictedQuery += " GROUP BY "
      for groupItem in query_dict["groupby"]:
        finalPredictedQuery += groupItem + ', '
      finalPredictedQuery = finalPredictedQuery[:-2]

    finalPredictedQuery += ";"
    return finalPredictedQuery
    


query_dict = {
  "entities":[],
  "attributes": [],
  "where": [],
  "agg": [],
  "groupby": [],
  "orderby": [],
  "whereAggr": [],
  "selectAttrs": []
}


######################################## test sentences ########################################
#sentence = "get first_name and salary of employees sorted by age"
sentence = "get minimum and maximum salary of employees for each age"
sentence = "get first_name and maximum salary of employees"
#sentence = "get first_name and last_name then minimum and maximum and average of salary and age of the employee for each salary where salary greater than (250) and age greater than (25) sorted by age desc then first_name then salary desc"
#sentence = "get salary of employee which is greater than (200) and less than (500)"
#sentence = "get first_name of employee where his salary exceeds the average of salary"
#sentence = "get first_name of employee whose first_name doesn't start with (N)"
#sentence = "get first_name and last_name of employee whose age in range of (20) to (30) and salary smaller than (2000)"
#sentence = "get salary and age of the employee where salary greater than (250)"
#sentence = "get first_name of employees with salary equal to the greatest salary"
#sentence = "get first_name and last_name of employees whose first_name starts with (Nihal)"
#sentence = "get first_name and last_name of employees grouped by age whose salary equal to the maximum salary"

import os
def convertNlpToSQLQuery(sentence,finalSchema):
  #os.chdir('NlpToSql')
  # load json files
  with open('done_dict/agg_dict.json') as f:
    agg_dict = json.load(f)

  with open('stop_words.json') as f:
    stop_words = json.load(f)

  with open('done_dict/where_dict.json') as f:
    where_dict = json.load(f)

  with open('done_dict/conditions_dict.json') as f:
    conditions_dict = json.load(f)

  values = separate_values_in_question(sentence)
  tokens_dict,tokens = cleanup_question(sentence,stop_words)
  match_tokens_to_schema(tokens_dict,finalSchema,query_dict)
  tokens = get_conditions_filters(tokens,conditions_dict)
  conjunctions_sets,reconstructed_question = get_conjunctions_sets(tokens,query_dict,values,conditions_dict,where_dict,agg_dict)
  get_where_group_order_by_filters(reconstructed_question,query_dict,conjunctions_sets)
  get_select_attributes(query_dict,reconstructed_question,conjunctions_sets)
  print(conjunctions_sets)
  print(reconstructed_question)
  usedAggrAttrs = get_aggregates_in_question(query_dict,reconstructed_question,conjunctions_sets)
  finalQuery = get_query_from_question(query_dict,usedAggrAttrs)
  return finalQuery


test2 = {
    1: {
        "TableName": "articles",
        "attributes":{
            "aid": "str",
            "textbody": "str",
            "timestamp": "str",
            "title": "str",
            "users_writes_userid": "str",
        }
    },
    2: {
        "TableName": "users",
        "attributes":{
            "email": "str",
            "name": "str",
            "userid": "str"
        }
    },
    3:{
        "TableName": "comments",
        "attributes":{
            "articles_has_aid": "str",
            "cid": "str",
            "text": "str",
            "timestamp": "int",
            "users_posts_userid": "str"
        }
    }
}
#sentence = "get title and textbody of articles whose title starts with (good)"
# sentence = "get first_name of employees ordered by salary then age"
# finalQuery = convertNlpToSQLQuery(sentence,test_schema[0])
# print("finalQuery ==> " , finalQuery)

'''
#TODO: don't use all attributes in select   ==> done
#TODO: (Having) -> aggregate in where clause  ==> done only for one condition for one attribute
#TODO: groupby ==> done
#TODO: order by ==> done
#TODO: testing to get different cases
#TODO: SELECT keyword 
#TODO: try to instead of separating garbage then check type only check type for first one then start with the second one again
#TODO: fill in dictionaries
#TODO: like  ==> done
#TODO: between  ==> done
#TODO: remove not attributes in select  ==> done
#TODO: or / and 
'''

############################ important #####################
# to order by multiple columns use then
# after each column write desc or leave it empty to the default (asc)

# if you want to select attributes with aggregation write attributes then write (then) then write aggregations 
# if you want to get list of same type of and then take care if there someting before use then

# aggreagtion then attributes not (viceversa)

# where followed by attributes and conditions and values or aggregation if needed

# till now take care of keywords existed in dictionaries for correct replacement 

# having only with one condition and one attribute

#write entity after attributes not before