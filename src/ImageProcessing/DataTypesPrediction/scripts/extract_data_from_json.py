import json 
import csv
import os
import re
import sys
import collections
import matplotlib.pyplot as plt

wordName = []

def readFile(path):
    file = open(path,'r')
    file_dic = json.loads(file.read())
    file.close()
    file_str = json.dumps(file_dic)
    return file_str 


def extractVariables(file_str,dic):
    data = []
    variables_lists = re.findall('"variables": {.*?}', file_str)
    for variables_list in variables_lists:
        variables_list = variables_list.split('"variables": ')[-1]
        variables_dic = json.loads(variables_list)
        for variable,t in variables_dic.items():
            if "datetime" in t.lower():
                t = "datetime"
            if t != "" and variable not in wordName and t in ["builtins.str" , "builtins.int" , "builtins.bool" , "builtins.float" , "datetime"]:
                t = t.split(".")[-1]
                wordName.append(variable)
                data.append([variable,t])

                #counting the values of each type
                if t in dic:
                    dic[t] +=1
                else:
                    dic[t] = 1
    return data , dic


def writeToCSVFile(uniqeData,filename):
    f = open(filename, 'w')
    writer = csv.writer(f)
    writer.writerows(uniqeData)


def parseMultipleFiles(inPath ,outPath):
    files = os.listdir(inPath)
    filesnum = len(files)
    data = [['word','dataType']]
    index = 0
    stat = {}
    for file in files:  
        if index%100 == 0:
            print(index)
        if file.split('.')[-1] == 'json':
            cFile = readFile(inPath+'/'+file)
            fileData , stat = extractVariables(cFile,stat) 
            data = data + fileData
        index +=1

    writeToCSVFile(data, outPath+'/'+"data.csv")

    
    ##########################################
    sort_orders = sorted(stat.items(), key=lambda x: x[1], reverse=True)
    index=0
    for i in sort_orders:
        if index <=50:
            #print(i[0], i[1])
            index+=1

    a_file = open(outPath+'/'+"data.json", "w")
    json.dump(sort_orders, a_file)
    a_file.close()

    sort_orders_dic = collections.OrderedDict(sort_orders)
    x = list(sort_orders_dic.keys())
    y = list(sort_orders_dic.values())
    fig = plt.figure(figsize = (10, 5))
    
    plt.bar(x, y, color ='blue',width = 0.4)
    plt.xlabel("data types")
    plt.ylabel("count of each data type")
    plt.title("dataset statistics")
    plt.show()
    fig.savefig(outPath+'/'+'dataset_statistics.png')
    ###########################################
 

def main():
    if len(sys.argv)==1:
        print("Enter the directory .")
    elif len(sys.argv)==2:
        parseMultipleFiles(str(sys.argv[1]),str(sys.argv[1]))
    else:
        parseMultipleFiles(str(sys.argv[1]),str(sys.argv[2]))

        
if __name__ == "__main__":
    main()

