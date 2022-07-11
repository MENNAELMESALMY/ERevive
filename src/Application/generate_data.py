#import spacy
import difflib
import random
import json
import re
import datetime
import itertools
from turtle import st
from numpy import positive
from sqlalchemy.sql import case
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sqlalchemy import create_engine
from textblob import Sentence
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
    #clean words
    #try excat match 
    #try NER
    #put defaults
    
    attr_pk = (attributes.copy())
    attr_pk.update(primary_keys)
    attr_pk_mapping= {}

    # cleaned = [' '.join(clean_word(k,stop_words)) for k in attr_pk.keys()]
    # sentence = ' '.join(cleaned)
    # doc = nlp(sentence)
    # print("//////////////////////////////////")
    # print(sentence)
    # for ent in doc.ents:
    #     print("-->",ent.text, ent.label_)


    for attr , datatype in attr_pk.items():
        attr_cleaned = clean_word(attr,stop_words)
        max_score,best_match = 0,None
        #print("//////////////////////////////")
        for faker_class in faker_classes_mapper.keys():
            faker_class_cleaned = clean_word(faker_class,stop_words)
            score = match(attr_cleaned,faker_class_cleaned)
            
            value = faker_classes_mapper[faker_class]()
            same_type = isinstance(value,classes[datatype])
        
            # #////////////////
            # a = ' '.join(attr_cleaned)
            # b = ' '.join(faker_class_cleaned)
            # seq = difflib.SequenceMatcher(None,a,b)
            # d = seq.ratio()*100
            # if d >= 50 and same_type:print(f"({a} , {b}) --> {d}")
            # #/////////////////

            if score > max_score and same_type:
                max_score = score
                best_match = faker_class
        
        if not best_match: #default
            best_match = datatype

        #print(f"best match is ({attr},{best_match}) --> {max_score}")

        attr_pk_mapping[attr] = best_match
 
    return attr_pk_mapping


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


def get_fk_data(model,pks_data,num_of_records):
    stmt = ""
    values = []
    for i,fk in enumerate(model):
        stmt += fk["attributeName"] + ', '
        table = fk["ForignKeyTable"]
        attr = fk["ForignKeyTableAttributeName"]
        pk = pks_data[table][attr]
        pk = random.choices(pk , k = num_of_records)
        values.append(pk)
    return values,stmt[:-2]

        


# def fill_model_statment(num_of_records, model_name, attr_pk_mapping, primary_keys, attributes):
#     pk = primary_keys.keys()
    
#     statment = f"INSERT INTO {model_name} ("
#     values = "("
#     for attr,faker_class in attr_pk_mapping.items():
#         statment += "{0}, ".format(attr)
    
#     for _ in range(num_of_records):
#         for attr,faker_class in attr_pk_mapping.items():
#             if attr in pk:
#                 value = pk_faker_classes[faker_class]()
#             else:
#                 value = faker_classes_mapper[faker_class]()

#             if isinstance(value,str) or isinstance(value,datetime.datetime):
#                 values += "'{0}', ".format(value)
#             else:
#                 values += "{0}, ".format(value)
#         values = values[:-2] + ') , ('
    
#     statment = statment[:-2] + ') VALUES '+values[:-4]+';'
#     return statment

    


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

    # l1 = [[1,2,5,4],[4,5,2,6],[4,2,5,6]]
    # l2 = [4,5,2,6]
    # print(list(zip(*l1)))
    
    #nlp = spacy.load("en_core_web_sm")
    stop_words = stopwords.words('english')
    attr_pk_mapping = {}
    models_fk = {}
    num_of_records = 5

    user="root"
    password="admin<3Super"
    database="department"
    connection_string = "mysql+mysqlconnector://{0}:{1}@127.0.0.1:3306/{2}".format(user, password, database) 
    engine = create_engine(connection_string)

    pks_data = {}
    with engine.begin() as conn:
        #insert attrs and primary keys
        for model_name , model in models.items():
            #print("//////////////////////////////////////")
            attributes, primary_keys, foriegn_keys = get_keys_attrs(model)
            models_fk[model_name] = foriegn_keys
            attr_pk_mapping[model_name] = mapping_model_to_faker(stop_words, classes, attributes, primary_keys)
            pks_data[model_name] = get_pk_data(primary_keys,attr_pk_mapping[model_name],num_of_records)
            
        #print(pks_data)
        for model_name,model in models.items():
            #print("//////////////////////////////////////")
            attr_data, attr_stmt = fill_model_statment(num_of_records, attr_pk_mapping[model_name], model["primaryKey"])
            #fk_data,fk_stmt = get_fk_data(model["ForgeinKey"],pks_data,num_of_records)
            row_values = list(pks_data[model_name].values())

            if len(attr_data): row_values.extend(attr_data)
            #if len(fk_data): row_values.extend(fk_data)
            row_values = list(zip(*row_values))

            insert_stmt = "INSERT INTO {0} (".format(model_name)
            for pk in model["primaryKey"]:
                insert_stmt +=  pk + ', '

            insert_stmt = insert_stmt[:-2]
            if attr_stmt: insert_stmt += ", " + attr_stmt
            #if fk_stmt: insert_stmt += ", " + fk_stmt
            insert_stmt += ") VALUES {0};".format(str(row_values)[1:-1])
            #print(insert_stmt)

            # print(insert_stmt)
            try:    
                conn.execute(insert_stmt)
                #conn.execute("delete from {0}".format(model_name))
                print(f"inserted in model {model_name} successfully")
            except Exception as e:
                print(e)
                #continue

        #foriegn keys
        for model_name,model in models.items():
            if  len(model["ForgeinKey"]) == 0: continue
            #print("???????????????????????????????????????????????????/")
            fk_data,fk_stmt = get_fk_data(model["ForgeinKey"],pks_data,num_of_records)
            #print(fk_stmt)
            row_values = list(pks_data[model_name].values())

            if len(fk_data): row_values.extend(fk_data)
            row_values = list(zip(*row_values))

            insert_stmt = "INSERT INTO {0} (".format(model_name)
            for pk in model["primaryKey"]:
                insert_stmt +=  pk + ', '

            insert_stmt = insert_stmt[:-2]
            if fk_stmt: insert_stmt += ", " + fk_stmt
            insert_stmt += ") VALUES {0} ".format(str(row_values)[1:-1])
            insert_stmt += "ON DUPLICATE KEY UPDATE "

            fks_names = fk_stmt.split(', ')
            #print(fks_names)
            for fk_name in fks_names:
                insert_stmt +=  "{0} = VALUES({0}), " .format(fk_name)
            insert_stmt = insert_stmt[:-2] +';'

            #print(insert_stmt)

            #pk_data.extend(fk_data)
            #values = list(zip(*pk_data))
            #print(row_values)
            #stmt = "INSERT into comments (cid, articles_has_aid, users_posts_userid) VALUES {0} ".format(str(values)[1:-1])
            #stmt += "ON DUPLICATE KEY UPDATE users_posts_userid = VALUES(users_posts_userid), articles_has_aid = VALUES(articles_has_aid);"

            try:
                conn.execute(insert_stmt)
                print(f"inserted foriegn keys in model {model_name} successfully")
            except Exception as e:
                print(e)
        '''
        
        from sqlalchemy.sql import case

        query(MyTable).filter(
            MyTable.col1.in_(payload)
        ).update({
            MyTable.col2: case(
                payload,
                value=MyTable.col1,
            )
        }, synchronize_session=False)
        col2=CASE mytable.col1
                WHEN 'x' THEN 'y'
                WHEN 'a' THEN 'b'
                WHEN 'c' THEN 'd'
        '''
    
        
        # #insert foriegn keys
        # for model_name , fks in models_fk.items():
        #     if len(fks) == 0:continue 
        #     print("/////////////////")
        #     print(model_name)
        #     insert_stmt = "INSERT INTO {0} (".format(model_name)
        #     values = []
        #     for fk_name , fk_object in fks.items(): 
        #         attr = fk_object["ForignKeyTableAttributeName"]
        #         table = fk_object["ForignKeyTable"]
                
        #         select_stmt = "SELECT {0} FROM {1};".format(attr,table)
        #         try:
        #             results = list(conn.execute(select_stmt).fetchall())
        #             insert_stmt += "{0}, ".format(fk_name)
        #         except Exception as e:
        #             print(e)

        #         results = list(itertools.chain(*results))
        #         #print("results",results)
        #         results = random.choices(results , k = num_of_records)
        #         values.append(results)

                
        #     #print("values",values)
        #     if len(values) > 1:
        #         values = tuple(zip(*values))
        #         #values = str(values)[1:-1]
        #     else:
        #         values = tuple(zip(values[0]))
        #         #values = str(values).replace(",)",")")[1:-1]


        #     pks = models[model_name]["primaryKey"]
        #     pk_stmt = ",".join(pks)
        #     select_stmt = "SELECT {0} FROM {1};".format(pk_stmt,model_name)
        #     results = tuple(conn.execute(select_stmt).fetchall())[:num_of_records]
        #     print("pk",results)
        #     results = tuple(zip(values,results))
        #     print("////////////////////")
        #     print(results)
        #     print("////////////////////")
        #     print("zipped",values)
        #     insert_stmt = insert_stmt[:-2] + ')'
        #     insert_stmt += " VALUES "+ values+";"
        #     print(insert_stmt)

        #     # try:    
        #     #     conn.execute(insert_stmt)
        #     #     print(f"inserted in model {model_name} successfully")
        #     # except Exception as e:
        #     #     print(e)
        #     #     continue

            


    with open("./fk.json","w+") as file:
        json.dump(models_fk , file)    

    with open("./mapped_to_faker.json","w+") as file:
        json.dump(attr_pk_mapping , file)
    
__main__()
