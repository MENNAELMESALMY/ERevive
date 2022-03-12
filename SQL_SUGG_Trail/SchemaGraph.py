import re
class node():
    def __init__(self,name):
        self.name = name
        self.edges = []
        self.attributes = []
        self.primary_key = []
        self.candidate_keys = []
        self.foreign_keys = []
        self.df = None
        self.mapped_attributes={}
        self.mapped_entity = None
        self.file_name = None
    def add_df(self,df):
        self.df = df
    def add_attribute(self,attribute):
        self.attributes.append(attribute)
    def add_primary_key(self,attribute):
        self.primary_key = sorted(attribute)
    def add_foreign_key(self,fk):
        self.foreign_keys.append(fk)
    def add_candidate_key(self,ck):
        self.candidate_keys.append(sorted(ck))
    def add_edge(self,edge):
        self.edges.append(edge)
    def set_mapped_attributes(self,mapAttr):
        self.mapped_attributes = mapAttr
    def set_mapped_entity(self,mappedEntity):
        self.mapped_entity = mappedEntity
    def print_node(self):
        print("---------------------------------------------------------")
        print("Node name: " + self.name)
        print("Node attributes: " + str(self.attributes))
        print("Node primary key: " + str(self.primary_key))
        print("Node edges: " + str(self.edges))
        print("Node foreign keys: " + str(self.foreign_keys))
        print("Node candidate keys: " + str(self.candidate_keys))
        print("Node mapped attributes: " + str(self.mapped_attributes))
        print("---------------------------------------------------------")



class SchemaGraph():
    def __init__(self,files_names):
        self.files_names = files_names
        self.nodes = []
        self.node_map = {}
        self.edge_map = {}
        self.read_schema()
    def read_schema(self):
        schemas = self.files_names
        for schema in schemas: 
            node = executeScriptsFromFile(schema)
            self.add_node(node)
        for node in self.nodes:
            for edge in node.edges:
                self.add_edge(node,self.node_map[edge])

    def add_node(self,node):
        self.nodes.append(node)
        self.node_map[node.name] = node

    def add_edge(self,node1,node2):
        self.edge_map[(node1.name,node2.name)] = self.get_join_condition(node1,node2)

    def get_join_condition(self,node1,node2):
        join_conditions = []
        for fk in node1.foreign_keys:
            if fk['ref_table'] == node2.name:
                join_condition = None
                for i,column in enumerate(fk['column']):
                    if join_condition == None:
                        join_condition = node1.name+"."+column + "=" + fk['ref_table'] + "." + fk['ref_column'][i]
                    else:
                        join_condition = join_condition + " AND " + node1.name+"."+column + "=" + fk['ref_table'] + "." + fk['ref_column'][i]
                join_conditions.append(join_condition)
        return join_conditions
    
    def print_schema(self):
        for node in self.nodes:
            node.print_node()
        print("Edge map: " + str(self.edge_map))

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';\n')

    # Execute every command from the input file
    
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        
        if(command.find('CREATE TABLE')!=-1):
            tableName = command[command.find('`')+1:]
            tableName = tableName[:tableName.find('`')]
            tableNode = node(tableName)
            
            tableAttributesWithBrackets = command[command.find('(')+1:command.find('ENGINE')]
            tableAttributesWithBrackets = tableAttributesWithBrackets.strip()
            tableAttributes = tableAttributesWithBrackets.strip(')')
            #print(tableAttributes)
            tableAttributes = tableAttributes.split(',\n')
            for attribute in tableAttributes:
                #print(attribute)
                attribute = attribute.strip()
                attribute = attribute.replace('\n','')

                if attribute.find('PRIMARY KEY')!=-1:
                    attribute = attribute.strip()
                    brackIndex = attribute.rfind(')')
                    attribute = attribute[attribute.find('(')+1:brackIndex]
                    attribute = re.sub(r'(?<=\()(.*?)(?=\))','',attribute)
                    attribute = attribute.replace('`','').replace('()','')
                    tableNode.add_primary_key(attribute.split(','))
                elif attribute[0]=='`':
                    attribute = attribute[1:]
                    attribute_name = attribute[0:attribute.find('`')]
                    tableNode.add_attribute(attribute_name)
                elif attribute.find('FOREIGN KEY')!=-1:
                    
                    column = attribute[attribute.find('FOREIGN KEY')+13:attribute.find(')')]
                    column = column.replace('`','')
                    ref_attr = attribute[attribute.find('REFERENCES'):]
                    ref_table = ref_attr[11:ref_attr.find('(')]
                    ref_table = ref_table.replace('`','').strip()
                    ref_column = ref_attr[ref_attr.find('(')+1:ref_attr.find(')')]
                    ref_column = ref_column.replace('`','')
                    ref_columns = ref_column.split(',')
                    ref_columns = [rc.strip() for rc in ref_columns]
                    columns = column.split(',')
                    columns = [rc.strip() for rc in columns]
                    fk = {'ref_table':ref_table,'ref_column': sorted(ref_columns),'column':sorted(columns)}
                    tableNode.add_foreign_key(fk)
                    tableNode.add_edge(ref_table)
                elif attribute.find('UNIQUE KEY')!=-1:
                    attribute = attribute.strip()
                    brackIndex = attribute.rfind(')')
                    attribute = attribute[attribute.find('(')+1:brackIndex]                    
                    attribute = re.sub(r'(?<=\()(.*?)(?=\))','',attribute)
                    attribute = attribute.replace('`','').replace('()','')
                    tableNode.add_candidate_key(attribute.split(','))
                elif attribute.find('FULLTEXT KEY')!=-1:
                    attribute = attribute.strip()
                    brackIndex = attribute.rfind(')')
                    attribute = attribute[attribute.find('(')+1:brackIndex]                    
                    attribute = re.sub(r'(?<=\()(.*?)(?=\))','',attribute)
                    attribute = attribute.replace('`','').replace('()','')
                    tableNode.add_candidate_key(attribute.split(','))
                elif attribute.find('KEY')!=-1:
                    attribute = attribute.strip()
                    brackIndex = attribute.rfind(')')
                    attribute = attribute[attribute.find('(')+1:brackIndex]                    
                    attribute = re.sub(r'(?<=\()(.*?)(?=\))','',attribute)
                    attribute = attribute.replace('`','').replace('()','')
                    tableNode.add_candidate_key(attribute.split(','))
            return tableNode

def createGraphSchema(files_names):
    schema_graph = SchemaGraph(files_names)
    #schema_graph.print_schema()
    return schema_graph

