 
import random 
import json 
import re 
import datetime 
import os 
import shutil 
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
from .faker_classes import faker_classes_mapper , pk_faker_classes 


def clean_word(colName , stopwords): 
    if len(colName) <= 1: 
        return colName 

    result = re.search("^[ 0-9]+$", colName) 
    if result is not None: 
        return colName 

    colName = re.sub("[0-9]+$", "", colName) 

    colName = colName.replace("_"," ") 

    colName = colName.replace("-"," ") 

    if colName.isupper() == True or len(colName.split()) > 1: 
        colName = colName.lower() 

    if re.search("^[a-z]+[A-Z]+", colName) is not None: 
        words = re.findall("[A-Z][^A-Z]*", colName) 
        if len(words) > 1 and len(words[0]) == 1 and len(words[1]) == 1: 
            result = "".join(words) 
        else: 
            result = " ".join(words) 
        colName = colName.split(re.findall("[A-Z][^A-Z]*", colName)[0])[0]+" " + result 
        colName = colName.lower() 

    if len(re.findall("[A-Z][^A-Z]*", colName)) >0: 
        words = re.findall("[A-Z][^A-Z]*", colName) 
        newWords = []  
        i = 0 
        while i<len(words): 
            if i+1<len(words) and len(words[i])==1 and len(words[i+1])==1: 
                newWords.append(words[i]+words[i+1]) 
                i+=1 
            else: 
                newWords.append(words[i]) 
            i+=1 
        colName = " ".join(newWords) 

    colName = " ".join(colName.split()) 
    colName = colName.lower() 

    colName = colName.split(" ") 

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
    pk_is_a_fk = False 
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
            pk_is_a_fk = True 

    return attributes, primary_keys, foriegn_keys, pk_is_a_fk 


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

        stmt += attr +", " 
        values.append([]) 
        for _ in range(num_of_records): 
            value = faker_classes_mapper[faker_class]() 

            if isinstance(value,str) or isinstance(value,datetime.datetime): 
                values[i].append(str(value)) 
            else: 
                values[i].append(value) 

        i+=1 

    stmt = stmt[:-2] if len(stmt) else stmt 

    return values,stmt 


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
def get_fk_data(model,pks_data,num_of_records,is_pk_and_fk): 
    stmt = "" 
    values = [] 
    for fk in model: 
        stmt += fk["attributeName"] + ", " 
        table = fk["ForignKeyTable"] 
        attr = fk["ForignKeyTableAttributeName"] 
        pk = pks_data[table][attr] 
        if is_pk_and_fk: 
            pk = random.sample(pk, k = num_of_records) 
            print(pk) 
        else: 
            pk = random.choices(pk , k = num_of_records) 
        values.append(pk) 
    return values,stmt[:-2] 


def get_insert_stmt(num_of_records,model_mapping,primary_keys,model_name,database,pks_data): 
    attr_data, attr_stmt = fill_model_statment(num_of_records, model_mapping, primary_keys) 
    #fk_data,fk_stmt = get_fk_data(model["ForgeinKey"],pks_data,num_of_records) 
    row_values = list(pks_data[model_name].values()) 

    if len(attr_data): row_values.extend(attr_data) 
    #if len(fk_data): row_values.extend(fk_data) 
    row_values = list(zip(*row_values)) 

    insert_stmt = "INSERT INTO {0}.{1} (".format(database,model_name) 
    for pk in primary_keys: 
        insert_stmt +=  pk + ", " 

    insert_stmt = insert_stmt[:-2] 
    if attr_stmt: insert_stmt += ", " + attr_stmt 
    insert_stmt += ") VALUES {0};".format(str(row_values)[1:-1]) 

    return insert_stmt 


def generate_seeds(database,models): 

    classes = { 
        "str":str, 
        "int":int, 
        "float":float, 
        "bool":bool, 
        "datetime":datetime.datetime 
    } 

    stop_words = stopwords.words("english") 
    attr_pk_mapping = {} 
    models_fk = {} 
    models_pk = {} 
    num_of_records = 100 


    pks_data = {} 
    weak_pk = [] 
    stmts = [] 

    for model_name , model in models.items(): 
        attributes, primary_keys, foriegn_keys, pk_is_a_fk = get_keys_attrs(model) 

        if pk_is_a_fk: 
            weak_pk.append(model_name) 
            print(attributes, primary_keys, foriegn_keys) 

        models_fk[model_name] = foriegn_keys 
        models_pk[model_name] = list(primary_keys.keys()) 
        attr_pk_mapping[model_name] = mapping_model_to_faker(stop_words, classes, attributes, primary_keys) 
        pks_data[model_name] = get_pk_data(primary_keys,attr_pk_mapping[model_name],num_of_records) 

    weak_entites = [] 
    for model_name,model in models.items(): 
        if model_name in weak_pk: 
            print(model_name) 
            continue 

        insert_stmt = get_insert_stmt(num_of_records, attr_pk_mapping[model_name],models_pk[model_name],model_name,database,pks_data) 
        stmts.append(insert_stmt.replace("),","),").replace("VALUES","VALUES")) 

    for model_name,model in models.items(): 
        if  len(model["ForgeinKey"]) == 0: continue 
        fk_data,fk_stmt = get_fk_data(model["ForgeinKey"],pks_data,num_of_records,(model_name in weak_pk)) 
        row_values = list(pks_data[model_name].values()) 

        if len(fk_data): row_values.extend(fk_data) 

        attr_stmt = "" 
        if model_name in weak_pk: 
            attr_data, attr_stmt = fill_model_statment(num_of_records, attr_pk_mapping[model_name], models_pk[model_name]) 
            if len(attr_stmt): 
                row_values.extend(attr_data) 

        row_values = list(zip(*row_values)) 
        insert_stmt = "INSERT INTO "+database+"."+model_name+" (".format(database,model_name) 
        for pk in models_pk[model_name]: 
            insert_stmt +=  pk + ", " 

        insert_stmt = insert_stmt[:-2] if len(models_pk[model_name]) else insert_stmt 
        if fk_stmt: insert_stmt += ", " + fk_stmt if len(models_pk[model_name]) else fk_stmt  
        if attr_stmt: insert_stmt += ", " + attr_stmt 

        insert_stmt += ") VALUES "+str(row_values)[1:-1].replace("),","),")+" " 
        if model_name in weak_pk: 
            insert_stmt += ";" 
        else: 
            insert_stmt += " ON DUPLICATE KEY UPDATE " 
            fks_names = fk_stmt.split(", ") 
            for name in fks_names: 
                insert_stmt +=  " "+name+" = VALUES("+name+"), " .format(name) 
            insert_stmt = insert_stmt[:-2] +";" 

        stmts.append(insert_stmt) 

    currentPath = os.getcwd()  
    seedspath = os.path.join(currentPath, "seeds") 
    if not os.path.exists(seedspath): 
        os.makedirs(seedspath) 
    else: 
        shutil.rmtree(seedspath, ignore_errors=True) 
        os.makedirs(seedspath) 

    count = 0 
    for stmt in stmts: 
        path = seedspath +"/"+ str(count)+".sql" 

        with open(path,"w+") as file:  
            file.write(stmt) 
        count += 1 
