
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
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

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
    

def start_creating_application(final_schema):
    src_dir = os.getcwd()
    os.chdir('Application')
    print("start creating application")
    Create_Application(final_schema)
    os.system("python3 run.py &")
    os.chdir('./..')
    front_path =  Path(src_dir) / Path('CreateFrontProject/CreateFrontProject.sh')
    print("start creating front project")
    os.system('chmod +rwx '+str(front_path))
    os.system(str(front_path))

    front_thread = threading.Thread(target=run_front,args=(src_dir,))
    front_thread.start()

    SqlQueriesPage.finish_creating_application()


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



    

class GeneratedSchemaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        ################### scroll bar not working ###################
        canvas = Canvas(self,bg = "#FFFFFF")
        canvas.pack(fill='both', expand=True,side='left')
        scroll_y = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_y.pack(fill=Y, side=RIGHT)
        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((300, 0), window=self, anchor="nw")
        ##############################################################
        
        screen_width = self.winfo_screenwidth()
        label = Label(self, text ="Generated Schema", style = 'W.TLabel', font=VERYLARGEFONT)
        label.place(x = screen_width/2, y = 90, anchor="center")

        self.finalSchema = tk.PhotoImage(file=relative_to_assets("./generatedSchema.png"))
        Label(self, image=self.finalSchema).place(x = 970, y = 950, anchor="center")

        canvas.update_idletasks()