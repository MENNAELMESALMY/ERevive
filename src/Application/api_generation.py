from .api_templates import ApiFactory
from .generate_model import createAllModels
from .generate_data import generate_seeds
import json
import os
import stat

def Create_Directory(directory):
    path = os.path.join(os.getcwd(), directory) 
    os.umask(0)
    if os.path.exists(path):
        command = "find "+path + " -mindepth 1 ! -regex '^"+path+"/venv"+"\(/.*\)?' -delete"
        os.system(command)
    else:
        os.makedirs(path,mode=0o777)

def get_clusters():
    clusters = []
    with open('../SearchEngine/finalMergedQueries.json','rb') as file:
        testSchema = json.load(file)
        for cluster in testSchema.keys():
            c = []
            for q in testSchema[cluster]:
                query = q[0]
                query.update({"constructed_query":q[1]})
                c.append(query)
            clusters.append(c)
    return clusters
    
def Create_Application(schema,clusters,user="",password = "",db="",port=3000):
    Create_Directory('api')
    os.chdir('api')
    models,modelsObjects = createAllModels(schema) 
      

    api = ApiFactory(models,user,password,db,modelsObjects)
    apisFiles,crud_ui_out = api.create_models_apis()
    with open('../crud_ui_out.json','w') as f:
        json.dump(crud_ui_out,f)
    createApis(apisFiles)
    namespaces_imports,inits,clusters_out = create_api_namespaces(api,clusters,crud_ui_out)
    json_clusters = json.dumps(clusters_out)
    with open('../clusters.json','w') as f:
        f.write(json_clusters)
    create_api_init(api,namespaces_imports,inits)
    create_app(api)
    create_app_init(api)
    create_app_requirements(api)
    create_app_run(api)
    create_app_setup(api)
    create_app_env(api,port)
    create_app_utils(api)
    generate_seeds(db,modelsObjects)
    os.chdir('./..')


def create_api_namespaces(api,clusters,clusters_out):
    namespaces_imports = ""
    inits = ""
    
    for cluster in clusters.values():
        errors = []
        entities = cluster[0][0]["queryObj"]["entities"]
        api_name = '_'.join(entities)
        api_name = api_name.lower()
        if api_name not in clusters_out:
            clusters_out[api_name] = []
        api_file  = 'apis/'+api_name+'_api.py'
        namespace_name = api_name+"_namespace"
        route_path = '/'.join(entities)
        if(api_name not in api.api_files):
            init,namespace,namespace_import = api.create_api_structure(api_name,route_path,entities)
            namespaces_imports += namespace_import
            inits += init
            with open(api_file, 'w') as f:
                f.write(namespace)

        for query in cluster:
            cartesian = len(query[0]["queryObj"]["entities"]) > 1 and len(query[0]["queryObj"]["bestJoin"]) == 0
            hasGroupBy = len(query[0]["queryObj"]["groupByAttrs"]) != 0
            if cartesian and hasGroupBy:
                continue

            endpoint_object , resource_model = query
       
            if endpoint_object['endpoint_name'] not in errors:
                errors.append(endpoint_object['endpoint_name'])
            else:
                continue
 
            clusters_out[api_name].append(endpoint_object)
            parse_args , db_query = create_query_api_logic(endpoint_object,query[0]["queryObj"],api.modelsObjects)  

            create_resource(resource_model, endpoint_object,api_file,namespace_name,parse_args , db_query)

    return namespaces_imports , inits ,clusters_out


def get_entities_as_select_attr(entities,models_obj):
    
    select_attr = ", ".join(entities)
    select_attr += ", "
    return select_attr


def is_agg_in_orderby(aggr_attrs):
    for attr in aggr_attrs:
        if attr[1]:
            return True
    return False

def get_aggr_attrs(aggr_attrs):
    count_attrs = []
    final_aggr_attr = []
    remove_counts = False
    for attr in aggr_attrs:
        attr_aggregation = attr[1]
        if attr_aggregation != "count":
            final_aggr_attr.append(attr)
        else:
            count_attrs.append(attr)
            if "*" in attr[0][0]:
                final_aggr_attr.append(attr)
                remove_counts = True
    
    if not remove_counts:
        final_aggr_attr.extend(count_attrs)
    
    return final_aggr_attr


def order_joins(query_joins,db_query):
    joins = query_joins.copy()
    best_Joins = []
    best_entities = []
    first_join = True
    not_found = []
    not_found_entities = []

    join = joins.pop(0)
    entity1 = join.split('.')[0][1:]
    entity2 = join.split('=')[1].split('.')[0][1:]
    search_entity = entity2
    first_search = True
    should_print = False
    while len(joins):
        found = False
        
        for i in range(len(joins)):
            j = joins[i]
            j_entity1 = j.split('.')[0][1:]
            j_entity2 = j.split('=')[1].split('.')[0][1:]
            if search_entity == j_entity1 or search_entity == j_entity2:
                if first_join:
                    best_Joins.append(join.replace('=','=='))
                    first_join = False
                found = True
                first_search = True
                best_Joins.append(joins.pop(i).replace('=','=='))
                entity1 , entity2 = j_entity1 , j_entity2
                search_entity = entity1 if entity1 != search_entity else entity2
                break
        
        if not found and not first_search:
            should_print = True
            first_search = False
            j = joins.pop(0)
            entity1 = j.split('.')[0][1:] 
            entity2 = j.split('=')[1].split('.')[0][1:]
            not_found.append(j.replace('=','=='))
            not_found_entities.append(entity1)
            search_entity = entity2

        if not found and first_search:
            first_search = False
            search_entity = entity1 if entity1 != search_entity else entity2

        if found:
            first_search = True
        
        
    entity1 = best_Joins[-1].split('.')[0][1:]
    entity2 = best_Joins[-1].split('==')[1].split('.')[0][1:]
    substrings1 = "({0},|({0})| {0},| {0})|({0}.| {0}.".format(entity1).split("|")
    substrings2 = "({0},|({0})| {0},| {0})|({0}.| {0}.".format(entity2).split("|")
    
    if any(map(db_query.__contains__, substrings1)) or any(map(db_query.__contains__, substrings2)):
        best_Joins.reverse()
   
    best_entities = []
    entity1 = best_Joins[0].split('.')[0][1:]
    entity2 = best_Joins[0].split('==')[1].split('.')[0][1:]
    substrings1 = "({0},|({0})| {0},| {0})|({0}.| {0}.".format(entity1).split("|")

    if any(map(db_query.__contains__, substrings1)):
        prev_entity = entity2
        best_entities.append(entity2)
    else:
        prev_entity = entity1
        best_entities.append(entity1)

    for i in range(1,len(best_Joins)):
        join = best_Joins[i]
        entity1 = join.split('.')[0][1:]
        entity2 = join.split('==')[1].split('.')[0][1:]
        if prev_entity == entity1:
            best_entities.append(entity2)
        else:
            best_entities.append(entity1)
        prev_entity = best_entities[-1]

 
    best_Joins.extend(not_found)
    best_entities.extend(not_found_entities)

    return best_entities , best_Joins , should_print

    

def create_query_api_logic(endpoint_object,query,models_obj):

    params = endpoint_object["queryParams"]
    parser = endpoint_object["endpoint_name"].lower()
    parse_args=""
    if len(params):
        parse_args = "args = {0}_parser.parse_args()\n".format(parser)

    db_query = "results = db.session.query("
    select_attr = ""
    for attr in query["selectAttrs"]:
        if attr[0] == '*': 
            select_attr += get_entities_as_select_attr(query["entities"],models_obj)
            break
        elif "*" in attr[0]:
            entity_name = attr[0].split('.')[0]
            attr_name = models_obj[entity_name]["primaryKey"][0]
            select_attr += "{0}.{1}.label('{0}.{1}'), ".format(entity_name , attr_name)           
        else:
            entity = attr[0].split('.')[0]
            select_attr += "{0}.label('{0}'), ".format(attr[0])    

    aggr_attrs = get_aggr_attrs(query["aggrAttrs"])
    if len(query["aggrAttrs"]):
        pass
  
    for attr in aggr_attrs:      
        attr_aggregation = attr[1]
        attr_name = attr[0][0] if "*" not in attr[0][0] else ""
        label = 'all' if attr[0][0] == "*" else attr[0][0]
        select_attr += "func.{0}({1}).label('{2}')".format(attr_aggregation,attr_name,attr_aggregation+'_'+label) + ", "
    
    if len(query["entities"]) > 1 and len(query["bestJoin"]) == 0:
        for entity in query["entities"]:
            if entity not in select_attr:
                select_attr += entity + ", "

    if select_attr == "" :
        select_attr += get_entities_as_select_attr(query["entities"],models_obj)
        select_attr = select_attr[:-2]
    else:
        select_attr = select_attr[:-2]

    db_query += select_attr + ')'

    should_print = False
    hereJoins = False
    joins = ""
    if len(query["entities"]) > 1:
 
        if len(query["bestJoin"]) == 0:
            pass
        elif len(query["bestJoin"]) == 1:
            for join in query["bestJoin"]:
                
                join = join.replace('=','==')
                entity = join.split('.')[0]
                entity1 = entity[1:] 
                entity2 = join.split('==')[1].split('.')[0][1:]
                entity = entity1
                substrings1 = "({0},|({0})| {0},| {0})|({0}.| {0}.".format(entity1).split("|")
                substrings2 = "({0},|({0})| {0},| {0})|({0}.| {0}.".format(entity2).split("|")
                if any(map(db_query.__contains__, substrings1)):
                    entity = entity2
                else:
                    entity = entity1
                    if not any(map(db_query.__contains__, substrings2)):
                        id = join.split("==")[1][1:]
                        db_query = db_query[:-1]
                        db_query += ", " if db_query[-1] != "(" else ""
                        db_query += "{0}.label('{0}'))".format(id)
                        query["selectAttrs"].append([id , "str"])
                joins += "\\\n\t\t\t\t.join({0},{1})".format(entity,join)
        else:
            hereJoins = True
            entities,best_joins,should_print = order_joins(query["bestJoin"],db_query)
            for i in range(len(best_joins)):
                joins += "\\\n\t\t\t\t.join({0},{1})".format(entities[i],best_joins[i])


    db_query += joins if len(joins) else ""


    is_oring = False
    whereAttr = set()

    filters = "\\\n\t\t\t\t.filter(" if len(query["whereAttrs"]) else ""
    for attr in query["whereAttrs"]:
        attr_name = attr[0][0]
        attr_opperator = attr[1]
        attr_opperator = attr_opperator.strip()
        and_or = attr[3] if len(attr) >= 3 else ""
        attr_opperator = "==" if attr_opperator == "=" else attr_opperator
        attr_opperator = "in_" if attr_opperator == "in" else attr_opperator
        attr_opperator = "notlike" if attr_opperator == "not like" else attr_opperator
        

        if attr_name in whereAttr:
            continue
        whereAttr.add(attr_name)

        if attr[2] == "value":
            value = "args['{0}']".format(attr_name)

        else:
            value = attr[2]

        if is_oring: 
            filters = filters[:-2] + " | "
        if and_or == "or" or is_oring:
            filters += "("
        

        if attr_opperator in ["like","in_","notlike"]:
            filters += "{0}.{1}({2}), ".format(attr_name,attr_opperator,value)

        elif attr_opperator == "between":
            filters += "{0}.{1}({2}[0],{2}[1]), ".format(attr_name,attr_opperator,value)

        else:
            filters += "{0} {1} {2}, ".format(attr_name,attr_opperator,value)

        if and_or == "or" or is_oring:
            filters = filters[:-2] + "), "
            if not and_or: is_oring = False
            else:is_oring = True  
        else:
            is_oring = False

    if len(filters):
        filters = filters[:-2] +")"
        db_query += filters
    
    agg_in_orderby = is_agg_in_orderby(query["orderByAttrs"])
    groupByAttrs = set([attr[0] for attr in query["groupByAttrs"]])
    is_group_all = False
    if len(query["aggrAttrs"]) or agg_in_orderby or groupByAttrs:
        selectAttrs = set()
        for attr in query["selectAttrs"]:
            if attr[0] == '*':
                is_group_all = True
                for entity in query["entities"]:
                    attrs = models_obj[entity]["attributes"].keys()
                    attrs = [entity+'.'+attr for attr in attrs]
                    selectAttrs.update(attrs)
            else:
                selectAttrs.add(attr[0])
        groupByAttrs.update(selectAttrs)
    is_group_by = False
    groupby_attr = "\\\n\t\t\t\t.group_by(" if len(groupByAttrs) else ""
    for attr in groupByAttrs:
        groupby_attr += "{0}, ".format(attr)
    if len(groupby_attr):
        is_group_by = True
        groupby_attr = groupby_attr[:-2] + ")"
        db_query += groupby_attr

    having = "\\\n\t\t\t\t.having(" if len(query["havingAttrs"]) else ""
    for attr in query["havingAttrs"]:
        attr_name = attr[1][0] if "*" not in attr[1][0] else ""
        attr_aggregation = attr[0]

        attr_opperator = attr[2]
        attr_opperator = "==" if attr_opperator == "=" else attr_opperator
        attr_opperator = "in_" if attr_opperator == "in" else attr_opperator
        attr_opperator = "notlike" if attr_opperator == "not like" else attr_opperator

        arg_name = "having_value" if attr_name == "" else attr_name
        value = "args['{0}']".format(arg_name)

        if attr_aggregation:
            having += "func.{0}({1})".format(attr_aggregation,attr_name)
        else:
            having += "{0}".format(attr_name)

        if attr_opperator in ["like","in_","notlike"]:  
            having += ".{0}({1}), ".format(attr_opperator,value)

        elif attr_opperator == "between":
            having += ".{0}({1}[0],{1}[1]), ".format(attr_opperator,value)

        else:
            having += " {0} {1}, ".format(attr_opperator,value)

    if len(having):
        having = having[:-2] +")"
        db_query += having


    contains_aggr = any(map(db_query.__contains__, "(func.| func.".split("|")))
    will_print = False
    orderby_attr = "\\\n\t\t\t\t.order_by(" if len(query["orderByAttrs"]) else ""
    for attr in query["orderByAttrs"]:
        original_attr = attr
        if attr[0][0] == "*" and not attr[1] : continue
        attr_name = attr[0][0] if "*" not in attr[0][0] else ""
        attr_aggregation = attr[1]
        if (attr_aggregation and not (is_group_by or contains_aggr)):
            will_print = True
       
        aggr = "_"+attr_aggregation +"_" if (attr_aggregation and (is_group_by or contains_aggr)) else ""
        if "*" in attr[0][0]:
            aggr = "_"+attr_aggregation +"_"
            param_name = "is_order_of"+aggr+"of_rows_desc"
        else:
            aggr = "_" if not aggr else aggr
      
            param_name = "is_order_of"+aggr+attr_name.split('.')[1]+"_desc"

        variable_name = attr_name.split('.')[1] + "_" if attr_name else ""
        parse_args += "\
        {0}direction = desc if args['{1}'] else asc\n".format(variable_name,param_name)
        

        if attr_aggregation and (is_group_by or contains_aggr):
            orderby_attr += "{0}direction(func.{2}({1})), ".format(variable_name,attr_name,attr_aggregation)
        else:
            orderby_attr += "{0}direction({1}), ".format(variable_name,attr_name)

    if len(orderby_attr):
        orderby_attr = orderby_attr[:-2] + ")"
        db_query += orderby_attr


    db_query = db_query+".all()"

    return parse_args , db_query


def create_resource(resource_model, endpoint_object,api_file,namespace_name,parse_args , db_query):
 
    params = endpoint_object["queryParams"]
    parser = ""
    except_parser =  "\n" 
    if len(params):
        except_parser =  "@{1}.expect({0}_parser)\n".format(endpoint_object["endpoint_name"].lower(),namespace_name)
        parser = endpoint_object["endpoint_name"].lower()+"_parser = reqparse.RequestParser()\n"
        for param in params:
       
            attr_type = "str" if param[1] == "datetime" else param[1]
            if param[2] in ["in","between"]:
                parser += endpoint_object["endpoint_name"].lower()+"_parser.add_argument('"+param[0]+"', type="+attr_type+", required=True,action='append', location='args')\n"
            else:
                parser += endpoint_object["endpoint_name"].lower()+"_parser.add_argument('"+param[0]+"', type="+attr_type+", required=True, location='args')\n"
    resource = "\
{4}\n\
@{1}.route('/{3}', methods=['GET'])\n\
class {0}_resource(Resource):\n\
    \n\
    {5}\
    def get(self):\n\
        {6}\n\
        results = None\n\
        try:\n\
            {7}\n\n\
            results = serialize(results)\n\
            return results , 200\n\
        except Exception as e:\n\
            print(e)\n\
            return str(e) , 400\n\n".format(endpoint_object["endpoint_name"],namespace_name,resource_model,endpoint_object["endpoint_name"],parser,except_parser,parse_args , db_query)

    with open(api_file, 'a') as f:
        f.write(resource)
    
def get_attr_name_type(attrs,attr_type=None):
    attr_names = []

    for attr in attrs:
        if type(attr[0])!=str:
            attr_name = attr[0][0] 
            if attr_type and attr[1] and attr[1] !="":
                attr_name = attr_name.split('.')[0]+'.'+attr[1]+'_'+attr_name.split('.')[-1]
        else:
            attr_name = attr[0]
            if attr[1] and attr[1] !="":
                attr_name = attr[1]+"_"+attr_name
        if attr_name.find('*')!=-1:   
            attr_name = attr_name.replace('*','all')

        if type(attr[0])!=str and len(attr) > 2 and attr[2] != "value":
            attr_names.append(attr[2])    
        attr_names.append(attr_name)
    return attr_names

def query_renaming(entities,whereAttrs,groupAttrs,orderAttrs,isUpdate=False,is_group_all=False):
    where_attr = get_attr_name_type(whereAttrs)
    if not isUpdate:
        group_attr = get_attr_name_type(groupAttrs)
    else:
        group_attr = groupAttrs
    if is_group_all:
        group_attr = ["all"]
    order_attr = get_attr_name_type(orderAttrs,"order")
    where_attr = set([attr[attr.find(".")+1:] for attr in where_attr if attr != "*"])
    order_attr = set([attr[attr.find(".")+1:] for attr in order_attr if attr != "*"])
    group_attr = set([attr[attr.find(".")+1:] for attr in group_attr if attr != "*"])
    endpoint_name = "get"+"_"+"_".join(entities)
    ui_name = "get "+" ".join(entities)
    
    if len(where_attr) != 0:
        endpoint_name += "_filteredby"+"_"+"_".join(where_attr)
        ui_name += " filtered by "+" , ".join(where_attr)
    if len(group_attr) != 0:
        endpoint_name +="_groupedby"+ "_"+"_".join(group_attr)
        ui_name += " grouped by "+" , ".join(group_attr)
    if len(order_attr) != 0:
        #print(orderAttrs)
        endpoint_name +="_orderedby"+ "_"+"_".join(order_attr)
        ui_name += " ordered by "+" , ".join(order_attr)
    
    return endpoint_name,ui_name


def create_app_utils(api):
    app_utils = api.create_app_utils()
    with open('utils.py', 'w') as f:
        f.write(app_utils)
def create_app_env(api,port):
    app_env = api.create_app_env(port)
    with open('.env','w') as f:
        f.write(app_env)

def create_app_setup(api):
    app_setup = api.create_app_setup()
    with open('setup.sh','w') as f:
        f.write(app_setup)
    st = os.stat('setup.sh')
    os.chmod('setup.sh', st.st_mode | stat.S_IEXEC)

def create_app_run(api):
    app_run = api.create_app_run()
    with open('run.sh','w') as f:
        f.write(app_run)
    st = os.stat('run.sh')
    os.chmod('run.sh', st.st_mode | stat.S_IEXEC)

def create_app_requirements(api):
    app_reqs = api.create_app_requirements()
    with open('requirements.txt','w') as f:
        f.write(app_reqs)

def create_app_init(api):
    app_init = api.create_app_init()
    with open('__init__.py', 'w') as f:
        f.write(app_init)
    
def create_app(api):
    app = api.create_app()
    with open('app.py', 'w') as f:
        f.write(app)

def createApis(apisFiles):
    Create_Directory('apis')
    for api in apisFiles:
        with open('apis/'+api.lower()+'_api.py', 'w') as f:
            f.write(apisFiles[api])

def create_api_init(api,cluster_imports,clusters_init):
    api_init,api_imports = api.create_api_init()    
    with open('apis/__init__.py', 'w') as f:
        f.write(api_imports)
        f.write(cluster_imports)
        f.write(api_init)
        f.write(clusters_init)
        f.write("\n\
    return rest_plus_api")
