
import os
import pickle
from time import sleep
import tkinter as tk
from tkinter import ttk, Tk, Canvas, Entry, Text, Button, PhotoImage,Label,Scrollbar
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from pathlib import Path

from SearchEngine import suggest_queries

LARGEFONT =("Verdana", 20)
VERYLARGEFONT =("Verdana", 40)
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
    print("start search engine")
    print(os.getcwd())
    with open('./TestSchemas/sportsSchema.pickle','rb') as file:
        testSchema = pickle.load(file)
    os.chdir('SearchEngine')
    suggest_queries(testSchema)
    os.chdir('./..')
    SqlQueriesPage.finish()

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
    def finish():
        #change queries_label to suggest queries
        SqlQueriesPage.queries_label.configure(text = "Creating Application ....")
        SqlQueriesPage.queries_label.place(x = SqlQueriesPage.width/2, y = 100, anchor="center")




    

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