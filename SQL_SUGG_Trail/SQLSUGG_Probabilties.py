import pandas as pd
def PRni(datanode,N):

  prni = ((1-d)/N)
  pn=0
  for in_going_node in datanode.ingoing:
    pn+=(PRni(in_going_node,N)/in_going_node.outgoing_count)
  prni = prni+d*pn
  return prni
  
def P_RgivenT(R,datagraph,schemagraph):
  PR=0
  R = schemagraph.node_map[R]
  rows_count = R.df.shape[0]
  df = R.df
  for i in range(rows_count):
    if len(R.primary_key):
      node_name =  R.name +"_"+"_".join(R.primary_key)+ "_" + "_".join([str(df.at[i,pr]) for pr in R.primary_key])
    else:
      node_name =  R.name +"_"+"_".join(R.candidate_keys[0]) +"_" + "_".join([str(df.at[i,pr]) for pr in R.candidate_keys[0]])
    datanode = datagraph.node_map[node_name]
    PR+=PRni(datanode,len(datagraph.nodes))
  return PR/R.df.shape[0]


def getKjointR(K,R,schema_graph,node_file):
    # if K is the R name then it's the count of data frames rows
    # if K is the same of ony of the attributes then it's the count of df having this attribute
    # else count K on the values
    # P(R) is the count of entities in the schema topic having the same name
    # Normalize the result
    
    count_K_joint_R = 0
    node = schema_graph.node_map[R]
    node_df = pd.read_csv(node_file)
    if K == R:
        count_K_joint_R = node_df.shape[0]
    elif K in node.attributes:
        count_K_joint_R = node_df[K].value_counts().values.sum()
    else:
        #get all the occurrences of K in the dataframe
        sum_occurences =0
        for i in node.attributes:
            try:
                values = list(node_df[i].value_counts().keys())
                values = " ".join(values)
                sum_occurences +=values.count(K) 
            except:
                continue
        count_K_joint_R = sum_occurences
    return count_K_joint_R
    
def getKgivenR(K,R,schemagraph,node_file,topic):
  # if K is the R name then it's the count of data frames rows
  # if K is the same of ony of the attributes then it's the count of df having this attribute
  # else count K on the values
  # P(R) is the count of entities in the schema topic having the same name
  # Normalize the result
  count_K_joint_R = getKjointR(K,R,schemagraph,node_file)
  count_R = topic['entities'].count(R)
  return count_K_joint_R/count_R

