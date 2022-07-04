
import os
import pickle
import threading
from time import sleep
import tkinter as tk
from tkinter import ttk, Tk, Canvas, Entry, Text, Button, PhotoImage,Label,Scrollbar
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from pathlib import Path

from SearchEngine import suggest_queries
from Application import Create_Application
LARGEFONT =("Verdana", 20)
VERYLARGEFONT =("Verdana", 40)
OUTPUT_PATH = Path(__file__).parent
LASTPAGE = False
canvas = None
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
database_info = {
    'username' : "",
    "password" : "",
}

def enableSideButtons():
    global LASTPAGE
    LASTPAGE = True

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def showDone(self,screen_width):
    self.ER_image = tk.PhotoImage(file=relative_to_assets("./done.png"))
    Label(self, image=self.ER_image, background="#FFFFFF").place(x = 980, y = 300,width=300,height=300, anchor="center")
    label = ttk.Label(self, text ="", style = 'W.TLabel',background="#FFFFFF")
    label.place(x = screen_width/2, y = 550, width=500, anchor="center")
    label = ttk.Label(self, text ="Done Successfully!", style = 'W.TLabel', foreground="#338855")
    label.place(x = screen_width/2, y = 550, anchor="center")

def update(self,ind,frameCnt, frames, label):
    try:
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        
        label.configure(image=frame)
        label.place(x=850.0,y=200.0)
        self.after(40, update, self,ind,frameCnt, frames, label)
    except Exception as e:
        pass

def start_search_engine(final_schema):
    #final_schema = {'DEPARTMENT': {'TableName': 'DEPARTMENT', 'attributes': {'name': 'str', 'start_date': 'datetime', 'EMPLOYEE_Manages_ssn': 'int'}, 'primaryKey': ['name'], 'ForgeinKey': [{'attributeName': 'EMPLOYEE_Manages_ssn', 'ForignKeyTable': 'EMPLOYEE', 'ForignKeyTableAttributeName': 'ssn', 'patricipaction': 'partial', 'dataType': 'int'}], 'isWeak': False}, 'EMPLOYEE': {'TableName': 'EMPLOYEE', 'attributes': {'last_name': 'str', 'salary': 'float', 'sex': 'str', 'status': 'str', 'DEPARTMENT_Employed_name': 'str', 'middle_name': 'str', 'first_name': 'str', 'address': 'str', 'birth_date': 'datetime', 'ssn': 'int', 'start_date': 'datetime', 'EMPLOYEE_Supervision_ssn': 'int'}, 'primaryKey': ['ssn'], 'ForgeinKey': [{'attributeName': 'DEPARTMENT_Employed_name', 'ForignKeyTable': 'DEPARTMENT', 'ForignKeyTableAttributeName': 'name', 'patricipaction': 'full', 'dataType': 'str'}, {'attributeName': 'EMPLOYEE_Supervision_ssn', 'ForignKeyTable': 'EMPLOYEE', 'ForignKeyTableAttributeName': 'ssn', 'patricipaction': 'partial', 'dataType': 'int'}], 'isWeak': False}, 'PROJECT': {'TableName': 'PROJECT', 'attributes': {'location': 'str', 'budget': 'float', 'DEPARTMENT_Assigned_name': 'str', 'name': 'str'}, 'primaryKey': ['name'], 'ForgeinKey': [{'attributeName': 'DEPARTMENT_Assigned_name', 'ForignKeyTable': 'DEPARTMENT', 'ForignKeyTableAttributeName': 'name', 'patricipaction': 'partial', 'dataType': 'str'}], 'isWeak': False}, 'DEPENDENT': {'TableName': 'DEPENDENT', 'attributes': {'relatlonship': 'str', 'name': 'str', 'birth_date': 'datetime', 'sex': 'str', 'Dependents_EMPLOYEE_ssn': 'int'}, 'primaryKey': ['Dependents_EMPLOYEE_ssn'], 'ForgeinKey': [{'attributeName': 'Dependents_EMPLOYEE_ssn', 'ForignKeyTable': 'EMPLOYEE', 'ForignKeyTableAttributeName': 'ssn', 'patricipaction': 'partial', 'dataType': 'int'}], 'isWeak': True}, 'Works_EMPLOYEE_PROJECT': {'TableName': 'Works_EMPLOYEE_PROJECT', 'attributes': {'start_date': 'datetime', 'hours': 'int', 'EMPLOYEE_ssn': 'int', 'PROJECT_name': 'str'}, 'primaryKey': ['EMPLOYEE_ssn', 'PROJECT_name'], 'ForgeinKey': [{'attributeName': 'EMPLOYEE_ssn', 'ForignKeyTable': 'EMPLOYEE', 'ForignKeyTableAttributeName': 'ssn', 'patricipaction': 'full', 'dataType': 'int'}, {'attributeName': 'PROJECT_name', 'ForignKeyTable': 'PROJECT', 'ForignKeyTableAttributeName': 'name', 'patricipaction': 'full', 'dataType': 'str'}], 'isWeak': False}, 'DEPARTMENT_location': {'TableName': 'DEPARTMENT_location', 'attributes': {'DEPARTMENT_name': 'str', 'Clocation': 'str', 'location': 'str'}, 'primaryKey': ['DEPARTMENT_name', 'Clocation'], 'ForgeinKey': [{'attributeName': 'DEPARTMENT_name', 'ForignKeyTable': 'DEPARTMENT', 'ForignKeyTableAttributeName': 'name', 'patricipaction': 'full', 'dataType': 'str'}], 'isWeak': False}}
    print("start search engine")
    print(os.getcwd())
    os.chdir('SearchEngine')
    suggest_queries(final_schema.copy())
    os.chdir('./..')
    SqlQueriesPage.finish_search_engine()
    start_creating_application(final_schema.copy())



def run_front(src_dir):
    front_path =  Path(src_dir) / Path('CreateFrontProject/FrontCode')
    os.chdir(str(front_path))
    os.system('npm run serve')
    
#App.database_info["username"],App.database_info["password"],App.database_info["database"]
def start_creating_application(final_schema):
    src_dir = os.getcwd()
    os.chdir('Application')
    print("start creating application")
    Create_Application(final_schema,database_info["username"],database_info["password"])
    os.system("python3 run.py &")
    os.chdir('./..')
    front_path =  Path(src_dir) / Path('CreateFrontProject/CreateFrontProject.sh')
    print("start creating front project")
    os.system('chmod +rwx '+str(front_path))
    os.system(str(front_path))

    front_thread = threading.Thread(target=run_front,args=(src_dir,))
    front_thread.start()

    SqlQueriesPage.finish_creating_application()

def checkIfAllDatabaseInfoTaken ():
    if database_info['username'] != "" and database_info['password'] != "":
        Page3.finish() 

def getDatabaseUsername(entry):
    username = entry.get()
    global database_info
    database_info['username'] = username
    checkIfAllDatabaseInfoTaken()

def getDatabasePassword(entry):
    password = entry.get()
    global database_info
    database_info['password'] = password
    checkIfAllDatabaseInfoTaken() 

class Page3(tk.Frame):
    frame_controller = None
    width = 0
    height = 0
    frame = None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        label = ttk.Label(self, text ="Let us know your database information?", style = 'W.TLabel',font=VERYLARGEFONT)
        label.place(x = screen_width/2, y = 100, anchor="center")

        style = ttk.Style()
        style.configure('TEntry', foreground = '#0f1136')
        input_text1 = StringVar()
        entry1 = ttk.Entry(self,width=90,textvariable = input_text1, justify = CENTER,font = ('courier', 18, 'bold'))
        entry1.focus_force()
        entry1.place(x = screen_width/2, y = 250,height=50, anchor="center")

        button1 = ttk.Button(self, text ="Add Database UserName",style='W.TButton',
        command = lambda : [getDatabaseUsername(entry1)])
        button1.place(x = screen_width/2, y = 350, width = 350.0, height = 70.0, anchor = "center")

        input_text2 = StringVar()
        entry2 = ttk.Entry(self,width=90,textvariable = input_text2, justify = CENTER,font = ('courier', 18, 'bold'))
        entry2.focus_force()
        entry2.place(x = screen_width/2, y = 450,height=50, anchor="center")

        button2 = ttk.Button(self, text ="Add Database Password",style='W.TButton',
        command = lambda : [getDatabasePassword(entry2)])
        button2.place(x = screen_width/2, y = 550, width = 350.0, height = 70.0, anchor = "center")

        Page3.frame = self
        Page3.frame_controller = controller
        Page3.width = screen_width
        Page3.height = screen_height
    @staticmethod    
    def finish():
        button4 = ttk.Button(Page3.frame, text ="Move To Next Step ...",style='W.TButton',
        command = lambda : [print(database_info),Page3.frame_controller.showSqlPage()])
        button4.place(x = Page3.width/2, y = Page3.height-140, width = 350.0, height = 70.0, anchor = "center")


class SqlQueriesPage(tk.Frame):
    frame_controller = None
    width = 0
    height = 0
    gif_label = None
    frame = None
    queries_label = None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        queries_label = ttk.Label(self, text ="Suggesting Queries ....", style = 'W.TLabel',font=VERYLARGEFONT)
        queries_label.place(x = screen_width/2, y = 100, anchor="center")
        SqlQueriesPage.queries_label = queries_label
        ### gif of loading
        frameCnt = 45
        frames = [PhotoImage(file=relative_to_assets("Loading.gif"),format = 'gif -index %i' %(i)) for i in range(frameCnt)]
        label = ttk.Label(self,background='#FFFFFF')
        label.place(x = 850, y = 200, anchor = "center")
        label.pack()
        self.after(0, update, self,0,frameCnt, frames, label)
        SqlQueriesPage.frame_controller = controller
        SqlQueriesPage.width = screen_width
        SqlQueriesPage.height = screen_height
        SqlQueriesPage.gif_label = label
        SqlQueriesPage.frame = self
       
    @staticmethod    
    def finish_search_engine():
        #change queries_label to suggest queries
        SqlQueriesPage.queries_label.configure(text = "Creating Application ....")
        SqlQueriesPage.queries_label.place(x = SqlQueriesPage.width/2, y = 100, anchor="center")
    
    @staticmethod
    def finish_creating_application():
        SqlQueriesPage.gif_label.destroy()
        SqlQueriesPage.queries_label.configure(text = "Good To Go!")
        SqlQueriesPage.queries_label.place(x = SqlQueriesPage.width/2, y = 100, anchor="center")
        showDone(SqlQueriesPage.frame,SqlQueriesPage.width)
        enableSideButtons()



class GeneratedSchemaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        ################### scroll bar not working ###################
        # canvas = Canvas(self,bg = "#FFFFFF")
        # canvas.pack(fill='both', expand=True,side='left')
        # scroll_y = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        # scroll_y.pack(fill=Y, side=RIGHT)
        # canvas.configure(yscrollcommand=scroll_y.set)
        # canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        # canvas.create_window((300, 0), window=self, anchor="nw")
        ##############################################################

##      
        # self.geometry(f"{screen_width}x{screen_height}")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

##
        frame_main = Frame(self)
        frame_main.grid(padx=(185,0),sticky='news')
        frame_main.grid_propagate(0)

        screen_width = frame_main.winfo_screenwidth()
##
        # Create a frame for the canvas with non-zero row&column weights
        sql_frame = Frame(frame_main)
        sql_frame.grid(row=0, column=0, sticky='nw')
        sql_frame.grid_rowconfigure(0, weight=1)
        sql_frame.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        sql_frame.grid_propagate(False)
        global canvas
        # Add a canvas in that frame
        canvas = Canvas(sql_frame, bg="yellow")
        canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        global vsb
        vsb = Scrollbar(sql_frame, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)
        ##############################################################
        
        screen_width = self.winfo_screenwidth()
        label = Label(self, text ="Generated Schema", style = 'W.TLabel', font=VERYLARGEFONT)
        label.place(x = screen_width/2, y = 90, anchor="center")

        self.finalSchema = tk.PhotoImage(file=relative_to_assets("./generatedSchema.png"))
        Label(self, image=self.finalSchema).place(x = 970, y = 950, anchor="center")

        canvas.update_idletasks()

class GeneratedQueries(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        