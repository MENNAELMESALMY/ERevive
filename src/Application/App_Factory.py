from sklearn import cluster
from Api_Factory import ApiFactory
import json
import os
import stat
from generateModel import createAllModels
def Create_Directory(directory):
    path = os.path.join(os.getcwd(), directory) 
    os.umask(0)
    try:
        os.mkdir(path)
    except Exception as e:
        pass
Create_Directory('api')
os.chdir('api')
  
# TODO
# for select * ()
# crud
# db logic
# create parser for query paramters


# Create Models method
def Create_Application(schema,clusters,user="nada",password = "Ringmybells5",db="default"):
    models,modelsObjects = createAllModels(schema)  #should be replaced with nihal's models 
      
    api = ApiFactory(models,user,password,db,modelsObjects)
    apisFiles,crud_ui_out = api.create_models_apis()
    createApis(apisFiles)
    namespaces_imports,inits,clusters_out = create_api_namespaces(api,clusters)
    clusters_out.update(crud_ui_out)
    #dump clusters_out to file
    json_clusters = json.dumps(clusters_out)
    with open('clusters.json','w') as f:
        f.write(json_clusters)

    create_api_init(api,namespaces_imports,inits)
    create_app(api)
    create_app_init(api)
    create_app_requirements(api)
    create_app_run(api)
    create_app_setup(api)
    create_app_env(api)
    create_app_utils(api) 


def create_api_namespaces(api,clusters):
    namespaces_imports = ""
    inits = ""
    clusters_out= {}
    errors = []
    for cluster in clusters:
        
        #endoint = create_endpoint(clusters[0])
        entities = cluster[0]["entities"]
        api_name = '_'.join(entities)
        clusters_out[api_name] = []
        api_file  = 'apis/'+api_name+'_api.py'
        namespace_name = api_name+"_namespace"
        route_path = '/'.join(entities)
        if(api_name not in api.api_files):
            init,namespace,namespace_import = api.create_api_structure(api_name,route_path,entities) #check if entites names same as the models names 
            namespaces_imports += namespace_import
            inits += init
            with open(api_file, 'w') as f:
                f.write(namespace)
        # for get queries
        # handle * by adding a function that takes arrayo models and returns updated model of them all
        # create parser for each query
        for query in cluster:
            #print(query['entities'])
            resource_model , endpoint_object , _ = create_query_ui_endpoint(query,api.modelsObjects)  # return to frontend
            clusters_out[api_name].append(endpoint_object)
            parse_args , db_query = create_query_api_logic(endpoint_object,query,api.modelsObjects)  
            #create api logic
            if endpoint_object["endpoint_name"] == "get_players_awards_players_groupedby_playerID_orderedby_all":
                print("WEWEWE\n")
                query.pop("origQuery")
                print(query)
            if endpoint_object['endpoint_name'] not in errors:
                errors.append(endpoint_object['endpoint_name'])
            else:
                print("ENDPOINT ALREADY EXISTS\n",query,endpoint_object['endpoint_name'])   
            #if "awards_coaches" in query["entities"] and "coaches" in query["entities"]:
            #if "awards_players" in query["entities"] and "player_allstar" in query["entities"]:
                #print("\nquery entites: ",query["entities"],"\n")
                #print("\nfile name: ",api_file,"\n")
                #print("\ncluster entites: ",cluster[0]["entities"],"\n")
                #print("\ncluster" , cluster[0])
                #print("\nquery" , query)

            create_resource(resource_model, endpoint_object,api_file,namespace_name,parse_args , db_query)
            
        #handle crud response
        # add is_entity --> true
    return namespaces_imports , inits ,clusters_out


def get_entities_as_select_attr(entities,models_obj):
    select_attr = ""
    if len(entities) > 1:
        select_attr = ", ".join(entities)
        select_attr += ", "
    else:
        entity_name = entities[0]
        attr = next(iter(models_obj[entity_name]["attributes"])) # O(1)
        #print("//////////////////////////////////////////////")
        #print(entity_name)
        #print(attr)
        #if primaryKey == "name":print(models_obj[entity_name])
        select_attr += "{0}, {0}.{1}.label('{0}.{1}'), ".format(entity_name , attr)
        #print(select_attr)
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


def create_query_api_logic(endpoint_object,query,models_obj):
    #if "awards_coaches" in query["entities"] and "coaches" in query["entities"]:
    #if len(query["entities"])==1 and "coaches" in query["entities"]:
    #print("//////////////////////////////////////////////")
    #print(models_obj)
    #print("query" , query)
    #print("whereAttrs" , query["whereAttrs"])
    #print("groupByAttrs",query["groupByAttrs"])
    #print("orderbyAttrs" , query["orderByAttrs"])
    #print("having" , query["havingAttrs"])
    #print("aggrAttrs", query["aggrAttrs"])
    #print("selectAttrs",query["selectAttrs"])
    #print("joins", query["bestJoin"])
    #print("entities", query["entities"])

    #print()
    #print("response" , endpoint_object['response'])
    #print()
    #print("queryParams" , endpoint_object['queryParams'])
    #print()
    #print("query" , query)
    #print()
    #print("modelsObjects" , modelsObjects)
    

    params = endpoint_object["queryParams"]
    parser = endpoint_object["endpoint_name"]
    parse_args=""
    if len(params):
        parse_args = "args = {0}_parser.parse_args()\n".format(parser)

    #get select attrs
    db_query = "results = db.session.query("
    select_attr = ""
    for attr in query["selectAttrs"]:
        if attr[0] == '*': # get all entities attributes
            select_attr += get_entities_as_select_attr(query["entities"],models_obj)
            break
        elif "*" in attr[0]:
            entity_name = attr[0].split('.')[0]
            attr_name = models_obj[entity_name]["primaryKey"][0]
            select_attr += "{0}.{1}.label('{0}.{1}')".format(entity_name , attr_name)           
        else:
            entity = attr[0].split('.')[0]
            if entity and entity not in select_attr:
                select_attr += entity +", "
                #print("/////////////////////////////////////")
                #print(select_attr)
                
            select_attr += attr[0] + ", "

    aggr_attrs = get_aggr_attrs(query["aggrAttrs"])
    if len(query["aggrAttrs"]):
        pass
        #print("////////////////////////////////////////////////")
        #print(query["aggrAttrs"])
        #print(aggr_attrs)
    for attr in aggr_attrs:      
        attr_aggregation = attr[1]
        attr_name = attr[0][0] if "*" not in attr[0][0] else ""
        label = 'all' if attr[0][0] == "*" else attr[0][0]
        select_attr += "func.{0}({1}).label('{2}')".format(attr_aggregation,attr_name,attr_aggregation+'_'+label) + ", "
    
    #cross product put entities in select
    if len(query["entities"]) > 1 and len(query["bestJoin"]) == 0:
        for entity in query["entities"]:
            if entity not in select_attr:
                select_attr += entity + ", "

    if select_attr == "" :
        #select_attr = ", ".join(query["entities"])
        select_attr += get_entities_as_select_attr(query["entities"],models_obj)
        select_attr = select_attr[:-2]
    else:
        select_attr = select_attr[:-2]

    db_query += select_attr + ')'


    #join
    hereJoins = False
    joins = ""
    if len(query["entities"]) > 1:
        #cross product 
        #no entities in join for cross product
        if len(query["bestJoin"]) == 0:
            hereJoins = True
            pass
            # for entity in query["entities"]:
            #     joins += "\\\n\t\t\t\t.join({0})".format(entity)
        #joins
        else:
            hereJoins = True
            for join in query["bestJoin"]:
                join = join.replace('=','==')
                entity = join.split('.')[0]
                entity1 = entity[1:] # remove space
                entity2 = join.split('==')[1].split('.')[0][1:]
                #print(entity1,entity2)
                entity = entity1
                if len(query["bestJoin"]) == 1:
                    substrings = "({0},|({0})| {0},| {0})".format(entity1)
                    substrings = substrings.split("|")
                    print("select",db_query)
                    print(substrings)
                    print(entity1) 
                    print(entity2)
                    print(list(map(db_query.__contains__, substrings)))
                    if any(map(db_query.__contains__, substrings)):
                        entity = entity2
                    else:
                        entity = entity1
                    #entity = entity1 if entity1 not in select_attr else entity2
                joins += "\\\n\t\t\t\t.join({0},{1})".format(entity,join)
       
    db_query += joins if len(joins) else ""


    # filters
    # Note aggregation in where is not valid
    # anding and oring not handled currently
    whereAttr = set()
    filters = "\\\n\t\t\t\t.filter(" if len(query["whereAttrs"]) else ""
    for attr in query["whereAttrs"]:
        attr_name = attr[0][0]
        attr_opperator = attr[1]
        attr_opperator = attr_opperator.strip()
        #print(attr_name,attr_opperator)
        attr_opperator = "==" if attr_opperator == "=" else attr_opperator
        attr_opperator = "in_" if attr_opperator == "in" else attr_opperator
        attr_opperator = "notlike" if attr_opperator == "not like" else attr_opperator
        #print(attr_name,attr_opperator)
        #removing duplicates for anding and oring
        ##########################
        if attr_name in whereAttr:
            continue
        whereAttr.add(attr_name)
        ##########################

        #value filter --> get values from parser
        if attr[2] == "value":
            value = "args['{0}']".format(attr_name)

        #column filter
        else:
            value = attr[2]

        if attr_opperator in ["like","in_","notlike"]:
            filters += "{0}.{1}({2}), ".format(attr_name,attr_opperator,value)

        elif attr_opperator == "between":
            filters += "{0}.{1}({2}[0],{2}[1]), ".format(attr_name,attr_opperator,value)

        else:
            filters += "{0} {1} {2}, ".format(attr_name,attr_opperator,value)

    if len(filters):
        filters = filters[:-2] +")"
        db_query += filters
    
    
    # group by
    # Note -> assumed if there is aggr then all attrs in select are in group by
    agg_in_orderby = is_agg_in_orderby(query["orderByAttrs"])
    groupByAttrs = set([attr[0] for attr in query["groupByAttrs"]])
    is_group_all = False
    if len(query["aggrAttrs"]) or agg_in_orderby:
        selectAttrs = set()
        for attr in query["selectAttrs"]:
            if attr[0] == '*':
                is_group_all = True
                for entity in query["entities"]:
                    attrs = models_obj[entity]["attributes"].keys()
                    attrs = [entity+'.'+attr for attr in attrs]
                    selectAttrs.update(attrs)
                    #print("attrs: ",attrs)
                    #print()
            else:
                selectAttrs.add(attr[0])
            #selectAttrs = [attr[0] for attr in query["selectAttrs"] if "*" not in attr[0]]
        #print("final Attrs: ",selectAttrs)
        groupByAttrs.update(selectAttrs)
    groupby_attr = "\\\n\t\t\t\t.group_by(" if len(groupByAttrs) else ""
    for attr in groupByAttrs:
        groupby_attr += "{0}, ".format(attr)
    if len(groupby_attr):
        groupby_attr = groupby_attr[:-2] + ")"
        db_query += groupby_attr


    # having 
    # Note --> having(count(*)) > having_vale
    # having_value is the count of rows
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


    # order_by
    orderby_attr = "\\\n\t\t\t\t.order_by(" if len(query["orderByAttrs"]) else ""
    for attr in query["orderByAttrs"]: # [["teams.tmID", "str"], ""]
        if attr[0][0] == "*" and not attr[1] : continue
        attr_name = attr[0][0] if "*" not in attr[0][0] else ""
        attr_aggregation = attr[1]

        aggr = "_"+attr_aggregation +"_" if attr_aggregation else ""
        if attr[0][0] == "*":
            param_name = "is_order_of"+aggr+"of_rows_desc"
        else:
            aggr = "_" if not aggr else aggr
            param_name = "is_order_of"+aggr+attr_name.split('.')[1]+"_desc"

        variable_name = attr_name.split('.')[1] + "_" if attr_name else ""
        parse_args += "\
        {0}direction = desc if args['{1}'] else asc\n".format(variable_name,param_name)
        

        if attr_aggregation:
            orderby_attr += "{0}direction(func.{2}({1})), ".format(variable_name,attr_name,attr_aggregation)
        else:
            orderby_attr += "{0}direction({1}), ".format(variable_name,attr_name)

    if len(orderby_attr):
        orderby_attr = orderby_attr[:-2] + ")"
        db_query += orderby_attr

    #print(db_logic)
    #if "awards_coaches" in query["entities"] and "coaches" in query["entities"]:
    #if len(query["entities"])==1 and "coaches" in query["entities"]:
    #print(db_query)
    db_query = db_query+".all()"
    if hereJoins and len(query["bestJoin"]) == 1:
        print("//////////////////////////////")
        print("selectAttrs",query["selectAttrs"])
        print("aggrAttrs", query["aggrAttrs"])
        print("groupByAttrs",query["groupByAttrs"])
        print("entities",query["entities"])
        print(db_query,"\n")
    print("groupByAttrsgroupByAttrs",groupByAttrs)
    endpoint_name,ui_name = query_renaming(query["entities"],query["whereAttrs"],groupByAttrs,query["orderByAttrs"],True,is_group_all)
    endpoint_url = '/'.join(query["entities"])+'/'+endpoint_name
    parse_args = parse_args.replace(parser,endpoint_name)
    endpoint_object.update({
        "endpoint_name":endpoint_name,
        "ui_name":ui_name,
        "url":endpoint_url,
        }) 
    
    return parse_args , db_query


def create_resource(resource_model, endpoint_object,api_file,namespace_name,parse_args , db_query):
    #stringfy the restplus resource_model
    #append to api file
    params = endpoint_object["queryParams"]
    parser = ""
    except_parser =  "\n" 
    if len(params):
        except_parser =  "@{1}.expect({0}_parser)\n".format(endpoint_object["endpoint_name"],namespace_name)
        parser = endpoint_object["endpoint_name"]+"_parser = reqparse.RequestParser()\n"
        for param in params:
            if param[2] in ["in","between"]:
                parser += endpoint_object["endpoint_name"]+"_parser.add_argument('"+param[0]+"', type="+param[1]+", required=True,action='append', location='args')\n"
            else:
                parser += endpoint_object["endpoint_name"]+"_parser.add_argument('"+param[0]+"', type="+param[1]+", required=True, location='args')\n"
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
    

    

def create_query_ui_endpoint(query,modelsObjects):
 
    endpoint_name,ui_name = query_renaming(query["entities"],query["whereAttrs"],query["groupByAttrs"],query["orderByAttrs"])
    endpoint_url = '/'.join(query["entities"])+'/'+endpoint_name
    endpoint_method = "get"
    #attr name - attr type - attr aggregation - attr relation mapping (foreign key)
    #TODO if column == column in conditions (where / having)
    queryParams = []
    for attr in query["whereAttrs"]:
        if attr[2] != "value":
            continue
        attr_name = attr[0][0]
        attr_type = attr[0][1]
        attr_operator = attr[1]
        queryParams.append((attr_name,attr_type,attr_operator,None))

    for attr in query["havingAttrs"]:
        # if "*" in attr[1][0]:
        #     continue
        attr_name = attr[1][0] if "*" not in attr[1][0] else "having_value"
        attr_type = attr[1][1] if "*" not in attr[1][0] else "int"
        attr_operator = attr[2]
        attr_aggregation = attr[0]
        queryParams.append((attr_name,attr_type,attr_operator,attr_aggregation))

    for attr in query["orderByAttrs"]:
        if attr[0][0] == "*" and attr[1] is None:
            continue
        
        attr_name = attr[0][0]
        attr_type = attr[0][1]
        attr_aggregation = attr[1]
        param_name = ""
        aggr = "_"+attr_aggregation +"_" if attr_aggregation else ""
        if attr_name == "*":
            param_name = "is_order_of"+aggr+"of_rows_desc"
        else:
            attr_name = attr_name.split('.')[1]
            aggr = "_" if not aggr else aggr
            param_name = "is_order_of"+aggr+attr_name+"_desc"
        queryParams.append((param_name,"bool",None,attr_aggregation))

    #print(query["selectAttrs"])
    aggrAttrs = get_aggr_attrs(query["aggrAttrs"])
    response_model , ui_response_model , db_selects = create_response_model(query["selectAttrs"],aggrAttrs,query["entities"],modelsObjects)
    response_model = "{ "+response_model+" }"
    endpoint = {
        "method": endpoint_method,
        "url": endpoint_url,
        "queryParams": queryParams,
        "bodyParams": [],
        "response": ui_response_model,
        "ui_name": ui_name,
        "cluster_name": "_".join(query["entities"]),
        "endpoint_name":endpoint_name,
        "is_single_entity":len(query["entities"])==1
    }

    #print("////////////////////////////////////////////")
    #print(endpoint)
    #print("////////////////////////////////////////////")

    return response_model , endpoint , db_selects


def create_response_model(selectAttrs,aggrAttrs,entities,modelsObject):
    pythondtypes_restmapping = {
    "str":"fields.String",
    "int":"fields.Integer",
    "float":"fields.Float",
    "bool":"fields.Boolean",
    "datetime":"fields.DateTime"
    }
    response_model = ""
    ui_response_model = {}
    db_selects= []
    #select *
    #enttity.*
    #print("aggrAttrs",aggrAttrs)
    #print(entities)
    #print("///////////////////////////////////////////")
    #print("attr",selectAttrs)
    #print("///////////////////////////////////////////")
    if (len(selectAttrs)==1 and selectAttrs[0][0]=="*") or (len(selectAttrs)==0 and len(aggrAttrs)==0):
        #print("entities_astrisk",entities)
        response_model,ui_response_model =  get_astrisk_models(entities,modelsObject)
        response_model+=","
        selectAttrs=[]
    #print("entities",entities)
    all_entities_astrisk=[]
    sel_len=0
    for attr in selectAttrs:   
        if "*" in attr[0]:
            all_entities_astrisk.append(attr[0].split('.')[0])
        else:
            sel_len+=1
    all_entities_astrisk = list(set(all_entities_astrisk))
    if len(all_entities_astrisk):
        #print("all_entities_astrisk",all_entities_astrisk)
        response_model,ui_response_model =  get_astrisk_models(all_entities_astrisk,modelsObject)
        response_model+=","
    for attr in selectAttrs:
        #print("select ",attr)
        attr_name = attr[0]
        attr_type = attr[1]
        #print("attr_type",attr_type)
        #print("attr_name",attr_name)
        if "*" in attr:
            continue
        db_selects.append((attr_name,attr_type,None))

        if attr_type in pythondtypes_restmapping:
            response_model+= "'"+attr_name+"' : "+pythondtypes_restmapping[attr_type]+","
            ui_response_model[attr_name] = attr_type
        else:
            response_model+=  "'"+attr_name+"' : fields.String,"
            ui_response_model[attr_name] = "str"
            
    for attr in aggrAttrs:
        attr_aggregation = attr[1]
        attr_name = attr[0][0]
        attr_type = attr[0][1] if ("*" not in attr[0][0] and attr[1] != "count") else "int"
        db_selects.append((attr_name,attr_type,attr_aggregation))
        attr_name = attr_aggregation+"_"+ (attr_name if "*" not in attr_name else "all")
        if attr_name == "count_awards_players.playerID":print(attr)
        if attr_type in pythondtypes_restmapping:
            response_model+= "'"+attr_name+"' : "+pythondtypes_restmapping[attr_type]+","
            ui_response_model[attr_name] = attr_type
        else:
            response_model+=  "'"+attr_name+"' : fields.String ,"
            ui_response_model[attr_name] = "str"
    response_model = response_model[:-1]
    return response_model , ui_response_model ,db_selects

def get_astrisk_models(entities,modelsObjects):
    #print("inside astrisk",entities)
    all_models_response=''
    all_models_ui_response = {}
    for entity in entities:
        
        attrs = modelsObjects[entity]['attributes'].items()
        #print(attrs)
        attrs = [(entity+'.'+attr[0],attr[1]) for attr in attrs]
        #print(attrs)
        
        entity_model,entity_ui_model,_ = create_response_model(attrs,[],entities,modelsObjects)
        all_models_response+=entity_model+","
        all_models_ui_response.update(entity_ui_model)
    all_models_response = all_models_response[:-1]
    return all_models_response , all_models_ui_response


def get_attr_name_type(attrs):
    attr_names = []

    for attr in attrs:
        if type(attr[0])!=str:
            attr_name = attr[0][0] 
        else:
            attr_name = attr[0]
        if attr_name.find('*')!=-1:   
            #replace * with all
            attr_name = attr_name.replace('*','all')

        if type(attr[0])!=str and len(attr) > 2 and attr[2] != "value":
            attr_names.append(attr[2])    
        attr_names.append(attr_name)
    return attr_names

def query_renaming(entities,whereAttrs,groupAttrs,orderAttrs,isUpdate=False,is_group_all=False):
    #print("////////////////////////////////////////////")
    where_attr = get_attr_name_type(whereAttrs)
    if not isUpdate:
        group_attr = get_attr_name_type(groupAttrs)
    else:
        group_attr = groupAttrs
    if is_group_all:
        group_attr = ["all"]
    order_attr = get_attr_name_type(orderAttrs)
    #print("orrdderd by before" , order_attr)
    where_attr = set([attr[attr.find(".")+1:] for attr in where_attr if attr != "*"])
    order_attr = set([attr[attr.find(".")+1:] for attr in order_attr if attr != "*"])
    group_attr = set([attr[attr.find(".")+1:] for attr in group_attr if attr != "*"])
    endpoint_name = "get"+"_"+"_".join(entities)
    ui_name = "get "+" ".join(entities)
    #print("orrdderd by after" , order_attr)
    #print()
    #print("whereAttrs" , whereAttrs)

    #print("where_attr " , where_attr)
    #print()
    
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
    
    #print(endpoint_name)
    #print(endpoint_name)
    #print(ui_name)
    #print("////////////////////////////////////////////")
    
    return endpoint_name,ui_name

'''
-ask DR.khaled for queries names
-remove join condition from where
-check if we will allow cartesian products or not
'''         
'''
if attr doesn't have . before it then decide which entity has this attr
select from -> db.session.query(aggr(Entity.attr),Entity.attr2).join()
select from where-> db.session.query(aggr(Entity.attr),Entity.attr2).join().filter

select from where 
select aggr() from where group by
'''



def create_app_utils(api):
    app_utils = api.create_app_utils()
    with open('utils.py', 'w') as f:
        f.write(app_utils)
def create_app_env(api):
    app_env = api.create_app_env()
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

        

with open('/home/nada/GP/GP/src/SearchEngine/finalMergedQueries.json','rb') as file:
    testSchema = json.load(file)
    clusters = []
    for cluster in testSchema.keys():
        c = []
        for q in testSchema[cluster]:
            query = q[0]
            query.update({"constructed_query":q[1]})
            c.append(query)
        clusters.append(c)
    #print(clusters[0])
# with open('/home/nada/GP/GP/src/SearchEngine/finalMergedClusters.json','rb') as file:
#     testSchema = json.load(file)
#     clusters = [testSchema[cluster]["queries"] for cluster in testSchema.keys()]

    Create_Application({
        1: 
        {'TableName': 'awards_coaches', 
            'TableType':'',
            'attributes': {
            'id': 'str', 
            'coachID': 'str',
            'award': 'str',
            'lgID': 'str',
            'note': 'str',
            }, 
            'primaryKey': ['id'], 
            'ForgeinKey': [
            {
            'attributeName': 'coachID',
            'ForignKeyTable': 'coaches', 
            'ForignKeyTableAttributeName': 'coachID', 
            'patricipaction': 'partial', 
            'dataType': 'str'},
            ], 
            'isWeak': False
        },
        2: 
        {
            'TableName': 'awards_players', 
            'TableType':'',
            'attributes': {
            'playerID': 'str', 
            'award': 'str',
            'year': 'int',
            'lgID': 'str',
            'note': 'str',
            'pos': 'str'
            }
            , 
            'primaryKey': ['name','year','lgID']
            , 
            'ForgeinKey': [
            {
            'attributeName': 'playerID',
            'ForignKeyTable': 'players', 
            'ForignKeyTableAttributeName': 'playerID', 
            'patricipaction': 'partial', 
            'dataType': 'str'
            }
            ], 
            'isWeak': False
        },
        5:
        {
            'TableName': 'player_allstar', 
            'TableType':'',
            'attributes': {
            'playerID': 'str', 
            'last_name': 'str',
            'first_name': 'str',
            'season_id': 'str',
            'conference': 'str',
            'league_id': 'str',
            'games_played': 'str',
            'minutes': 'str',
            'points': 'str',
            'o_rebounds': 'str',
            'd_rebounds': 'str',
            'rebounds': 'str',
            'assists': 'str',
            'steals': 'str',
            'blocks': 'str',
            'turnovers': 'str',
            'personal_fouls': 'str',
            'fg_attempted': 'str',
            'fg_made': 'str',
            'ft_attempted': 'str',
            'ft_made': 'str',
            'three_attempted':  'str',
            'three_made': 'str',
            }, 
            'primaryKey': ['playerID'], 
            'ForgeinKey': [
            {
            'attributeName': 'playerID',
            'ForignKeyTable': 'players', 
            'ForignKeyTableAttributeName': 'playerID', 
            'patricipaction': 'partial', 
            'dataType': 'str'},
            ], 
            'isWeak': False
        },
        3:
        {
            'TableName': 'players', 
            'TableType':'',
            'attributes': {
            'playerID' : 'str',
            'useFirst' : 'str',
            'firstName' : 'str',
            'middleName' : 'str',
            'lastName' : 'str',
            'nameGiven' : 'str',
            'fullGivenName' : 'str',
            'nameSuffix' : 'str',
            'nameNick' : 'str',
            'pos' : 'str',
            'firstseason' : 'int',
            'lastseason' : 'int',
            'height' :'float',
            'weight' : 'int',
            'college' : 'str',
            'collegeOther' : 'str',
            'birthDate': 'datetime',
            'birthCity' : 'str',
            'birthState' : 'str',
            'birthCountry' : 'str',
            'highSchool' : 'str',
            'hsCity' : 'str',
            'hsState' : 'str',
            'hsCountry' : 'str',
            'deathDate': 'datetime',
            'race' : 'str',
            }
            , 
            'primaryKey': ['playerID']
            , 
            'ForgeinKey': [], 
            'isWeak': False
        },
        4:{
            'TableName': 'coaches',
            'TableType':'',
            'attributes': {
            'coachID': 'str', 
            'year': 'int',
            'tmID': 'str',
            'lgID': 'str',
            'stint': 'int',
            'won': 'int',
            'lost': 'int',
            'post_wins': 'int',
            'post_losses': 'int'},
            'primaryKey': ['coachID','year','tmID','stint'],
            'ForgeinKey': [
            # {
            # 'attributeName': 'tmID',
            # 'ForignKeyTable': 'teams', 
            # 'ForignKeyTableAttributeName': 'tmID', 
            # 'patricipaction': 'partial', 
            # 'dataType': 'str'}
            ]
        },
        6: 
        {
            'TableName': 'players_teams', 
            'TableType':'',
            'attributes': {
            'id' : 'int',
            'playerID' : 'str',
            'year' : 'int',
            'stint' : 'int',
            'tmID' : 'str',
            'lgID' : 'str',
            'GP' : 'int',
            'GS' : 'int',
            'minutes' : 'int',
            'points' : 'int',
            'oRebounds' : 'int',
            'dRebounds' : 'int',
            'rebounds' : 'int',
            'assists' : 'int',
            'steals' : 'int',
            'blocks' : 'int',
            'turnovers' : 'int',
            'PF' : 'int',
            'fgAttempted' : 'int',
            'fgMade' : 'int',
            'ftAttempted' : 'int',
            'ftMade' : 'int',
            'threeAttempted' : 'int',
            'threeMade' : 'int',
            'PostGP' : 'int',
            'PostGS' : 'int',
            'PostMinutes' : 'int',
            'PostPoints' : 'int',
            'PostoRebounds' : 'int',
            'PostdRebounds' : 'int',
            'PostRebounds' : 'int',
            'PostAssists' : 'int',
            'PostSteals' : 'int',
            'PostBlocks' : 'int',
            'PostTurnovers' : 'int',
            'PostPF' : 'int',
            'PostfgAttempted' : 'int',
            'PostfgMade' : 'int',
            'PostftAttempted' : 'int',
            'PostftMade' : 'int',
            'PostthreeAttempted' : 'int',
            'PostthreeMade' : 'int',
            'note' : 'str',
                }
                , 
                'primaryKey': ['id']
                , 
                'ForgeinKey': [
                {
                'attributeName': 'playerID',
                'ForignKeyTable': 'players', 
                'ForignKeyTableAttributeName': 'playerID', 
                'patricipaction': 'partial', 
                'dataType': 'str'
                },
                {
                'attributeName': 'tmID',
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'tmID',
                'patricipaction': 'partial', 
                'dataType': 'str'
                }
                ], 
                'isWeak': False
        },
        7: 
        {
            'TableName': 'draft', 
            'TableType':'',
            'attributes': 
            {'id': 'str', 
            'draftYear': 'int',
            'draftRound': 'str',
            'draftSelection':'str',
            'draftOverall': 'datetime',
            'tmID': 'str',
            'firstName':'str',
            'lastName':'str',
            'suffixName':'str',
            'playerID':'str',
            'draftForm':'str',
            'lgID':'str',
            }, 
            'primaryKey': ['id'], 
            'ForgeinKey': 
                [{'attributeName': 'tmID',
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'tmID', 
                'patricipaction': 'partial', 
                'dataType': 'str'},
                {'attributeName': 'draftYear',
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'year', 
                'patricipaction': 'partial', 
                'dataType': 'int'}
                ], 
            'isWeak': False
        },
        8: 
        {
            'TableName': 'series_post', 
            'TableType':'',
            'attributes': 
                {'id': 'str',
                'year': 'int',
                'round': 'str',
                'series': 'str',
                'tmIDWinner': 'str',
                'lgIDWinner': 'str',
                'tmIDLoser': 'str',
                'lgIDLoser': 'str',
                'w': 'str',
                'L': 'str',}, 
            'primaryKey': ['id'], 
            'ForgeinKey': 
                [{'attributeName': 'tmIDWinner', 
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'tmID', 
                'patricipaction': 'full', 
                'dataType': 'str'},
                {'attributeName': 'tmIDLoser', 
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'tmID', 
                'patricipaction': 'full', 
                'dataType': 'str'},
                {'attributeName': 'year', 
                'ForignKeyTable': 'teams', 
                'ForignKeyTableAttributeName': 'year', 
                'patricipaction': 'full', 
                'dataType': 'int'},
                ], 
            'isWeak': False
        },
        9:{
            'TableName': 'teams',
            'TableType':'',
            'attributes': {
                'year': 'int',
            'lgID' :'str',
            'tmID' : 'str',
            'franchID' : 'str',
            'confID': 'str',
            'divID': 'str',
            'rank' :'int',
            'confRank': 'int',
            'playoff': 'str',
            'name' : 'str',
                    },
                    'primaryKey': ['year','tmID'],
                    'ForgeinKey': []
        }

    },clusters)
    '''
    Create_Application({
        11: 
        {'TableName': 'DEPARTMENT', 
        'TableType':'',
        'attributes': {'name': 'str', 
        'start_date': 'datetime',
        'EMPLOYEE_Manages': 'str'}, 
        'primaryKey': ['name'], 
        'ForgeinKey': [{'attributeName': 'EMPLOYEE_Manages',
        'ForignKeyTable': 'EMPLOYEE', 
        'ForignKeyTableAttributeName': 'ssn', 
        'patricipaction': 'partial', 
        'dataType': 'str'}], 
        'isWeak': False},
        34: 
        {'TableName': 'DEPARTMENT_Clocation', 
        'TableType':'',
        'attributes': {'Clocation': 'str',
        'DEPARTMENT_name': 'str'}, 
        'primaryKey': ['Clocation', 
        'DEPARTMENT_name'], 
        'ForgeinKey': [{'attributeName': 'DEPARTMENT_name', 
        'ForignKeyTable': 'DEPARTMENT', 
        'ForignKeyTableAttributeName': 'name', 
        'patricipaction': 'full', 
        'dataType': 'str'}], 
        'isWeak': False}, 
        12: 
        {'TableName': 'EMPLOYEE',
        'TableType':'',
        'attributes': {'last_name': 'str', 
        'middle_initis': 'str', 
        'first_name': 'str', 
        'address': 'str',
        'salary': 'float',
        'sex': 'str', 
        'status': 'str', 
        'birth_dat': 'str', 
        'ssn': 'str',
        'start_date': 'datetime',
        'DEPARTMENT_Employed_name': 'str',
        'EMPLOYEE_Supervision_': 'str'},
        'primaryKey': ['ssn'], 
        'ForgeinKey': [{'attributeName': 'DEPARTMENT_Employed_name',
        'ForignKeyTable': 'DEPARTMENT', 'ForignKeyTableAttributeName': 'name',
        'patricipaction': 'full', 'dataType': 'str'}, 
        {'attributeName': 'EMPLOYEE_Supervision_', 
        'ForignKeyTable': 'EMPLOYEE', 
        'ForignKeyTableAttributeName': 'ssn',
        'patricipaction': 'partial', 
        'dataType': 'str'}], 
        'isWeak': False},
        24: {'TableName': 'PROJECT', 
        'TableType':'',
        'attributes': {'location': 'str',
        'name': 'str', 
        'budget': 'float',
        'DEPARTMENT_Assigned_name': 'str'}, 
        'primaryKey': ['name'], 
        'ForgeinKey': [{'attributeName': 'DEPARTMENT_Assigned_name',
        'ForignKeyTable': 'DEPARTMENT', 
        'ForignKeyTableAttributeName': 'name',
        'patricipaction': 'partial', 
        'dataType': 'str'}], 
        'isWeak': False}, 
        25: 
        {'TableName': 'DEPENDENT',
        'TableType':'',
        'attributes': {'sex': 'str', 
        'relatlonship': 'str',
        'name': 'str',
        'birth_date': 'datetime', 
        'Dependents_EMPLOYEE_': 'str'}, 
        'primaryKey': ['Dependents_EMPLOYEE_'], 
        'ForgeinKey': [{'attributeName': 'Dependents_EMPLOYEE_', 
        'ForignKeyTable': 'EMPLOYEE', 
        'ForignKeyTableAttributeName': 'ssn', 
        'patricipaction': 'partial', 
        'dataType': 'str'}], 
        'isWeak': True}, 
        35: 
        {'TableName': 'Works_EMPLOYEE_PROJECT', 
        'TableType':'mTm',
        'attributes': {'start_date': 'datetime', 
        'hours': 'int', 
        'EMPLOYEE_': 'str', 
        'PROJECT_': 'str'}, 
        'primaryKey': ['EMPLOYEE_', 'PROJECT_'], 
        'ForgeinKey': [{'attributeName': 'EMPLOYEE_', 
        'ForignKeyTable': 'EMPLOYEE',
        'ForignKeyTableAttributeName': 'ssn', 
        'patricipaction': 'full',
        'dataType': 'str'}, 
        {'attributeName': 'PROJECT_',
        'ForignKeyTable': 'PROJECT', 
        'ForignKeyTableAttributeName': 'name',
        'patricipaction': 'full',
        'dataType': 'str'}], 
        'isWeak': False}})
    '''