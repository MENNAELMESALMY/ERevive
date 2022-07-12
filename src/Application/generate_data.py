#import spacy
import difflib
import random
import json
import re
import datetime
import itertools
import timeit
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sqlalchemy import create_engine
from faker_classes import faker_classes_mapper , pk_faker_classes


def clean_word(colName , stopwords):
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

    #seperate words
    colName = colName.split(" ")

    #remove stop words and stem
    porter = PorterStemmer()
    colName = [porter.stem(word) for word in colName if word not in stopwords]

    return colName


def match(attr,faker_class):
    max_len = max(len(attr),len(faker_class))
    score = 0
    if max_len == 0:
        return score
    for word in attr:
        if word in faker_class:
            score += 1
    return score/max_len


def get_keys_attrs(model):
    attributes = model["attributes"].copy()
    primary_keys = {}
    foriegn_keys = {}
    for fk in model["ForgeinKey"]:
        foriegn_keys[fk["attributeName"]] = fk
        del attributes[fk["attributeName"]]

    for pk in model["primaryKey"]:
        if pk in attributes.keys():
            primary_keys[pk] = attributes[pk]
            del attributes[pk]
        else:
            primary_keys[pk] = foriegn_keys[pk]["dataType"]
    
    return attributes, primary_keys, foriegn_keys


def mapping_model_to_faker(stop_words, classes, attributes, primary_keys):
    attr_pk = (attributes.copy())
    attr_pk.update(primary_keys)
    attr_pk_mapping= {}

    for attr , datatype in attr_pk.items():
        attr_cleaned = clean_word(attr,stop_words)
        max_score,best_match = 0,None

        for faker_class in faker_classes_mapper.keys():
            faker_class_cleaned = clean_word(faker_class,stop_words)
            score = match(attr_cleaned,faker_class_cleaned)
            
            value = faker_classes_mapper[faker_class]()
            same_type = isinstance(value,classes[datatype])

            if score > max_score and same_type:
                max_score = score
                best_match = faker_class
        
        if not best_match:
            best_match = datatype

        attr_pk_mapping[attr] = best_match
 
    return attr_pk_mapping


def fill_model_statment(num_of_records, attr_pk_mapping, primary_keys):
    pk = primary_keys
    values = []
    i = 0
    stmt = ""
    for attr,faker_class in attr_pk_mapping.items():
        if attr in pk:
            continue

        stmt += attr +', '
        values.append([])
        for _ in range(num_of_records):
            value = faker_classes_mapper[faker_class]()

            if isinstance(value,str) or isinstance(value,datetime.datetime):
                values[i].append(str(value))
            else:
                values[i].append(value)

        i+=1
    return values,stmt[:-2]


def get_pk_data(primary_keys,attr_pk_mapping,num_of_records):
    values = {}
    for i,pk in enumerate(primary_keys):
        values[pk] = []
        faker_class = attr_pk_mapping[pk]
        for _ in range(num_of_records):
            value = pk_faker_classes[faker_class]()
            if isinstance(value,str) or isinstance(value,datetime.datetime):
                values[pk].append(str(value))
            else:
                values[pk].append(value)
    return values


def get_fk_data(model,pks_data,num_of_records):
    stmt = ""
    values = []
    for fk in model:
        stmt += fk["attributeName"] + ', '
        table = fk["ForignKeyTable"]
        attr = fk["ForignKeyTableAttributeName"]
        pk = pks_data[table][attr]
        pk = random.choices(pk , k = num_of_records)
        values.append(pk)
    return values,stmt[:-2]


def __main__():
    with open("./modelsObjects.json","r") as file:
        models = json.load(file)

    classes = {
        'str':str,
        'int':int,
        'float':float,
        'bool':bool,
        'datetime':datetime.datetime
    }

    stop_words = stopwords.words('english')
    attr_pk_mapping = {}
    models_fk = {}
    num_of_records = 100

    user="root"
    password="admin<3Super"
    database="department"
    connection_string = "mysql+mysqlconnector://{0}:{1}@127.0.0.1:3306/{2}".format(user, password, database) 
    engine = create_engine(connection_string)

    pks_data = {}
    stmts = []
    with engine.begin() as conn:
        start = timeit.default_timer()

        #insert attrs and primary keys
        for model_name , model in models.items():
            #print("//////////////////////////////////////")
            attributes, primary_keys, foriegn_keys = get_keys_attrs(model)
            models_fk[model_name] = foriegn_keys
            attr_pk_mapping[model_name] = mapping_model_to_faker(stop_words, classes, attributes, primary_keys)
            pks_data[model_name] = get_pk_data(primary_keys,attr_pk_mapping[model_name],num_of_records)

        end = timeit.default_timer()  
        with open("timing.txt","w+") as file:
            file.write(f"time for primary keys data {end-start} \n") 
        start = timeit.default_timer()
        
        with open("./fk.json","w+") as file:
            json.dump(models_fk , file)    

        with open("./mapped_to_faker.json","w+") as file:
            json.dump(attr_pk_mapping , file)

        #print(pks_data)
        for model_name,model in models.items():
            #print("//////////////////////////////////////")
            attr_data, attr_stmt = fill_model_statment(num_of_records, attr_pk_mapping[model_name], model["primaryKey"])
            #fk_data,fk_stmt = get_fk_data(model["ForgeinKey"],pks_data,num_of_records)
            row_values = list(pks_data[model_name].values())

            if len(attr_data): row_values.extend(attr_data)
            #if len(fk_data): row_values.extend(fk_data)
            row_values = list(zip(*row_values))

            insert_stmt = "INSERT INTO {0}.{1} (".format(database,model_name)
            for pk in model["primaryKey"]:
                insert_stmt +=  pk + ', '

            insert_stmt = insert_stmt[:-2]
            if attr_stmt: insert_stmt += ", " + attr_stmt
            #if fk_stmt: insert_stmt += ", " + fk_stmt
            insert_stmt += ") VALUES {0};".format(str(row_values)[1:-1])
            #print(insert_stmt)

            end = timeit.default_timer()
            with open("timing.txt","a+") as file:
                file.write(f"time for adding {model_name} attr and pk data {end-start} \n") 
            start = timeit.default_timer()
            # print(insert_stmt)
            stmts.append(insert_stmt.replace("),","),\n").replace("VALUES","\nVALUES\n") + "\n")
            try:    
                conn.execute(insert_stmt)
                #conn.execute("delete from {0}".format(model_name))
                print(f"inserted in model {model_name} successfully")
            except Exception as e:
                print(e)
                #continue

            end = timeit.default_timer()
            with open("timing.txt","a+") as file:
                file.write(f"time for inserting {model_name} attr and pk data to DB {end-start} \n") 
            start = timeit.default_timer()

        #foriegn keys
        for model_name,model in models.items():
            if  len(model["ForgeinKey"]) == 0: continue
            #print("???????????????????????????????????????????????????/")
            fk_data,fk_stmt = get_fk_data(model["ForgeinKey"],pks_data,num_of_records)
            #print(fk_stmt)
            row_values = list(pks_data[model_name].values())

            if len(fk_data): row_values.extend(fk_data)
            row_values = list(zip(*row_values))

            insert_stmt = "INSERT INTO {0}.{1} (".format(database,model_name)
            for pk in model["primaryKey"]:
                insert_stmt +=  pk + ', '

            insert_stmt = insert_stmt[:-2]
            if fk_stmt: insert_stmt += ", " + fk_stmt
            insert_stmt += ") \nVALUES \n {0} ".format(str(row_values)[1:-1].replace("),","),\n"))
            insert_stmt += "\nON DUPLICATE KEY UPDATE \n"

            fks_names = fk_stmt.split(', ')
            #print(fks_names)
            for fk_name in fks_names:
                insert_stmt +=  " {0} = VALUES({0}),\n" .format(fk_name)
            insert_stmt = insert_stmt[:-2] +';'

            end = timeit.default_timer()
            with open("timing.txt","a+") as file:
                file.write(f"time for adding {model_name} fk data {end-start} \n") 
            start = timeit.default_timer()
            
            
            stmts.append(insert_stmt + "\n")
            try:
                conn.execute(insert_stmt)
                print(f"inserted foriegn keys in model {model_name} successfully")
            except Exception as e:
                print(e)
            
            end = timeit.default_timer()
            with open("timing.txt","a+") as file:
                file.write(f"time for inserting attr and fk data to DB {end-start} \n") 

        
    stmts = '\n'.join(stmts)
    with open("seeds.sql","w+") as file:
        file.write(stmts)
    

__main__()
