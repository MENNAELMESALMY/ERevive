import json
import os
wikisql_path = "/home/nada/GP/search engine/datasets/WikiSQL-master/data"
queriesFile = open(wikisql_path + '/queries.jsonl','w')
def prepareData():
    wikisql_files = os.listdir(wikisql_path)
    trains=["dev.jsonl","train.jsonl","test.jsonl"]
    for wikisql_file in wikisql_files:
        if wikisql_file in trains:
            file = open(wikisql_path + '/' + wikisql_file)
            for line in file:    
                line = json.loads(line)
                parseSqlQuery(line)



tables={}
def get_tables():
    trains=["dev","train","test"]
    for train in trains:
        file = open(wikisql_path + '/' + train+".tables.jsonl")
        for line in file:
            line = json.loads(line)
            tables[line['id']]=line

def parseSqlQuery(dataObject):
    agg_ops = ['', 'MAX', 'MIN', 'COUNT', 'SUM', 'AVG']
    cond_ops = ['=', '>', '<', 'OP']
    queryParsed='SELECT '
    query = dataObject['sql']
    queryTableId = dataObject['table_id']
    queryTable = tables[queryTableId]
    selectColumnIndex = query['sel']
    selectColumn = queryTable['header'][selectColumnIndex]
    selectColumn = selectColumn.replace(" ","_").replace('/','_')
    aggOperatorIndex = query['agg']
    aggOperator = agg_ops[aggOperatorIndex]
    queryTable['name'] = queryTable['page_title']
    if aggOperator != '':
        selectColumn = aggOperator + '(' + selectColumn + ')'
    queryParsed += selectColumn + ' FROM ' + queryTable['name'].replace(" ","_").replace('/','_')
    conditions = query['conds']
    queryParsed += ' WHERE '
    for i,condition in enumerate(conditions):
        if i<len(conditions)-1:
            andCond=' AND '
        else:
            andCond=''  
        conditionColumnIndex = condition[0]
        conditionColumn = queryTable['header'][conditionColumnIndex]
        condOperatorIndex = condition[1]
        conditionOperator = cond_ops[condOperatorIndex]
        conditionValue = condition[2]
        conditionColumn = conditionColumn.replace(' ','_').replace('/','_')
        queryParsed +=  conditionColumn + ' ' + conditionOperator + ' ' + str(conditionValue) + andCond
    queriesFile.write(json.dumps(queryParsed) + '\n')



get_tables()
prepareData()