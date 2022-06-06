from tkinter import Tk,Frame, Canvas, OptionMenu, Variable, Button,Label,Scrollbar,StringVar,IntVar,Checkbutton
from tkinter import RIGHT,Y,BOTTOM,LEFT,X,TOP,W,E,N,S
from customtkinter import CTkEntry,CTkFrame,CTkCheckBox,CTkComboBox,CTkLabel,CTkButton

test_schema = {
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
    'isWeak': False}}

dataTypes = ['str', 'int', 'float', 'datetime','bool']

class attribute:
    def __init__(self,wrapperFrame, name, dataType,isPrimaryKey):
        self.removed = False
        self.name = StringVar(wrapperFrame)
        self.name.set(name)

        self.dataType = StringVar(wrapperFrame)
        self.dataType.set(dataType)
        self.attrName = CTkEntry(wrapperFrame,\
             textvariable=self.name, width=120)
        # self.attrName.grid(row=row)
        self.attrName.pack(fill='both', expand=True,padx=20, pady=20)

        
        self.dataTypeMenu = OptionMenu(wrapperFrame,self.dataType,*dataTypes)
        self.dataTypeMenu.pack(fill='both', expand=True,padx=20, pady=20)


        # self.dataTypeMenu.grid(row=row+1)
        #self.isPrimaryKey = isPrimaryKey
        self.isPrimaryKey = Variable()
        self.isPrimaryCheckbox = CTkCheckBox(wrapperFrame, text = "isPrimaryKey", \
            variable=self.isPrimaryKey)
        self.isPrimaryCheckbox.pack(fill='both', expand=True,padx=20, pady=20)
        # self.c.grid(row=row+1, column=3)
        self.isPrimaryKey.set(isPrimaryKey)
        if isPrimaryKey: self.isPrimaryCheckbox.select()
        #self.isForeignKey = isForeignKey

        self.removeAttrButton = CTkButton(wrapperFrame, \
            text="Remove Attribute",command=self.removeAttribute)

        self.removeAttrButton.pack(fill='both', expand=True,padx=20, pady=20)
    def removeAttribute(self):
        self.attrName.destroy()
        self.isPrimaryCheckbox.destroy()
        self.dataTypeMenu.destroy()
        self.removeAttrButton.destroy()
        self.removed = True

class entity:
    def __init__(self, name, attributes, \
        primaryKeys, ForgeinKey, isWeak):
        self.wrapper = Frame(validation_frame, highlightthickness=2, highlightbackground='black')
        # self.wrapper.grid(row=row)
        self.attributes = []
        self.primaryKeys = set(primaryKeys)
        self.ForgeinKey = ForgeinKey
        # Entity Name
        self.name = StringVar(self.wrapper)
        self.name.set(name)
        self.entityName = CTkEntry(self.wrapper,\
             textvariable=self.name, width=120)
        self.entityName.pack(fill='both', expand=True,padx=20, pady=20)

        # self.entityName.grid(row=row+1, column=1)
        # self.entityName.pack(padx=20, pady=20)
        # Is Weak
        self.isWeak = Variable()
        self.c = CTkCheckBox(self.wrapper, text = "isWeak", variable=self.isWeak)
        # self.c.grid(row=row+1, column=3)
        self.isWeak.set(int(value['isWeak']))
        if isWeak: self.c.select()
        self.wrapper.pack(fill='both', expand=True,padx=20, pady=20)
        self.c.pack(fill='both', expand=True,padx=20, pady=20)
        # Attributes
        for attributeName,dataType in attributes.items():
            # print(attributeName,dataType)
            self.attributes.append(attribute(self.wrapper,\
                attributeName, dataType,attributeName in self.primaryKeys))

        self.newAttrButton = CTkButton(self.wrapper, \
            text="Add Attribute",command=self.addAttribute)

        self.newAttrButton.pack(fill='both', expand=True,padx=20, pady=20)

    
    def addAttribute(self):
        self.attributes.append(attribute(self.wrapper,"", "",False))
    
    def removeAttribute(self):
        self.attributes.pop()

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg = "#FFFFFF")
# create main frame 
frame = CTkFrame(root)
frame.pack(fill='both', expand=True)
frame.configure(bg = "#FFFFFF")

# create canvas
canvas = Canvas(frame)
canvas.pack(fill='both', expand=True,side='left')

scroll_y = Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll_y.pack(fill=Y, side=RIGHT)
canvas.configure(yscrollcommand=scroll_y.set)
canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
validation_frame = Frame(canvas)
canvas.create_window((0, 0), window=validation_frame, anchor="nw")

entities_list = []
# group of widgets
for _, value in test_schema.items():
    entities_list.append(entity(value['TableName'],\
         value['attributes'], value['primaryKey'],\
              value['ForgeinKey'], value['isWeak']))

# put the frame in the canvas
# canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()


                 
# scroll_y.config(command=frame.yview)
root.mainloop()
