from ClassifySchema import *
from SchemaGraph import *
from NlpUtilityFunctions import *
from SQLSUGG_Probabilties import *
from LoadGraphs import *
import copy
def getSchemaCleanMetaDate(entities):
  clean_names=[]
  for entity in entities:
    clean_entity = cleanAttribute(entity.name)
    clean_names.extend(clean_entity)
    for attr in entity.attributes:
      clean_attrs = cleanAttribute(attr)
      clean_names.extend(clean_attrs)
  return clean_names


def inputSchema(schemaFilesPaths,topics,model):
  topics_keys = list(topics.keys())
  schema_input_graph = createGraphSchema(schemaFilesPaths)
  cleanMetaData = getSchemaCleanMetaDate(schema_input_graph.nodes)
  schemaTopic = classifySchema(cleanMetaData,topics,model)
  topic  = loadTopic(schemaTopic)
  topic.update(topics[schemaTopic])
  for node in schema_input_graph.nodes:
    mapped_entity,mapped_db = classifyEntity(node.name,topic,model)
    print(mapped_db,schemaTopic)
    mapped_schemagraph = topic['graphs'][mapped_db]
    mapped_file = "/content/keywords2SQL/"+schemaTopic+"/"+ mapped_db+'_'+mapped_entity+'.csv'
    mapped_entity_node = topic['graphs'][mapped_db].node_map[mapped_entity]
    node.set_mapped_entity({"entity":mapped_entity,"node":mapped_entity_node,"file":mapped_file,"db":mapped_db,'schemagraph':mapped_schemagraph})

    mapped_attributes = {}
    for attr in node.attributes:
      mapAttr,mapFile = classifyAttribute(attr,topic,model)
      mapped_attributes[attr]= {"attr":mapAttr,"file":mapFile}

    node.set_mapped_attributes(mapped_attributes)
  return schema_input_graph,schemaTopic,topic



def ingestInputSchema(schema_input_graph,T,INV,FWD,topic,keywords=None):
  for entity in schema_input_graph.nodes:
    mapEntity = entity.mapped_entity
    entity.PR = mapEntity['node'].PR
 
  if keywords is None:
    Qs = []
    for entity in schema_input_graph.nodes:
      Q = mappedKeywordsEntity(entity.name)
      Qs.extend(Q)
  else: 
    Qs = keywords
  return Qs_pipeline_generation(Qs,T,INV,FWD,schema_input_graph,topic)



def Qs_pipeline_generation(Qs,T,INV,FWD,schema_input_graph,topic):
  for Q in Qs:
    entity_alpha={}
    alphas=[]
    for entity in schema_input_graph.nodes:
      mapEntity = entity.mapped_entity
      alpha_r = 0
      for k in Q:
        alpha_r+=getKgivenR(k,mapEntity['entity'],mapEntity['schemagraph'],mapEntity['file'],topic)
      alphas.append(alpha_r)
    alphas = [float(alpha)/sum(alphas) for alpha in alphas]
    for i,entity in enumerate(schema_input_graph.nodes):
      entity_alpha[entity.name]=alphas[i]
    print(entity_alpha)
    top_one_T = getTopGeneratedTemplate(entity_alpha,T,INV,FWD,schema_input_graph)
    #call generateSqlModuleWithThe_T
    return top_one_T

def getPRWithT(R,T,FWD,schema_input_graph):
  rs = FWD[T]
  prs=[]
  r_index = 0
  for i,r in enumerate(rs):
    if r==R:
      r_index = i
    node_pr = schema_input_graph.node_map[r].PR
    prs.append(node_pr)
  prs = [float(pr)/sum(prs) for pr in prs]
  return prs[r_index]

def getPRT(R,T,INV):
  for t in INV[R]:
    if t['T']==T: return t['PRT']
  return 0

def getTopKTemplates(K,INV,FWD,schema_input_graph,entity_alpha):
  beta = 0
  R_Set = []
  entities = schema_input_graph.nodes
  current_step=0
  while len(R_Set)<K:
    Tlist = [INV[r.name][current_step] for r in entities if current_step<len(INV[r.name]) and entity_alpha[r.name]!=0]
    beta = sum([t['PRT']*t['alpha_r'] for t in Tlist])
    for t in Tlist:#
      t_pqt = sum([entity_alpha[r]*getPRT(r,t['T'],INV) for r in FWD[t['T']] if entity_alpha[r]!=0 ])
      if t_pqt>=beta:
        R_Set.append(t)
    current_step+=1
  return R_Set

def getTopGeneratedTemplate(entity_alpha,T,INV,FWD,schema_input_graph):
  INV_copy = copy.deepcopy(INV)
  for entity in schema_input_graph.nodes:
    alpha_r = entity_alpha[entity.name]
    if alpha_r!=0:
      entity_templates = INV[entity.name]
      entitySortedTemplates = []
      for T in entity_templates:
        prt = getPRWithT(entity.name,T,FWD,schema_input_graph)
        entitySortedTemplates.append({'T':T,'PRT':prt,'alpha_r':alpha_r})
      entitySortedTemplates = sorted(entitySortedTemplates, key=lambda item: item['PRT'])
      INV_copy[entity.name] = entitySortedTemplates
  INV = INV_copy
  return getTopKTemplates(1,INV,FWD,schema_input_graph,entity_alpha)


