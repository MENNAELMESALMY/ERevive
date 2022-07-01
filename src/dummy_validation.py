from tkinter import NW, Tk,Frame, Canvas, OptionMenu, Variable,Label,Scrollbar,StringVar
from tkinter import RIGHT,Y
from turtle import window_height, window_width
from customtkinter import CTkEntry,CTkFrame,CTkCheckBox,CTkButton

global_schema = {
    11: 
    {'TableName': 'DEPARTMENT', 
    'TableType':'',
    'attributes': {
    'name': 'str', 
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
    'attributes': {
    'start_date': 'datetime', 
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
    'dataType': 'str'}
    ], 
    'isWeak': False}}

old_keys = list(global_schema.keys())
for old_key in old_keys:
    new_key = global_schema[old_key]['TableName']
    global_schema[new_key] = global_schema.pop(old_key)

dataTypes = ['str', 'int', 'float', 'datetime','bool']
participations = ['full', 'partial']

def addEntity():
    default_entity_name = 'entity_'+ str(len(global_schema))
    global_schema[default_entity_name] = {'TableName': default_entity_name, 
    'TableType':'',
    'attributes': {}, 
    'primaryKey': [], 
    'ForgeinKey': [], 
    'isWeak': False}
    entities_list.append(entity(default_entity_name,{}, [],[]))
    expandCanvas()
    updataAllForeignKeys()

def expandCanvas():
    validation_frame.update()
    height = validation_frame.winfo_height()
    canvas.itemconfigure("canvas_frame", height=height)
    canvas.configure(scrollregion=canvas.bbox("all"))

def saveChanges():
    # destroy errors if exists
    for err_lb in errors_labels: err_lb.destroy()
    errors=[]
    for entity in global_schema.values():
        entityName = entity['TableName']
        if len(entity['attributes'])==0: errors.append(f'{entityName} has no attributes')
        if len(entity['primaryKey'])==0: errors.append(f'{entityName} has no primary keys')
        for fk in entity['ForgeinKey']:
            fkName = fk['attributeName']
            fkTable = fk['ForignKeyTable']
            fkTableAttrName = fk['ForignKeyTableAttributeName']
            if entity['attributes'][fkName] == global_schema[fkTable]['attributes'][fkTableAttrName]:
                fk['dataType'] = entity['attributes'][fkName]
            else:
                errors.append(f'{fkName} foreignkey in {entityName} has type mismatch with attribute it is pointing to')
    if len(errors)>0: errors.append('cannot save changes')
    else: 
        print('------------------------------------------------------')
        print(global_schema)
    # add ui for errors
    for err in errors:
        err_lb = Label(errors_wrapper,text =err)
        err_lb.pack(fill='both', expand=True,padx=10, pady=10)
        errors_labels.append(err_lb)
    expandCanvas()


def updataAllForeignKeys(entityNameOld='',entityNameNew = ''):
    for entity in entities_list:
        for fk in entity.ForgeinKeysUI:
            if fk.removed:continue
            # print(entityNameOld,fk.entityName.get())
            if fk.entityName.get() == entityNameOld:
                #print("updating Name", fk.entityName.get())
                fk.update(entityNameOld,entityNameNew)
            else:
                #print("not updating entity Name", fk.entityName.get())
                fk.update()

def removeHangingForeignKeys(entityName='',attributeName = ''):
    for entity in entities_list:
        for fk in entity.ForgeinKeysUI:
            # print(entityNameOld,fk.entityName.get())
            if fk.removed:continue
            if fk.entityName.get() == entityName:
                # Is entity deleted 
                if entityName not in set(global_schema.keys()):
                    fk.removeForeignKey()
                elif attributeName not in set(global_schema[entityName]['attributes'].keys()):
                    #print("hihihi")
                    fk.removeForeignKey() 
class attribute:
    def __init__(self,wrapperFrame,entityName, name, dataType,isPrimaryKey):
        self.isInitialized = False
        self.entityName = entityName
        self.removed = False

        self.dataType = StringVar(wrapperFrame)
        self.dataType.set(dataType)

        self.nameStr = name
        self.name = StringVar(wrapperFrame)
        self.name.trace("w", lambda name, index, mode, sv=self.name: self.editAtrr(sv))
        self.name.set(name)

        
        self.attrName = CTkEntry(wrapperFrame,\
             textvariable=self.name, width=120)
        # self.attrName.grid(row=row)
        self.attrName.pack(fill='both', expand=True,padx=20, pady=20)

        
        self.dataTypeMenu = OptionMenu(wrapperFrame,\
            self.dataType,*dataTypes,command=self.changeDataType)
        self.dataTypeMenu.pack(fill='both', expand=True,padx=20, pady=20)

        # self.dataTypeMenu.grid(row=row+1)
        #self.isPrimaryKey = isPrimaryKey
        self.isPrimaryKey = Variable()
        self.isPrimaryCheckbox = CTkCheckBox(wrapperFrame, text = "isPrimaryKey", \
            variable=self.isPrimaryKey, command=self.isPrimaryKeyCheckbox)
        self.isPrimaryCheckbox.pack(fill='both', expand=True,padx=20, pady=20)
        # self.isWeakCheckBox.grid(row=row+1, column=3)
        self.isPrimaryKey.set(isPrimaryKey)
        if isPrimaryKey: self.isPrimaryCheckbox.select()

        self.removeAttrButton = CTkButton(wrapperFrame, \
            text="Remove Attribute",command=self.removeAttribute)

        self.removeAttrButton.pack(fill='both', expand=True,padx=20, pady=20)
        self.isInitialized = True


    def removeAttribute(self):
        entityName,attributeName = self.entityName,self.name.get()
        global_schema[self.entityName]['attributes'].pop(self.name.get())
        if self.name.get() in global_schema[self.entityName]['primaryKey']:
            global_schema[self.entityName]['primaryKey'].remove(self.name.get())
        self.attrName.destroy()
        self.isPrimaryCheckbox.destroy()
        self.dataTypeMenu.destroy()
        self.removeAttrButton.destroy()
        self.removed = True
        updataAllForeignKeys()
        removeHangingForeignKeys(entityName,attributeName)
    
    def editAtrr(self,sv):
        if sv.get() != self.nameStr:
            # print("Allah hallah")
            # print(self.entityName)
            global_schema[self.entityName]['attributes'][sv.get()] = self.dataType.get()
            global_schema[self.entityName]['attributes'].pop(self.nameStr)
            if self.nameStr in global_schema[self.entityName]['primaryKey']:
                global_schema[self.entityName]['primaryKey'].append(sv.get())
                global_schema[self.entityName]['primaryKey'].remove(self.nameStr)
            self.nameStr = sv.get()
            updataAllForeignKeys()
    
    def isPrimaryKeyCheckbox(self):
        if self.isInitialized:
            if not self.isPrimaryKey.get():
                global_schema[self.entityName]['primaryKey'].append(self.nameStr)
            else:
                global_schema[self.entityName]['primaryKey'].remove(self.nameStr)
            updataAllForeignKeys()

    def changeDataType(self,dataType):
        global_schema[self.entityName]['attributes'][self.name.get()]=dataType
        


class foreignKey:
    def __init__(self,wrapperFrame,name,belongToEntity,attributes ,entityName, entityAtrribute, patricipaction):
        self.wrapperFrame = wrapperFrame
        self.removed = False
        self.belongToEntity = belongToEntity
        entitiesList = list(global_schema.keys())
        self.l = [None]*4

        #Table that this foreign key is pointing to
        self.l[0] = Label(wrapperFrame,text ="Table Name")
        self.l[0].pack(fill='both', expand=True,padx=10, pady=10)
        self.entityName = StringVar(wrapperFrame)
        self.entityName.set(entityName)
        self.entitiesMenu = OptionMenu(wrapperFrame,self.entityName,\
            *entitiesList,command=self.updateAttributes)
        self.entitiesMenu.pack(fill='both', expand=True,padx=20, pady=20)

        #All Attributes of the table that this foreign key is pointing to
        self.l[1]=Label(wrapperFrame,text ="Attributes in Table")
        self.l[1].pack(fill='both', expand=True,padx=10, pady=10)
        self.entityAttribute = StringVar(wrapperFrame)
        self.entityAttribute.set(entityAtrribute)
        self.entityAttributes = [e for e in global_schema[entityName]['primaryKey']]
        self.entityAttributesMenu = \
            OptionMenu(wrapperFrame\
                ,self.entityAttribute,*self.entityAttributes)
        self.entityAttributesMenu.pack(fill='both', expand=True,padx=20, pady=20)

        attributesKeys = list(attributes.keys())
        self.l[2] =Label(wrapperFrame,text ="Attributes Name")
        self.l[2].pack(fill='both', expand=True,padx=10, pady=10)
        self.attrName = StringVar(wrapperFrame)
        self.attrName.set(name)
        self.attrNameMenu = OptionMenu(wrapperFrame,self.attrName,*attributesKeys)
        self.attrNameMenu.pack(fill='both', expand=True,padx=20, pady=20)

        self.l[3]=Label(wrapperFrame,text ="Participation")
        self.l[3].pack(fill='both', expand=True,padx=10, pady=10)
        ##PARTICIPATION
        self.participation = StringVar(wrapperFrame)
        self.participation.set(patricipaction)
        self.participationMenu = OptionMenu(wrapperFrame,self.participation,*participations)
        self.participationMenu.pack(fill='both', expand=True,padx=20, pady=20)

        self.removeAttrButton = CTkButton(wrapperFrame, \
            text="Remove Foreign key",command=self.removeForeignKey)

        self.removeAttrButton.pack(fill='both', expand=True,padx=20, pady=20)


    def removeForeignKey(self):
        if self.removed:return
        self.attrNameMenu.destroy()
        self.entityAttributesMenu.destroy()
        self.participationMenu.destroy()
        self.entitiesMenu.destroy()
        self.removeAttrButton.destroy()
        self.removed = True
        for i in range(4):
            self.l[i].destroy()
    
    def updateAttributes(self,entityName= None):
        # print("IO")
        if entityName is not None:
            self.entityName.set(entityName)
            # print("pppppppppppppppppppppppppppp",entityName)
            self.entityAttributes = [e for e in global_schema[entityName]['primaryKey']]
            if len(self.entityAttributes)>0: self.entityAttribute.set(self.entityAttributes[0])
            else: self.removeForeignKey();return
        else:
            entityName = self.entityName.get()
            self.entityAttributes = [e for e in global_schema[entityName]['primaryKey']]
            if self.entityAttribute.get() in self.entityAttributes:
                self.entityAttribute.set(self.entityAttribute.get())
            else:
                if len(self.entityAttributes)>0: self.entityAttribute.set(self.entityAttributes[0])
                else: self.removeForeignKey();return
        
        self.entityAttributesMenu["menu"].delete(0, 'end')
        # print("attr",self.entityAttributes)
        for choice in self.entityAttributes:
            self.entityAttributesMenu["menu"]\
                .add_command(label=choice, command= lambda a=choice: \
                    self.entityAttribute.set(a))
    
    def updateEntities(self,entityName= None):
        if entityName is not None:
            self.entityName.set(entityName)
        # self.entitiesMenu["menu"].delete(0, 'end')
        entitiesList = list(global_schema.keys())
        self.entitiesMenu["menu"].delete(0, 'end')

        for choice in entitiesList:
            self.entitiesMenu["menu"]\
                .add_command(label=choice, command= lambda a=choice: \
                   [ self.entityName.set(a),self.updateAttributes(a) ])

    def updateAttrs(self,entityName= None):
        if entityName is not None: self.belongToEntity = entityName
        Attrs = list(global_schema[self.belongToEntity]['attributes'].keys()) 
        self.attrNameMenu["menu"].delete(0, 'end')

        if self.attrName.get() not in Attrs:
            if len(Attrs)==0:self.attrName.set('')
            else:self.attrName.set(Attrs[0])

        for choice in Attrs:
            self.attrNameMenu["menu"]\
                .add_command(label=choice, command= lambda a=choice: \
                    self.attrName.set(a))


    def update(self,entityNameOld=None,entityNameNew= None):

        self.updateEntities(entityNameNew)
        if self.belongToEntity == entityNameOld: 
            self.updateAttrs(entityNameNew)
        else:
            self.updateAttrs()
        self.updateAttributes(entityNameNew)

class entity:
    def __init__(self, name, attributes, \
        primaryKeys, ForgeinKeys,row,col,rowspan):
        self.isInitialized = False
        self.entityCurName = name
        self.wrapper = Frame(entities_wrapper, highlightthickness=2, highlightbackground='black')
        self.attWrapper = Frame(self.wrapper, highlightthickness=2, highlightbackground='black')

        self.attributes = {}
        self.primaryKeys = set(primaryKeys)
        self.ForgeinKeys = ForgeinKeys
        # Entity Name
        self.name = StringVar(self.wrapper)
        self.name.set(name)
        self.name.trace("w", lambda name, index, mode, sv=self.name: self.editEntityName(sv))

        self.entityName = CTkEntry(self.wrapper,\
             textvariable=self.name, width=120)
        self.entityName.pack(fill='both', expand=True,padx=20, pady=20)

        # Is Weak
        self.isWeak = Variable()
        self.isWeakCheckBox = CTkCheckBox(self.wrapper, text = "isWeak", variable=self.isWeak,command=self.isWeakChecked)
        self.isWeak.set(int(value['isWeak']))
        self.isWeakCheckBox.pack(fill='both', expand=True,padx=20, pady=20)
        # Attributes
        self.attrLabel = Label(self.wrapper,text ="___Attributes__")
        self.attrLabel.pack(fill='both', expand=True,padx=10, pady=10)

        for attributeName,dataType in attributes.items():
            self.attributes[attributeName] =attribute(self.attWrapper,name,\
                attributeName, dataType,attributeName in self.primaryKeys)

        # self.wrapper.pack(fill='both', expand=True,padx=20, pady=20)
        #self.wrapper.update()
        #print(self.wrapper.winfo_height())
        self.wrapper.grid(row=row, column=col,\
            columnspan=1, sticky='news',padx=(10, 10),pady=(10,10))

        self.attWrapper.pack(fill='both', expand=True,padx=20, pady=20)

        self.newAttrButton = CTkButton(self.wrapper, \
            text="Add Attribute",command=self.addAttribute)

        self.newAttrButton.pack(fill='both', expand=True,padx=20, pady=20)

        self.foreibnLabel = Label (self.wrapper,text ="__Foreign Keys__")
        self.foreibnLabel.pack(fill='both', expand=True,padx=10, pady=10)
        self.foreignKeyWrapper = Frame(self.wrapper, highlightthickness=2, highlightbackground='black')

        self.ForgeinKeysUI = []
        for f in ForgeinKeys:
            fk = foreignKey(self.foreignKeyWrapper,f['attributeName']\
                ,self.name.get(),attributes,f['ForignKeyTable'], \
                f['ForignKeyTableAttributeName'], f['patricipaction'])
            self.ForgeinKeysUI.append(fk)

        self.foreignKeyWrapper.pack(fill='both', expand=True,padx=20, pady=20)
        self.isInitialized = True


        self.newFKButton = CTkButton(self.wrapper, \
            text="Add Foreign Key",command=self.addForeignKey)

        self.newFKButton.pack(fill='both', expand=True,padx=20, pady=20)

        self.deleteEntityButton = CTkButton(self.wrapper, \
            text="Delete Entity",command=self.deleteEntity)

        self.deleteEntityButton.pack(fill='both', expand=True,padx=20, pady=20)
    
    def addAttribute(self):
        attr_default_name = "attr" + str(len(self.attributes)+1)
        self.attributes[attr_default_name] =\
             attribute(self.attWrapper,self.name.get(),attr_default_name, "str",False)
        global_schema[self.name.get()]['attributes'][attr_default_name] = "str"
        expandCanvas()
        updataAllForeignKeys()

    def isWeakChecked(self):
        if self.isInitialized:
            global_schema[self.name.get()]['isWeak'] = not self.isWeak.get()

    def editEntityName(self,sv):
        if self.isInitialized:
            old_key = self.entityCurName
            new_key = sv.get()
            global_schema[old_key]['TableName'] = new_key
            global_schema[new_key] = global_schema.pop(old_key)#global_schema[old_key]
            updataAllForeignKeys(old_key,new_key)
            for attrKey in self.attributes.keys():
                if self.attributes[attrKey].entityName == old_key:
                    self.attributes[attrKey].entityName = new_key
            self.entityCurName = new_key
            ######################

    def addForeignKey(self):
        # default to first entity and to first primary key
        attributeName = list(self.attributes.keys())[0]
        default_participation = 'full'
        default_table = list(global_schema.keys())[0]
        default_attribute = global_schema[default_table]['primaryKey'][0]
        fk = foreignKey(self.foreignKeyWrapper,attributeName\
                ,self.name.get(),self.attributes,default_table, \
                default_attribute,default_participation)
        self.ForgeinKeysUI.append(fk)

        new_fk = { 'attributeName': attributeName, 
            'ForignKeyTable': default_table, 
            'ForignKeyTableAttributeName':default_attribute , 
            'patricipaction': 'full', 
            'dataType': self.attributes[attributeName]}
        
        global_schema[self.entityCurName]['ForgeinKey'].append(new_fk)
        expandCanvas()
        
    def deleteEntity(self):
        # delete attributes
        for att in self.attributes.values():att.removeAttribute()
        # delete FK
        for fk in self.ForgeinKeysUI: fk.removeForeignKey()
        # delete isweak,Name,buttons
        self.entityName.destroy()
        self.isWeakCheckBox.destroy()
        self.attrLabel.destroy()
        self.attWrapper.destroy()
        self.foreibnLabel.destroy()
        self.newAttrButton.destroy()
        self.newFKButton.destroy()
        self.deleteEntityButton.destroy()
        self.foreignKeyWrapper.destroy()
        self.wrapper.destroy()
        # remove from object
        global_schema.pop(self.name.get())


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg = "#FFFFFF")

root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = Frame(root, bg="gray")
frame_main.grid(sticky='news')
frame_main.grid_propagate(0)

# Create a frame for the canvas with non-zero row&column weights
validation_frame = Frame(frame_main)
validation_frame.grid(row=0, column=0, sticky='nw')
validation_frame.grid_rowconfigure(0, weight=1)
validation_frame.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
validation_frame.grid_propagate(False)

# Add a canvas in that frame
canvas = Canvas(validation_frame, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = Scrollbar(validation_frame, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
entities_wrapper = Frame(canvas, bg="blue")
canvas.create_window((10, 10), window=entities_wrapper, anchor='nw')

entities_list = []
row,col=0,0
max_rowspan = 0
# group of widgets
for _, value in global_schema.items():
    rowspan=len(value['attributes'])
    max_rowspan = max(max_rowspan,rowspan)
    entities_list.append(entity(value['TableName'],\
         value['attributes'], value['primaryKey'],\
              value['ForgeinKey'],row,col,rowspan))
    if col!=0 and col == 6:
        row +=max_rowspan
        max_rowspan=0
    col = (col+1)%7#+3)%12

# Update buttons frames idle tasks to let tkinter calculate buttons sizes
entities_wrapper.update_idletasks()

# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
width = screen_width -vsb.winfo_width() -50#sum([buttons[0][j].winfo_width() for j in range(0, 5)])
height = screen_height-70 #sum([buttons[i][0].winfo_height() for i in range(0, 5)])
validation_frame.config(width=width ,
                    height=height)

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# Launch the GUI
root.mainloop()
