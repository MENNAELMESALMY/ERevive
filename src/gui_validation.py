from tkinter import Tk,Frame, Canvas, OptionMenu, Variable,Label,Scrollbar,StringVar
from tkinter import RIGHT,Y
from customtkinter import CTkEntry,CTkFrame,CTkCheckBox,CTkButton
from numpy import pad

global_schema = {}

validation_frame = None
canvas = None
errors_labels = []
errors_wrapper = None
entities_list = []
# print(global_schema)

dataTypes = ['str', 'int', 'float', 'datetime','bool']
participations = ['full', 'partial']

def addEntity():
    global entities_list,row,col,ROWCOUNT,entities_wrapper
    global global_schema
    default_entity_name = 'entity_'+ str(len(global_schema))
    global_schema[default_entity_name] = {'TableName': default_entity_name, 
    'TableType':'',
    'attributes': {}, 
    'primaryKey': [], 
    'ForgeinKey': [], 
    'isWeak': False}
    entities_list.append(entity(default_entity_name,{}, [],[],\
        entities_wrapper,global_schema[default_entity_name],row,col))
    if col!=0 and col == ROWCOUNT-1:
        row +=1
    col = (col+1)%ROWCOUNT#+3)%12
    expandCanvas()
    updataAllForeignKeys()

def expandCanvas():
    global validation_frame
    global canvas
    validation_frame.update()
    height = validation_frame.winfo_height()
    canvas.itemconfigure("canvas_frame", height=height)
    canvas.configure(scrollregion=canvas.bbox("all"))

def saveChanges():
    # destroy errors if exists
    global errors_labels
    global global_schema
    for err_lb in errors_labels:
        err_lb.destroy()
    errors=[]
    print(global_schema)
    for entity in global_schema.values():
        entityName = entity['TableName']
        if len(entity['attributes'])==0: errors.append(f'{entityName} has no attributes')
        if len(entity['primaryKey'])==0: errors.append(f'{entityName} has no primary keys')
        print(entity)
        for fk in entity['ForgeinKey']:
            print("FK: ",fk)
            fkName = fk['attributeName']
            fkTable = fk['ForignKeyTable']
            fkTableAttrName = fk['ForignKeyTableAttributeName']
            print("entity['attributes']",entity['attributes'])
            print("global_schema[fkTable]['attributes']",global_schema[fkTable]['attributes'])
            if entity['attributes'][fkName] == global_schema[fkTable]['attributes'][fkTableAttrName]:
                fk['dataType'] = entity['attributes'][fkName]
            else:
                errors.append(f'{fkName} foreignkey in {entityName} has type mismatch with attribute it is pointing to')
    if len(errors)>0: errors.append('cannot save changes')
    else: 
        print('------------------------------------------------------')
        print(global_schema)
    # add ui for errors
    global errors_wrapper
    for err in errors:
        err_lb = Label(errors_wrapper,text =err)
        err_lb.pack(fill='both', expand=True,padx=10, pady=10)
        errors_labels.append(err_lb)
    expandCanvas()


def updataAllForeignKeys(entityNameOld='',entityNameNew = ''):
    global entities_list
    global global_schema
    for entity in entities_list:
        for fk in entity.ForgeinKeysUI:
            if fk.removed:continue
            # print(entityNameOld,fk.entityName.get())
            if fk.entityName.get() == entityNameOld:
                print("updating Name", fk.entityName.get())
                fk.update(entityNameOld,entityNameNew)
            else:
                print("not updating entity Name", fk.entityName.get())
                fk.update()

def removeHangingForeignKeys(entityName='',attributeName = ''):
    global entities_list
    global global_schema
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
    def __init__(self,wrapperFrame,entityName, name, dataType,isPrimaryKey,row,col):
        global global_schema
        wrapperFrame = Frame(wrapperFrame, highlightthickness=2, highlightbackground='black')
        wrapperFrame.pack(fill='both', expand=True,padx=20, pady=20)

        # wrapperFrame.grid(row=row,column=col, sticky='news',padx=(10, 10),pady=(10,10))

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
        global global_schema
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
        global global_schema
        if sv.get() != self.nameStr:
            # print("Allah hallah")
            # print(self.entityName)
            global_schema[self.entityName]['attributes'][sv.get()] = self.dataType.get()
            global_schema[self.entityName]['attributes'].pop(self.nameStr)
            if self.nameStr in global_schema[self.entityName]['primaryKey']:
                global_schema[self.entityName]['primaryKey'].append(sv.get())
                global_schema[self.entityName]['primaryKey'].remove(self.nameStr)
            self.nameStr = sv.get()
            updataAllForeignKeys(self.entityName,self.entityName)
    
    def isPrimaryKeyCheckbox(self):
        global global_schema
        if self.isInitialized:
            if not self.isPrimaryKey.get(): global_schema[self.entityName]['primaryKey'].append(self.nameStr)
            else: global_schema[self.entityName]['primaryKey'].remove(self.nameStr)
            updataAllForeignKeys(self.entityName,self.entityName)

    def changeDataType(self,dataType):
        global global_schema
        global_schema[self.entityName]['attributes'][self.name.get()]=dataType

class foreignKey:
    def __init__(self,wrapperFrame,name,belongToEntity,attributes ,entityName, entityAtrribute, patricipaction):
        wrapperFrame = Frame(wrapperFrame, highlightthickness=2, highlightbackground='black')
        wrapperFrame.pack(fill='both', expand=True,padx=20, pady=20)
        global global_schema
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
        global global_schema
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
        global global_schema
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
        global global_schema
        if entityName is not None:
            self.entityName.set(entityName)
        entitiesList = list(global_schema.keys())
        self.entitiesMenu["menu"].delete(0, 'end')

        for choice in entitiesList:
            self.entitiesMenu["menu"]\
                .add_command(label=choice, command= lambda a=choice: \
                   [ self.entityName.set(a),self.updateAttributes(a) ])

    def updateAttrs(self,entityName= None):
        global global_schema
        print("Update Attrs",entityName,self.belongToEntity)
        if entityName is not None: self.belongToEntity = entityName
        print("Update Attrs",entityName,self.belongToEntity)
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
        global global_schema
        print("IN UPDATE",entityNameOld,entityNameNew,self.belongToEntity)
        self.updateEntities(entityNameNew)
        if self.belongToEntity == entityNameOld: 
            self.updateAttrs(entityNameNew)
        # else:
        #     self.updateAttrs()
        self.updateAttributes(entityNameNew)



class entity:
    def __init__(self, name, attributes, \
        primaryKeys, ForgeinKeys,entities_wrapper,value,row,col):
        global global_schema
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
                attributeName, dataType,attributeName in self.primaryKeys,row,col)
            
            # if col!=0 and col==5:
            #     row+=1
            # col= (col+1)%6


        # self.wrapper.pack(fill='both', expand=True,padx=20, pady=20)
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
        global global_schema
        attr_default_name = "attr" + str(len(self.attributes)+1)
        self.attributes[attr_default_name] =\
             attribute(self.attWrapper,self.name.get(),attr_default_name, "str",False,0,0)
        global_schema[self.name.get()]['attributes'][attr_default_name] = "str"
        expandCanvas()
        updataAllForeignKeys(self.entityCurName,self.entityCurName)

    def isWeakChecked(self):
        global global_schema
        if self.isInitialized:
            global_schema[self.name.get()]['isWeak'] = not self.isWeak.get()

    def editEntityName(self,sv):
        global global_schema
        if self.isInitialized:
            old_key = self.entityCurName
            new_key = sv.get()
            print("Edit entity Name",old_key,new_key)
            global_schema[old_key]['TableName'] = new_key
            global_schema[new_key] = global_schema.pop(old_key)#global_schema[old_key]
            updataAllForeignKeys(old_key,new_key)
            for attrKey in self.attributes.keys():
                if self.attributes[attrKey].entityName == old_key:
                    self.attributes[attrKey].entityName = new_key
            self.entityCurName = new_key
            ######################

    def addForeignKey(self):
        global global_schema
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
        global global_schema
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
class ValidationPage(Frame):

    def __init__(self, parent, controller):
        global global_schema
        Frame.__init__(self, parent)
        global screen_width,screen_height

##
        # self.geometry(f"{screen_width}x{screen_height}")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

##
        frame_main = Frame(self, bg="gray")
        frame_main.grid(padx=(185,0),sticky='news')
        frame_main.grid_propagate(0)

        screen_width = frame_main.winfo_screenwidth()
        screen_height = frame_main.winfo_screenheight()


##
        # Create a frame for the canvas with non-zero row&column weights
        global validation_frame
        validation_frame = Frame(frame_main)
        validation_frame.grid(row=0, column=0, sticky='nw')
        validation_frame.grid_rowconfigure(0, weight=1)
        validation_frame.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        validation_frame.grid_propagate(False)

        global canvas

##
        # Add a canvas in that frame
        canvas = Canvas(validation_frame, bg="yellow")
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        global vsb
        vsb = Scrollbar(validation_frame, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)
##

##

  
    @staticmethod
    def init_schema(initial_schema):
        
        old_keys = list(initial_schema.keys())
        for old_key in old_keys:
            new_key = initial_schema[old_key]['TableName']
            initial_schema[new_key] = initial_schema.pop(old_key)
        global global_schema
        global_schema = initial_schema

    
        
    @staticmethod
    def loadEntitiesFrames():
        global global_schema
        global validation_frame
        # Create a frame to contain the buttons
        global entities_wrapper
        entities_wrapper = Frame(canvas, bg="blue")
        canvas.create_window((185, 0), window=entities_wrapper, anchor='nw')

        global entities_list,row,col,ROWCOUNT

        entities_list = []
        row,col,ROWCOUNT=0,0,4
        print("global_schema",global_schema)

        for _, value in global_schema.items():
            entities_list.append(entity(value['TableName'],\
                value['attributes'], value['primaryKey'],\
                    value['ForgeinKey'],entities_wrapper,value,row,col))
            if col!=0 and col == ROWCOUNT-1:
                row +=1
            col = (col+1)%ROWCOUNT#+3)%12
        
        entities_wrapper.update_idletasks()


        global errors_wrapper
        errors_wrapper = Frame(validation_frame, highlightthickness=2, highlightbackground='black')
        errors_wrapper.grid(row=row,column=0, pady=(5, 0), sticky='nw')

        global errors_labels
        errors_labels=[]
        #add entity
        #add button
        button_wrapper = Frame(validation_frame, highlightthickness=2, highlightbackground='black')

        button_wrapper.grid(row=row,column=0, pady=(5, 0), sticky='nw')
        # row+=1

        addEntityButton = CTkButton(button_wrapper, \
                    text="Add new Entity",command=addEntity)
        

        addEntityButton.pack(fill='both', expand=True,padx=20, pady=20)
        #save object and add errors if needed
        #save button
        saveButton = CTkButton(button_wrapper, \
                    text="Save Changes",command=saveChanges)
        saveButton.pack(fill='both', expand=True,padx=20, pady=20)


        # put the frame in the canvas
        # make sure everything is displayed before configuring the scrollregion
        global vsb,screen_width,screen_height
        width = 1500 #screen_width - vsb.winfo_width() -255
        height = screen_height-70 
        validation_frame.config(width=width ,
                            height=height)

        # Set the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox("all"))
        