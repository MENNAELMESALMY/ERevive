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

class entity:
    def __init__(self, name, attributes, \
        primaryKey, ForgeinKey, isWeak,row):
        self.attributes = attributes
        self.primaryKey = primaryKey
        self.ForgeinKey = ForgeinKey
        # Entity Name
        self.name = StringVar(frame)
        self.entityName = Entry(frame,\
             textvariable=self.name, width=20, font="Calibri, 12")
        self.entityName.grid(row=row+1, column=1)
        # self.entityName.pack(padx=20, pady=20)
        self.name.set(name)
        # Is Weak
        self.isWeak = Variable()
        self.c = Checkbutton(frame, text = "isWeak", variable=self.isWeak)
        self.c.grid(row=row+1, column=3)
        self.isWeak.set(int(value['isWeak']))
        if isWeak: self.c.select()
        # self.c.pack(padx=20, pady=20)
        # Attributes

from tkinter import Tk,Frame, Canvas, Entry, Variable, Button,Label,Scrollbar,StringVar,IntVar,Checkbutton
from tkinter import RIGHT,Y

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg = "#FFFFFF")
# canvas = Canvas(root)
scroll_y = Scrollbar(root, orient="vertical", command=Y)

frame = Frame(root)
frame.configure(bg = "#FFFFFF")

entities_list = []
i = 0
# group of widgets
for _, value in test_schema.items():
    entities_list.append(entity(value['TableName'],\
         value['attributes'], value['primaryKey'],\
              value['ForgeinKey'], value['isWeak'],i))
    i += 1

# put the frame in the canvas
# canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
# canvas.update_idletasks()

# canvas.configure(scrollregion=canvas.bbox('all'), 
#                  yscrollcommand=scroll_y.set)
                 
# canvas.pack(fill='both', expand=True, side='left')
# scroll_y.pack(fill='y', side='right')
frame.pack(fill='both', expand=True, side='left')
root.mainloop()
