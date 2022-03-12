class DataGraph:
    def __init__(self):
        self.nodes = []
        self.node_map = {}

    def add_node(self,node,names):
        self.nodes.append(node)
        for name in names:
            self.node_map[name] = node

    def print_schema(self):
        for node in self.nodes:
            node.print_node()
        

class dataNode:
    def __init__(self,names):
        self.names = names
        self.ingoing = []
        self.outgoing_count = 0
    def add_ingoing(self,ingoing_node):
        self.ingoing.append(ingoing_node)
    def add_outgoing(self):
        self.outgoing_count += 1
    def print_node(self):
        print("-----------------")
        print("Node: " , self.names)
        print("Ingoing: ")
        for ingoing in self.ingoing:
            print(ingoing.names)
        print("Outgoing: " + str(self.outgoing_count))
        print("-----------------")

def read_data(file_name):
    df = pd.read_csv(file_name)
    return df

def is_entity_data(entity_attributes,csv_header):
    schema_concat = "".join(sorted(entity_attributes))
    csv_concat = "".join(sorted(csv_header))
    return schema_concat == csv_concat

def get_data_frames(csvs):
    data_frames = []
    for csv in csvs:
        df = pd.read_csv(csv)
        print("DATAFRAME")
        print(csv)
        print(df.head())
        data_frames.append(df)
    return data_frames

def map_schema_csvs(data_frames,schema_graph,data_filesNames):
    for node in schema_graph.nodes:
        for i,data_frame in enumerate(data_frames):
            print(node.attributes,data_frame.columns)
            if is_entity_data(node.attributes,data_frame.columns):
                node.file_name = data_filesNames[i]
                node.add_df(data_frame)
                break

def construct_data_graph(schema_filesNames,data_filesNames):
    data_graph = DataGraph()
    data = get_data_frames(data_filesNames)
    schema = SchemaGraph(schema_filesNames)
    map_schema_csvs(data,schema,data_filesNames)
    for p,node in enumerate(schema.nodes):
        print(p,node.name)
        #if node.df is None:
        #  print(node.name,node.attributes)
        rows_count = node.df.shape[0]
        df = node.df
        node_name = node.name+"_"         
        for i in range(rows_count):
            names =[]
            if(len(node.primary_key)):
              #if node.name.find('ScoringSC')!=-1:
              #    print("HELLO",node.primary_key)
              names.append( node_name +"_".join(node.primary_key)+ "_" + "_".join([str(df.at[i,pr]) for pr in node.primary_key]))
            for ck in node.candidate_keys:
                #if node.name.find('ScoringSC')!=-1:
                #  print("HELLO",node.candidate_keys)
                names.append(node_name+"_".join(ck) + "_" + "_".join([str(df.at[i,c]) for c in ck]))
            #if node.name=="employees":
            #print(node.name)
            data_node = dataNode(names)
            data_graph.add_node(data_node,names)
    return data_graph,schema
def add_graph_edges(data_graph,schema_graph):
    for p,node in enumerate(schema_graph.nodes):
        print(p,node.name)
        if not len(node.foreign_keys): continue
        from_node_name = node.name+"_" 
        rows_count = node.df.shape[0]
        df = node.df
        for i in range(rows_count):     
          if len(node.primary_key):
            data_node_name =  from_node_name +"_".join(node.primary_key)+"_" + "_".join([str(df.at[i,pr]) for pr in node.primary_key])
          else:
            data_node_name =  from_node_name +"_".join(node.candidate_keys[0]) +"_" + "_".join([str(df.at[i,pr]) for pr in node.candidate_keys[0]])
          from_data_node = data_graph.node_map[data_node_name]
          print(node.name,node.foreign_keys)
          for fk in node.foreign_keys:
              to_node_name = fk['ref_table']+"_" +"_".join(fk['ref_column']) +"_"+"_".join([str(df.at[i,c]) for c in fk['column']])
              if to_node_name.find('.0')!=-1:
                if data_graph.node_map.get(to_node_name) is None and data_graph.node_map.get(to_node_name[:-2]):
                  to_node_name = to_node_name[:-2]
              if data_graph.node_map.get(to_node_name) is None:
                #print("Not Found: ",to_node_name)
                continue
              
              to_data_node = data_graph.node_map[to_node_name]
              to_data_node.add_ingoing(from_data_node)
              from_data_node.add_outgoing()
                