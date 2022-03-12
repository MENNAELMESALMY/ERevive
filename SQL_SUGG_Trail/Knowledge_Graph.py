from random import sample


#Utility Functions
#This is FreeBase to Wikidata mapping
def mapIdsToEntities(wikifb_file_path):
    wikifb_file = open(wikifb_file_path,'r')
    fbwikilines = wikifb_file.readlines()
    freeBase_to_Wikis = {}
    for line in fbwikilines:
        key = line.split()[0]
        freeBase_to_Wikis[key] = line[len(key)+1:-1]
    return freeBase_to_Wikis

#GLobal Variables
entitiesTable = {}
#Params
#path to file of KG in format: subject_entity_id relations===edges object_entity_id
#path to file with mapped ids to entities
#Returns Graph structure for KG
def init_KG(KG_file_path,wikifb_file_path):
    freeBase_to_Wikis = mapIdsToEntities(wikifb_file_path)
    file_lines = KG_file.readlines()
    subjects,objects={}
    for line in file_lines:
        triple = line.split("\t")
        triple[2]=triple[2][:-1]
        if freeBase_to_Wikis.get(triple[0]) is None or  freeBase_to_Wikis.get(triple[2]) is None: continue
        entity_from,relation, entity_to = freeBase_to_Wikis[triple[0]],triple[1],freeBase_to_Wikis[triple[2]]

        if (subjects.get(entity_from) is None): subjects[entity_from] = []
        subjects[entity_from].add((relation,entity_to))

        if (objects.get(entity_to) is None): objects[entity_to] = []
        objects[entity_to].add((relation,entity_from))
    return subjects,objects

def generateCols(entity_neighbors,entity,entityType,table):
    for pred,obj in entity_neighbors:
        col={}
        col['Predicate'] = pred.split('.')[1:]
        col['Subject'] = entity if entityType == 's' else obj
        col['Object'] = obj if entityType == 's' else entity
        
        #sentence = col['Subject'] + col['Predicate'][0] + col['Object']
        # and doc.ents[0].text == col['Subject']
        doc = nlp(col['Subject'])
        ner = [col['Subject']]
        if len(doc.ents):
            ner = doc.ents[0].label_ 
            ner = spacy.explain(ner)
            domains = re.split( ', |or',ner)
            ner = [ d for d in domains ]

        col['Domain'] = ner[:]
        doc = nlp(col['Object'])
        ner = [col['Object']]
        if len(doc.ents):
            ner = doc.ents[0].label_ 
            ranges = spacy.explain(ner).split(',')
            ranges = re.split( ', |or',ner)
            ner = [ r for r in ranges ]
        col['Range'] = ner[:]
        table.append(col)
    return table

def tableFromEntity(entity,subjects,objects):
  # Subject, Domain => NER of subject, predicate, object, Range => NER of object
    if entity in entitiesTable:
        return entitiesTable[entity]
    table = []
    entity_subjects = subjects.get(entity,[])
    table = generateCols(entity_subjects,entity,'s',table)

    entity_objects = objects.get(entity,[])
    table = generateCols(entity_objects,entity,'o',table)
  
    entitiesTable[entity] = table
    return table

def createEntityKeywords(entity,subjects,objects):
  #TODO: clean input scehma entities
  table = tableFromEntity(entity,subjects,objects)
  cols=[]
  for col in table:
    #####################################
    uniq_pred = list(set(col['Predicate']))
    Predicate = sample(uniq_pred,2)
    Subject = list(set(col['Subject']))
    Object = list(set(col['Object']))
    Domain = list(set([ d for d in col['Domain']]))
    Range = list(set([ r for r in col['Range']]))
    ##########################################
    colWords = [Subject] + Domain + Predicate + [Object] + Range
    cols.append(colWords)
  return cols

############################################

#TODO:
#can be connected in a graph for easier search instead of linear search
def mapEntity(entity,subjects,objects):
  #n4of hya 22rb l2ni entity fel KG
  #ne assignlha 2l table bta3ha
  #keywords given entity
  entity_res=None
  cur_similarity = -math.inf
  for entity_kg in subjects:
    entity_attrs = cleanAttribute(entity_kg,"K")
    entity_similarity = 0
    for attr in entity_attrs:
      try:
        entity_similarity += model.wv.similarity(entity,entity_kg)
      except Exception as e:
        print(e)
    entity_similarity = entity_similarity/len(entity_attrs)
    if entity_similarity>cur_similarity:
      entity_res = entity_kg
      cur_similarity = entity_similarity
  for entity_kg in objects:
    entity_attrs = cleanAttribute(entity_kg,"K")
    entity_similarity = 0
    for attr in entity_attrs:
      try:
        entity_similarity += model.wv.similarity(entity,entity_kg)
      except Exception as e:
        print(e)
    entity_similarity = entity_similarity/len(entity_attrs)
    if entity_similarity>cur_similarity:
      entity_res = entity_kg
      cur_similarity = entity_similarity
  return entity_res

def mappedKeywordsEntity(entity,subjects,objects):
  mapped_entity = mapEntity(entity,subjects,objects)
  keywords =  createEntityKeywords(mapped_entity,subjects,objects)
  print(mapped_entity)
  print(keywords)
  print('-------------------------------------------')
  return keywords