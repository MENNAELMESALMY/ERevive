
import re

stop_words = ["desc","asc"]
AggrFunctions = ["count","sum","min","max","avg"]
tokensToSkip = [",","(",")",".","by","distinct",";","-","null"]
endOfWhere = ["and","or","in","not","union","intersect","except","like"]
whereClauseEnd = ["group","order","limit","offset","having"]



def camel_case_paskal_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]
def cleanColName(colName):
    colNames = camel_case_paskal_split(colName)
    newColNames=[]
    for name in colNames:
      name = name.lower()
      newColNames.append(name)
    return newColNames

def cleanWord(token):
  token = token.strip()
  entityAlias=''
  splittedTokens = []
  ## clean entities if existed
  if token.find(".") != -1:
    splittedTokens = token.split(".")
    # first element is the entity, second element is the attribute
    entityTokens = re.split('_| |-',splittedTokens[0])
    entities_clean = []
    for token in entityTokens:
      cleanedToken = cleanColName(token)
      entities_clean.extend(cleanedToken)
    entityAlias = "_".join(entities_clean) + '.'
    token = splittedTokens[1]
  ## clean attributes
  attributes_clean=[]
  attributeTokens = re.split('_| |-',token)
  for token in attributeTokens:
    cleanedToken = cleanColName(token)
    attributes_clean.extend(cleanedToken)
  finalCleanedAttrs = "_".join(attributes_clean)
  return entityAlias+finalCleanedAttrs
#################################################################
def cleanTokens(tokens):
  cleaned_tokens = []
  for token in tokens:
    cleaned_tokens.append(cleanWord(token))
  return cleaned_tokens

def fixWhereClause(whereClauseInfo):
    if len(whereClauseInfo) == 2:
        whereClauseInfo.append("value")
    if len(whereClauseInfo) == 3 and whereClauseInfo[2] in ["and","or"]:
        tempCondition = whereClauseInfo.pop()
        whereClauseInfo.append("value")
        whereClauseInfo.append(tempCondition)
    if len(whereClauseInfo) == 3:
        whereClauseInfo.append("None")
    return whereClauseInfo
def getEntitiesAliasesMapping(query):
    entities_aliases = {}
    i = 0
    while i < len(query):
        token = query[i]
        if token == 'as':
            entity = query[i-1]
            alias = query[i+1]
            entities_aliases[alias] = entity
        i+=1
    return entities_aliases
def parse_query(realQuery):
    tokensList = re.split('(\W)', realQuery)
    tokensList = list(filter(None, tokensList))
    tokensList = list(filter(lambda x: x != ' ', tokensList))
    convertedTokensList = (map(lambda x: x.lower(), tokensList))
    query = list(convertedTokensList)
    entities = []
    selectAttrs = []
    joinAttrs = []
    groupByAttrs = []
    orderByAttrs = []
    aggrAttrs = []
    whereAttrs = []
    havingAttrs =[]
    aliases = getEntitiesAliasesMapping(query)
    i = 0
    token = ""
    wordType = ""
    orderFunction = ""
    aggrType = ""
    whereClauseInfo = []
    while i < len(query):
        token = query[i]
        if token == "select":
            wordType = "select"
            i += 1
            continue
        if token in stop_words:
            i += 1
            continue
        if token == "limit":
            i += 2
            continue
        if (token[0] == "'" or token[0] == '"') and (token[len(token)-1] == "'" or token[len(token)-1] == '"') and len(token) != 1:
            i+=1
            continue
        if token.find('\"') != -1 or token.find("'") != -1 or token.find('"') != -1 or token.find("%") != -1:
            #find the next same token
            i+=1
            while i < len(query) and query[i]!=token:
                i+=1
            i += 1
            continue
        if token in tokensToSkip:
            if token == ")" and wordType == "aggr":
                wordType = "select"
            if token == "(" and wordType in ["whereClause","havingClause"] and query[i-1]=="in":
                open_bracket = 1
                i+=1
                while i<len(query) and open_bracket >=1:
                    token = query[i]
                    if token == '(': open_bracket += 1
                    elif token == ')': open_bracket -= 1
                    if open_bracket == 0: break
                    i+=1
            i += 1
            continue
        if token == 'as':
            i+=2
            continue 
        if token == "group":
            wordType = "groupBy"
            i += 2
            continue
        if token == "order":
            wordType = "orderBy"
            if query[i+2] in AggrFunctions:
                orderFunction = query[i+2]
                i += 3
            else: 
                orderFunction = ""
                i += 2
            continue
        if token == "having":
            wordType = "havingClause"
            i += 1
            continue
        if token in AggrFunctions and wordType=="havingClause":
            whereClauseInfo.append(token)
            i += 1
            continue    
        if token in AggrFunctions and wordType!="havingClause":
            wordType = "aggr"
            aggrType = token
            i+= 1
            continue
        if token == "from" or token == "join":
            wordType = "entity"
            i += 1
            continue
        if token == "where":
            wordType = "whereClause"
            i += 1
            continue     
        if token == "on":
            wordType = "join"
            i += 1
            continue
        if len(whereClauseInfo)==2 and token.find("var")!=-1:
            i += 1
            continue
        # check for numbers to skip
        if re.match(r'[0-9]+',token):
            i += 1
            continue
        if wordType in ["select","groupBy","orderBy","whereClause","join","aggr","havingClause"]:
            if i+1 < len(query) and query[i+1] == ".":
                token = aliases.get(token,token)
                token = token + "."+query[i+2]
                i += 2
        if wordType in ["whereClause","havingClause"] :
            if token not in endOfWhere:
                if token in ["!",">","<"] and query[i+1] == "=":
                    token += query[i+1]
                    i += 1
                whereClauseInfo.append(token)
                if i+1<len(query) and query[i+1] not in whereClauseEnd:       
                    i += 1
                    continue
            if token == "like":
                whereClauseInfo.append(token)
                i += 1
                continue
            if token == "not" and query[i+1] in ["in","like","is"]:
                token = token + ' ' + query[i+1]
                whereClauseInfo.append(token)
                i += 1
            ### end of where condition (and , or , in)
            if token in ["and","or","in"]:
                if len(whereClauseInfo) > 0:
                    whereClauseInfo.append(token)
                else:
                    i += 1
                    continue
                
        if token in ["union","intersect","except"]:
            i += 1
            continue
        if token == "=" and wordType != "whereClause":
            i += 1
            continue
        token = cleanTokens([token])[0]
        
        if wordType == "select":
            selectAttrs.append(token)
        elif wordType == "entity":
            entities.append(token)
        elif wordType == "join":
            joinAttrs.append(token)
        elif wordType == "groupBy":
            groupByAttrs.append(token)
        elif wordType == "orderBy":
            orderByAttrs.append((token, orderFunction))
        elif wordType == "aggr":
            aggrAttrs.append((token,aggrType))
            aggrType = ""
        elif wordType == "whereClause":
            whereClauseInfo = fixWhereClause(whereClauseInfo)
            if len(whereClauseInfo) > 0:
                whereAttrs.append(whereClauseInfo)
                whereClauseInfo = []
                if i+1 < len(query) and query[i+1].find("var")!=-1:
                    i += 1
        elif wordType == "havingClause": 
            if len(whereClauseInfo) > 0:
                havingAttrs.append(whereClauseInfo)
                whereClauseInfo = []
                if i+1 < len(query) and query[i+1].find("var")!=-1:
                    i += 1
        i += 1
    if len(whereClauseInfo) != 0:
        if wordType == "whereClause":
            whereClauseInfo = fixWhereClause(whereClauseInfo)
            whereAttrs.append(whereClauseInfo)
            whereClauseInfo = []
        elif wordType == "havingClause":
            havingAttrs.append(whereClauseInfo)
            whereClauseInfo = []
    if len(whereAttrs) > 0:
        if len(whereAttrs[-1]) == 4:
            if whereAttrs[-1][3] in ["and","or"]:
                whereAttrs[-1][3] = "None"
    tempDict = {}
    tempDict["query"] = realQuery
    tempDict["entities"] = list(entities)
    tempDict["selectAttrs"] = list(selectAttrs)
    tempDict["joinAttrs"] = list(joinAttrs)
    tempDict["groupByAttrs"] = list(groupByAttrs)
    tempDict["orderByAttrs"] = list(orderByAttrs)
    tempDict["aggrAttrs"] = list(aggrAttrs)
    tempDict["whereAttrs"] = list(whereAttrs)
    tempDict["havingAttrs"] = list(havingAttrs)
    return tempDict