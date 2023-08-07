import re
import spacy
nlp = spacy.load('en_core_web_sm')

def camel_case_paskal_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

def cleanName(colName):
    #remove names with one character 
    if len(colName) <= 1: return colName
    #seperate pascal and camel cases
    Names = camel_case_paskal_split(colName)
    clean_Names=[]
    for name in Names:
      #remove names that are only numbers
      result = re.search("^[ 0-9]+$", name)
      if result is not None: continue
      #remove numbers at the end of the string 
      name = re.sub("[0-9]+$", '', name)
      #lower
      name = name.lower()
      lemma = nlp(name)[0].lemma_
      clean_Names.append(lemma)
      
    return clean_Names
    
def cleanFullName(fullName):
  fullName = fullName.strip()
  fullName = re.split('_| |-',fullName)
  entity_clean=[]
  for name in fullName:
    clean_name = cleanName(name)
    entity_clean.extend(clean_name)
  return ' '.join(entity_clean)
