from scipy import stats
from NlpUtilityFunctions import *
import math

#Classify Example Entity/Attribute to a certain topic
def NearestNeighbour(keyword,topics,model):
  topic_index=0
  cur_similarity=-math.inf
  topic_class='x'
  for index,topic in enumerate(list(topics.keys())):
    for word in topics[topic]['vocab']:
      try:
        sim = model.wv.similarity(word,keyword)
        #print("sim",sim,cur_similarity)
        if(cur_similarity<sim):
          topic_index = index
          topic_class = topic
          cur_similarity = sim
      except Exception as e:
        #print(e)
        continue

  return topic_index,topic_class,cur_similarity

#Classify Schema to a certain topic by taking majority vote on all entities/attributes
def classifySchema(schema,topics,model,debug=False):
  print("Classifying Schema:",schema)
  topics_sims={}
  schema_words_unique = list(set(schema))
  for word in schema_words_unique:
    #print("word",word)
    try:
      _,topic_class,best_similarity = NearestNeighbour(word,topics,model)
      #print("nn_res",nn_res)
      if(topic_class not in topics_sims): topics_sims[topic_class]=0
      topics_sims[topic_class]+=best_similarity
    except Exception as e:
      #print(e)
      continue
  # print(topics_votes)
  # topics_votes = stats.mode(topics_votes)
  # print("Topic",topics_votes)
  max_topic = max(topics_sims, key=topics_sims.get)
  return max_topic

#Match Attribute to nearest attribute name in a certain topic
def classifyAttribute(attr,topic,model):
  if attr in topic['attributes']: return attr,topic['attributes_files'][topic['attributes'].index(attr)]
  clean_attrs = cleanAttribute(attr)
  simWord = ''
  cur_similarity = -math.inf
  attrFile=''
  for i,attr in enumerate(topic['attributes']):
    sim=0
    for clatr in clean_attrs:
      max_sim=0
      for word in topic['attributes_words'][i]:
        try:
          cur_sim = model.wv.similarity(word,clatr)
          if(max_sim<cur_sim):
            max_sim = cur_sim
        except Exception as e:
          continue
      sim+=max_sim
      if cur_similarity<sim:
        cur_similarity = sim
        simWord = attr
        attrFile=topic['attributes_files'][i]
  return simWord,attrFile

#Match Entity to nearest Entity name in a certain topic
def classifyEntity(entity,topic,model):
  if entity in topic['entities']: return entity,topic['entities_files'][topic['entities'].index(entity)]
  clean_attrs = cleanAttribute(entity)
  simWord = ''
  cur_similarity = -math.inf
  entity_file=''
  for i,topic_entity in enumerate(topic['entities']):
    sim=0
    topic_entity_names = cleanAttribute(topic_entity)
    for clatr in clean_attrs:
      max_sim=0
      for word in topic_entity_names:
        try:
          cur_sim = model.wv.similarity(word,clatr)
          if(max_sim<cur_sim):
            max_sim = cur_sim
        except Exception as e:
          continue
      sim+=max_sim
      if cur_similarity<sim:
        cur_similarity = sim
        simWord = topic_entity
        entity_file=topic['entities_files'][i]
  return simWord,entity_file