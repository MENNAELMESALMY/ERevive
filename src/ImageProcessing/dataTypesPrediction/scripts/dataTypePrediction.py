import re
import pickle
import json
from os import path
from sklearn.feature_extraction.text import TfidfVectorizer

def extractNewWordFeatures(word):
    scriptPath = path.dirname(path.abspath(__file__))
    folderPath = path.dirname(scriptPath)
    oldtfidf = pickle.load(open(folderPath+"/modelOutput/TfidfVocabulary.pkl", 'rb'))
    
    ##print(oldtfidf)
    tfidf = TfidfVectorizer(encoding='latin-1', 
                            max_df=0.4662381347098422,
                            min_df=2, 
                            ngram_range=(1, 3),
                            sublinear_tf=True, 
                            token_pattern='\\w{1,}',
                            vocabulary = oldtfidf)
    

    features = tfidf.fit_transform(word)
    return features

def cleanColName(colName):
    #remove names with one character 
    if len(colName) <= 1:
        return colName
    
    #remove names that are only numbers
    result = re.search("^[ 0-9]+$", colName)
    if result is not None:
        return colName
    
    #remove numbers at the end of the string 
    colName = re.sub("[0-9]+$", '', colName)
    
    #replace _ with space
    colName = colName.replace("_"," ")

    #replace - with space
    colName = colName.replace("-"," ")
    
    #if all capital cases make it small or if it seperated by spaces
    if colName.isupper() == True or len(colName.split()) > 1:
        colName = colName.lower()
    
    #seperate pascal
    if re.search('^[a-z]+[A-Z]+', colName) is not None:
        words = re.findall('[A-Z][^A-Z]*', colName)
        if len(words) > 1 and len(words[0]) == 1 and len(words[1]) == 1:
            result = ''.join(words) 
        else:
            result = ' '.join(words) 
        colName = colName.split(re.findall('[A-Z][^A-Z]*', colName)[0])[0]+' ' + result
        colName = colName.lower()
    
    #seperate camal cases
    if len(re.findall('[A-Z][^A-Z]*', colName)) >0:
        words = re.findall('[A-Z][^A-Z]*', colName)
        newWords = []  
        i = 0 
        while i<len(words):
            if i+1<len(words) and len(words[i])==1 and len(words[i+1])==1:
                newWords.append(words[i]+words[i+1])
                i+=1
            else:
                newWords.append(words[i])
            i+=1
        colName = ' '.join(newWords)
      
    #remove multiple spaces
    colName = ' '.join(colName.split())
    
    #convert to lower case
    colName = colName.lower()
    return colName

def loadModelAndDict(modelName,dictName):
    model = pickle.load(open(modelName, 'rb'))
    id_to_category = json.load(open(dictName))
    return model , id_to_category

def predictWordsTypes(words):
    scriptPath = path.dirname(path.abspath(__file__))
    folderPath = path.dirname(scriptPath)
    model , id_to_category = loadModelAndDict(folderPath+"/modelOutput/model.sav",folderPath+"/modelOutput/id_to_category.txt")

    cleaned_words = [cleanColName(i) for i in words]

    #print(words)
    #print(cleaned_words)

    features = extractNewWordFeatures(cleaned_words)
    preds = model.predict(features)

    outTypes = [id_to_category[str(i)] for i in preds]
    #dic = dict(zip(words,outTypes))
    return outTypes



words = ["name","sex","birth_date","relationship","hours","name","budget","location","locations","ssn","status","salary","address","first_name","middle_initial","last_name","start_date"]
#print(predictWordsTypes(words)[0])
##print(predictWordsTypes(words)[1])