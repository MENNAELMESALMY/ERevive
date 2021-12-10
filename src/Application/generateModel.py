import os

dataTypes = {"str":"String(300)","int":"Integer","datetime":"DateTime","bool":"Boolean","float":"Float"}

#### check if folder models is existed or not
#### if not create it
def createModelsFolder():
    currentPath = os.getcwd() 
    modelPath = os.path.join(currentPath, "models")
    if not os.path.exists(modelPath):
        os.makedirs(modelPath)

    return modelPath


def createModelFile(modelsPath,ob):
    tableName = ob['TableName']
    ### create new file with the name of table
    ### write initially the imports needed
    filePath = os.path.join(modelsPath, tableName+".py")
    initPath = os.path.join(modelsPath, "__init__.py")
    with open(initPath, 'a') as initFile:
        initFile.write(f'from .{tableName} import {tableName}\n')
    with open(filePath, 'a') as file:
        file.write("from app import db \n\n")
        file.write("class " + tableName +  "(db.Model):\n")
        file.write(f'\t__tablename__ = "{tableName}"\n')
        ## get foreign keys ##
        forgeinKeys = [[item['attributeName'],item['ForignKeyTable'],item['ForignKeyTableAttributeName']] for item in ob['ForgeinKey']]
        foreignAttributes = list(list(zip(*forgeinKeys))[0])
        foreignTable = list(list(zip(*forgeinKeys))[1])
        foreignTableAttribute = list(list(zip(*forgeinKeys))[2])
        primaryKeys = ob['primaryKey']
        isKey = ""
        isForgeinKey = ""
        attributesList = []
        for key,value in ob['attributes'].items():
            attributesList.append(key)
            if key in primaryKeys:
                isKey = "primary_key=True"
            else:
                isKey = ""
            value = dataTypes[value]
            if key in foreignAttributes:
                keyIndex = foreignAttributes.index(key)
                isForgeinKey = f"db.ForeignKey('{foreignTable[keyIndex]}.{foreignTableAttribute[keyIndex]}')"
            else:
                isForgeinKey = ""
            ### primary key
            if isKey != "" and isForgeinKey != "":
                file.write(f'\t{key} = db.Column(db.{value},{isForgeinKey},{isKey})\n')
            elif isKey != "" and isForgeinKey == "":
                file.write(f'\t{key} = db.Column(db.{value},{isKey})\n')
            elif isKey == "" and isForgeinKey != "":
                file.write(f'\t{key} = db.Column(db.{value},{isForgeinKey})\n')
            else:
                file.write(f'\t{key} = db.Column(db.{value})\n')

    ### foreign key relation
    if ob['TableType'] == "mTm":
        foreignKeyRelation = {
            'relationType':"mTm",
            'table1':foreignTable[0],
            'table2':foreignTable[1],
            'secondary':tableName,
            }
    elif len(ob['ForgeinKey']) != 0:
        foreignKeyRelation = {
            'relationType':"oTm",
            'table1':foreignTable[0],
            'table2':tableName,
            }
    else:
        foreignKeyRelation = {}
    return foreignKeyRelation,tableName,attributesList


def createAllModels(objectsList):
    foreignKeyRelationList = []
    outPutList = {}
    p = createModelsFolder()
    for tableObject in objectsList:
        foreignKeyRelation,tableName,tableAttributes = createModelFile(p,objectsList[tableObject])
        foreignKeyRelationList.append(foreignKeyRelation)
        outPutList[tableName] = tableAttributes
    ### add db.relation for some models
    for relationObject in foreignKeyRelationList:
        tempPath = p
        modelPath = os.path.join(tempPath, relationObject['table1']+".py")
        with open(modelPath, 'a') as file:
            ## check if item in foreignKeyRelationList, if found add db.relation
            if relationObject['relationType'] == "oTm":
                file.write(f"\t{relationObject['table2']} = db.relationship('{relationObject['table2']}',backref='{relationObject['table2']}')\n")
            elif relationObject['relationType'] == "mTm":
                file.write(f"\t{relationObject['table2']} = db.relationship('{relationObject['table2']}',secondary='{relationObject['secondary']}',backref=db.backref('{relationObject['table2']}',lazy='dynamic'))\n")
    
    for item in outPutList:
        tempPath = p
        modelPath = os.path.join(tempPath, item+".py")
        with open(modelPath, 'a') as file:
            ### form serialize method for each model
            file.write("\n\tdef serialize(self):\n")
            file.write("\t\treturn{\n")
            for attr in outPutList[item]:
                file.write(f'\t\t\t"{attr}": self.{attr},\n')
            file.write("\t\t}\n")
    return outPutList




