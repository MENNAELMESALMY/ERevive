import os
import re
#get available sql topics
#format : topicName_db_name = [list of schemas]
def get_sql_topics(filesql):
  sql_topics = {}
  filelines = open(filesql,'r').readlines()
  for line in filelines:
    line = line.replace('"','').replace('\n','')
    topic_name = line.split('_')[0]
    sql_topics[topic_name] = line[line.find('[')+1:line.find(']')].split(",")
  return sql_topics

def get_topics_names(filesql):
  topics_names = []
  filelines = open(filesql,'r').readlines()
  for line in filelines:
    line = line.replace('"','').replace('\n','')
    topic_name = line.split('_')[0]
    topics_names.append(topic_name)
  return topics_names

#Parse and return files belonging to a specific schema => All entities in schema
def get_db_files(db,topic,schema_path,data_path,dbs):
  topic_schema_path = schema_path+topic
  topic_data_path = data_path+topic
  schemafiles = os.listdir(topic_schema_path)
  datafiles = os.listdir(topic_data_path)
  if db.find('_')!=-1:
    db_schemafiles=[topic_schema_path+"/"+sf for sf in schemafiles if sf[sf.rfind('/')+1:sf.find('_',sf.find('_')+1)]==db and sf.find('.ipynb_checkpoints')==-1]
    db_datafiles=[topic_data_path+"/"+sf for sf in datafiles if sf[sf.rfind('/')+1:sf.find('_',sf.find('_')+1)]==db and sf.find('.ipynb_checkpoints')==-1]
  else:
    db_schemafiles=[topic_schema_path+"/"+sf for sf in schemafiles if sf[sf.rfind('/')+1:sf.find('_')]==db and sf[sf.rfind('/')+1:sf.find('_',sf.find('_')+1)] not in dbs and sf.find('.ipynb_checkpoints')==-1]
    db_datafiles=[topic_data_path+"/"+sf for sf in datafiles if sf[sf.rfind('/')+1:sf.find('_')]==db and sf[sf.rfind('/')+1:sf.find('_',sf.find('_')+1)] not in dbs and sf.find('.ipynb_checkpoints')==-1]
  return db_schemafiles,db_datafiles

def create_topics_graphs(sql_topics,schemasfiles_path,datafiles_path):
  topics = {}
  for topic,schemas in sql_topics.items(): 
    topics[topic]={'graphs':{},'entities':[],'entities_files':[]} 
    for schema in schemas:
      db_schemafiles_paths,db_datafiles_paths = get_db_files(schema,topic,schemasfiles_path,datafiles_path,schemas)
      datagraph , schemagraph = construct_data_graph(db_schemafiles_paths,db_datafiles_paths)
      add_graph_edges(datagraph,schemagraph)
      topics[filename]['graphs'].update({db:(schemagraph , datagraph)})
      topics[filename]['entities'].extend([node.name for node in schemagraph.nodes])
      topics[filename]['entities_files'].extend([db for node in schemagraph.nodes])
  return topics

#####################Inference############################
# datafiles_path = './keywords2SQL/'
# schemasfiles_path = './schemas/'
# sql_topics = get_sql_topics('TopicsDataBases.txt')
# topics = create_topics_graphs(sql_topics)


  
