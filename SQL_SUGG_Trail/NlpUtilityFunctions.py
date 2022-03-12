import re
def camel_case_paskal_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

def cleanColName(colName,type="attribute"):
    #remove names with one character 
    if len(colName) <= 1: return colName
    #seperate pascal and camel cases
    colNames = camel_case_paskal_split(colName)
    newColNames=[]
    for name in colNames:
      if type=="attribute":
      #remove names that are only numbers
        result = re.search("^[ 0-9]+$", name)
        if result is not None: continue
        #remove numbers at the end of the string 
        name = re.sub("[0-9]+$", '', name)
      #lower
      name = name.lower()
      newColNames.append(name)
      
    return newColNames
    
def cleanAttribute(attribute,type="attribute"):
  attribute = attribute.strip()
  attribute = re.split('_| |-',attribute)
  attributes_clean=[]
  for att in attribute:
    atts = cleanColName(att,type)
    attributes_clean.extend(atts)
  return attributes_clean


def load_word2vec_model():
  word2vec_model_path = api.load("word2vec-google-news-300", return_path=True)
  model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_model_path, binary=True)
  return model