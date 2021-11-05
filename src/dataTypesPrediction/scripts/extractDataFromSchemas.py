#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:02:13 2021

@author: hager
"""
import re
import os
import sys
import csv
import collections
import pandas as pd
import matplotlib.pyplot as plt

#######################global variables####################### 
pythonTypes = [['STR','CHAR','NCHAR','VARCHAR','NVARCHAR','TEXT','LONGTEXT','MEDIUMTEXT','TINYTEXT'],
               ['INTEGER','INT','TINYINT','BIGINT','SMALLINT','MEDIUMINT','INTEGER'],
               ['TIME','DATETIME','DATE','TIMESTAMP','TIME','YEAR'],
               ['FLOAT','DECIMAL','DOUBLE','FLOAT','REAL','NUMERIC'],
               ['BLOB','MEDIUMBLOB','TINYBLOB','LONGBLOB'],
               ['ENUM','ENUM'],
               ['BINARY','VARBINARY','BITBINARY','BIT','BINARY','BOOL']]

types = ['CHAR','DATETIME','VARCHAR','INT','DOUBLE']
data = [['CHAR'],['DATETIME'],['VARCHAR'],['INT'],['DOUBLE']]
data2 = [['word','dataType']]
dummyUnique = []
##############################################################

def getCommands(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # remove endlines and tabs with spaces and remove extra spaces
    sqlFile = sqlFile.replace('\n', ' ').replace('\r', '')
    sqlFile = re.sub("\s\s+" , " ", sqlFile)
    
    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    return sqlCommands


def cleanColName(colName):
    #remove names with one character 
    if len(colName) <= 1:
        return False , ""
    
    #remove names that are only numbers
    result = re.search("^[ 0-9]+$", colName)
    if result is not None:
        return False , ""
    
    #remove numbers at the end of the string 
    colName = re.sub("[0-9]+$", '', colName)
    
    #replace _ with space
    colName = colName.replace("_"," ")
    
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
    return True,colName
    

def extractDataTypes(sqlCommands):
    columnName = []
    dataType = []
    for command in sqlCommands:
        #remove endlines and tabs
        command = command.strip()
        
        #find the create table command
        if command[0:12].upper() == "CREATE TABLE":  
            # split on ( and remove it
            temp = command.split("(",1)
            if(len(temp)==2):
                command = temp[1]
            
            # split the rest of the command on , 
            attributes = command.split(',')
            for attribute in attributes:
                attribute = attribute.strip()
                c = attribute[0]
                if c == '`' or c == '"':
                    if c=='`':
                        colName = re.search('`(.*)`', attribute)
                    else:
                        colName = re.search('"(.*)"', attribute)
                    isValidName , name = cleanColName(colName.group(1))
                    if isValidName == True:
                        columnName.append(name)
                        attribute = attribute.replace('\t', ' ')
                        dataType.append(((attribute.split(c+colName.group(1)+c+' ')[1]).strip().split()[0].split('(')[0]).upper())
                else: break         
    return columnName,dataType
                

def sortTypes(columnName ,dataType):
    index = 0
    for d in dataType:
        try:
            i = types.index(d)
            data[i].append(columnName[index])
        except ValueError:
            types.append(d)
            data.append([d,columnName[index]])   
        index+=1    


def removeDublicates2(columnNames ,dataTypes):
    for i , w in enumerate(dataTypes):
        for l in pythonTypes:
            if w in l:
                dataTypes[i] = l[0]
    
    for i , word in enumerate(columnNames):
        if(word not in dummyUnique and dataTypes[i] not in ['GEOMETRY' ,'SET' ,'BLOB' , 'ENUM']):
            dummyUnique.append(word)
            data2.append([word,dataTypes[i]])


def removeDublicates():
    uniqeData = []
    for i in range(len(data)):
        uniqeData.append([data[i][0]])
    
    for i in range(len(data)):
        dataTypeList = data[i]
        for word in dataTypeList:
            if word not in uniqeData[i]:
                uniqeData[i].append(word)
                
    return uniqeData
  
    
def parseMultipleFiles(inPath ,outPath):
    files = os.listdir(inPath)
    filesnum = len(files)
    index = 0
    for file in files:  
        if index%10 == 0: 
            print("parsing file no "+str(index)+" out of "+str(filesnum)+" ........")
        sqlCommands = getCommands(inPath+'/'+file)
        columnName , dataType = extractDataTypes(sqlCommands)
        removeDublicates2(columnName , dataType)
        sortTypes(columnName ,dataType)
        index+=1
    print("finished parsing "+str(index)+" out of "+str(filesnum)+" .........")
    print("start extracting unique data .....")
    uniqueData = removeDublicates()
    print("finished extracting uniue data ......")
    writeToCSVFile(data2, outPath+'/'+"data.csv")

    
    ##########################################
    #printing dataset statistics
    stat = {}
    for i in range(len(uniqueData)):
        if len(uniqueData[i])-1 > 0 and uniqueData[i][0] not in ['GEOMETRY' ,'SET' ,'BLOB' , 'ENUM']:
            stat[uniqueData[i][0]] = len(uniqueData[i])-1
        #print(str(uniqueData[i][0]) +": "+str(len(uniqueData[i])))
    sort_orders = sorted(stat.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        print(i[0], i[1])

    #ploting dataset statistics
    sort_orders_dic = collections.OrderedDict(sort_orders)
    x = list(sort_orders_dic.keys())
    y = list(sort_orders_dic.values())
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(x, y, color ='blue',width = 0.4)
    plt.xlabel("data types")
    plt.ylabel("count of each data type")
    plt.title("dataset statistics")
    plt.show()
    fig.savefig(outPath+'/'+'dataset_statistics.png')
    ###########################################
        

def writeToCSVFile(uniqeData,filename):
    f = open(filename, 'w')
    writer = csv.writer(f)
    writer.writerows(uniqeData)

        
def main():
    if len(sys.argv)==1:
        print("Enter the directory of the schemas and the directory of the output file.")
    elif len(sys.argv)==2:
        parseMultipleFiles(str(sys.argv[1]),str(sys.argv[1]))
    else:
        parseMultipleFiles(str(sys.argv[1]),str(sys.argv[2]))

        
if __name__ == "__main__":
    main()



