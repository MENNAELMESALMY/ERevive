import os

dataTypes = {"str":"String(300)","int":"Integer","datetime":"DateTime","bool":"Boolean","float":"Float"}


def createModelsFolder():
    currentPath = os.getcwd() 
    modelPath = os.path.join(currentPath, "models")
    if not os.path.exists(modelPath):
        os.makedirs(modelPath)
    elif os.path.join(modelPath, "__init__.py"):
        with open(os.path.join(modelPath, "__init__.py"), 'w') as file:
            file.write("")

    return modelPath


def createModelFile(modelsPath,ob):
    tableName = ob['TableName']

    filePath = os.path.join(modelsPath, tableName+".py")
    initPath = os.path.join(modelsPath, "__init__.py")
    with open(initPath, 'a') as initFile:
        initFile.write(f'from .{tableName} import {tableName}\n')
    with open(filePath, 'w') as file:
        file.write("from app import db \n\n")
        file.write("class " + tableName +  "(db.Model):\n")
        file.write(f'\t__tablename__ = "{tableName}"\n')
        forgeinKeys = [[item['attributeName'],item['ForignKeyTable'],item['ForignKeyTableAttributeName']] for item in ob['ForgeinKey']]
        foreignAttributes= []
        if len(forgeinKeys)>0:
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
                isKey = "unique=True,primary_key=True"
            else:
                isKey = ""
            value = dataTypes[value]
            if key in foreignAttributes:
                keyIndex = foreignAttributes.index(key)
                isForgeinKey = f"db.ForeignKey('{foreignTable[keyIndex]}.{foreignTableAttribute[keyIndex]}',onupdate='CASCADE',ondelete='CASCADE')"
            else:
                isForgeinKey = ""
            if isKey != "" and isForgeinKey != "":
                file.write(f'\t{key} = db.Column(db.{value},{isForgeinKey},{isKey})\n')
            elif isKey != "" and isForgeinKey == "":
                file.write(f'\t{key} = db.Column(db.{value},{isKey})\n')
            elif isKey == "" and isForgeinKey != "":
                file.write(f'\t{key} = db.Column(db.{value},{isForgeinKey})\n')
            else:
                file.write(f'\t{key} = db.Column(db.{value})\n')

    foreignKeyRelation = {}
    return foreignKeyRelation,tableName,attributesList


def createAllModels(objectsList):
    foreignKeyRelationList = []
    outPutList = {}
    modelsObjects={}
    p = createModelsFolder()
    for tableObject in objectsList:
        foreignKeyRelation,tableName,tableAttributes = createModelFile(p,objectsList[tableObject])
        foreignKeyRelationList.append(foreignKeyRelation)
        outPutList[tableName] = tableAttributes
        modelsObjects[tableName] = objectsList[tableObject]

    for item in outPutList:
        tempPath = p
        modelPath = os.path.join(tempPath, item+".py")
        with open(modelPath, 'a') as file:
            ### form serialize method for each model
            file.write("\n\tdef serialize(self):\n")
            file.write("\t\treturn{\n")
            for attr in outPutList[item]:
                if modelsObjects[item]["attributes"][attr] == "datetime":
                    file.write(f'\t\t\t"{attr}": str(self.{attr}),\n')
                else:
                    file.write(f'\t\t\t"{attr}": self.{attr},\n')
            file.write("\t\t}\n")
    return outPutList ,modelsObjects




