import tkinter as tk
from tkinter import ttk, Tk, Canvas, Entry, Text, Button, PhotoImage,Label,Scrollbar
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from pathlib import Path
from turtle import bgcolor
import webbrowser
import cv2

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
LARGEFONT =("Verdana", 20)
VERYLARGEFONT =("Verdana", 40)
LASTPAGE = False
NEXTPAGEBUTTON = False
ERimage = None

############################## mimic to the processing time ###############################
def wait(self, screen_width):
    showDone(self, screen_width)  
###########################################################################################

def resizeUploadedImage(imagePath):
    img = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(img, (550,260), interpolation = cv2.INTER_AREA)
    cv2.imwrite('./assets/uploadedImage.png',resized)

def open_file(self,screen_width,button):
    ERimage = filedialog.askopenfile(mode='r', filetypes=[('Image Files',['*png','*jpeg'])])
    if ERimage is not None:
        resizeUploadedImage(ERimage.name)
        self.ER_image = tk.PhotoImage(file=relative_to_assets("./uploadedImage.png"))
        Label(self, image=self.ER_image).place(x = screen_width/2, y = 755,width=550,height=260, anchor="center")
        button['state'] = "normal"

def update(self,ind,frameCnt, frames, label):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    
    label.configure(image=frame)
    label.place(x=850.0,y=200.0)
    self.after(40, update, self,ind,frameCnt, frames, label)

def showDone(self,screen_width):
    self.ER_image = tk.PhotoImage(file=relative_to_assets("./done.png"))
    Label(self, image=self.ER_image, background="#FFFFFF").place(x = 980, y = 300,width=300,height=300, anchor="center")
    label = ttk.Label(self, text ="", style = 'W.TLabel',background="#FFFFFF")
    label.place(x = screen_width/2, y = 550, width=500, anchor="center")
    label = ttk.Label(self, text ="Done Successfully!", style = 'W.TLabel', foreground="#338855")
    label.place(x = screen_width/2, y = 550, anchor="center")

def open_back_url():
    webbrowser.open_new("https://www.google.com/")

def open_front_url():
    webbrowser.open_new("http://localhost:8080/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def enableSideButtons():
    global LASTPAGE
    LASTPAGE = True

def reachedLastPage(page):
    if LASTPAGE == True and page == "front":
        open_front_url()
    elif LASTPAGE == True and page == "api":
        open_back_url()

def moveToPage(self,page):
    if LASTPAGE == True:
        self.show_frame(page)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.configure(bg = "#FFFFFF")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.maxsize(1950, 1024)
        self.minsize(1750, 1024)
        self.resizable(width=True, height=False)
        self.frames = {} 
        for F in (StartPage, Page1, Page2, Page3):
  
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
            frame.configure(bg = "white")
            canvas = Canvas(
                frame,
                bg = "#FFFFFF",
                height = 1024,
                width = 180,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            canvas.place(x = 0, y = 0)
            canvas.create_rectangle(
                0.0,
                0.0,
                181.0,
                1024.0,
                fill="#0F1136",
                outline="")
            self.home = tk.PhotoImage(file=relative_to_assets("home.png"))
            homeButton = ttk.Button(self, image =self.home,style='W.TButton', command = lambda: self.show_frame(StartPage))
            homeButton.place(x = 22, y = 50)

            self.sql = tk.PhotoImage(file=relative_to_assets("sql.png"))
            sqlButton = ttk.Button(self, image =self.sql,style='W.TButton', command = lambda: moveToPage(self, Page2))
            sqlButton.place(x = 22, y = 240)

            self.api = tk.PhotoImage(file=relative_to_assets("api.png"))
            apiButton = ttk.Button(self, image =self.api,style='W.TButton', command = lambda: reachedLastPage("api"))
            apiButton.place(x = 22, y = 440)

            self.front = tk.PhotoImage(file=relative_to_assets("frontDemo.png"))
            frontButton = ttk.Button(self, image =self.front,style='W.TButton', command = lambda: reachedLastPage("front"))
            frontButton.place(x = 22, y = 640)

            self.schema = tk.PhotoImage(file=relative_to_assets("schema.png"))
            schemaButton = ttk.Button(self, image =self.schema,style='W.TButton', command = lambda: moveToPage(self, Page3))
            schemaButton.place(x = 22, y = 840)
            
        self.show_frame(StartPage)
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ## add logo image
        self.viewWindow = Canvas(self, bg="white")
        self.viewWindow.pack(side="top", fill="both", expand=True)
        self.logo_image = tk.PhotoImage(file=relative_to_assets("image_1.png"))
        self.viewWindow.image = self.logo_image
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.viewWindow.create_image(screen_width/2, 300, anchor="center", image=self.logo_image, tags="bg_img")
        
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('W.TLabel', background = 'white', foreground = '#0F1136',font= LARGEFONT)
        label = ttk.Label(self, text ="Welcome To ERevive", style = 'W.TLabel')
        label.place(x = screen_width/2, y = 600, anchor="center")

        ## add camera image
        style.theme_use('alt')
        style.configure('W1.TButton', background = '#FFFFFF', width = 0, borderwidth=0, focusthickness=0, focuscolor='none')
        self.upload_image = tk.PhotoImage(file=relative_to_assets("upload_4.png"))
        upload_image_button = ttk.Button(self, image =self.upload_image,style='W1.TButton',command = lambda : open_file(self,screen_width,button1))
        upload_image_button.place(x = screen_width/2, y = 760,height=250, anchor="center")
       
        ## creating button to navigate to next page
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('W.TButton', background = '#0F1136', foreground = 'white', width = 0, borderwidth=0, focusthickness=0, focuscolor='none',font= LARGEFONT)
        style.map('W.TButton', background=[('active','#222222')])
        style.map('W.TButton', background=[('disabled','#222222')])
        style.map('W.TButton', foreground=[('disabled','#FFFFFF')])

        upload_button = ttk.Button(self, text ="Upload Image",style='W.TButton',
        command = lambda : [open_file(self,screen_width,button1)])
        upload_button.place(x = screen_width/2-210, y = screen_height-140, width = 350.0, height = 70.0, anchor = "center")

        button1 = ttk.Button(self, text ="Move To Next Step ...",style = "W.TButton",
        command = lambda : controller.show_frame(Page1), state = "disabled")
        button1.place(x = screen_width/2+210, y = screen_height-140, width = 350.0, height = 70.0, anchor = "center")

# second window frame page1
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        label = ttk.Label(self, text ="Performing Preprocessing ....", style = 'W.TLabel',font=VERYLARGEFONT)
        label.place(x = screen_width/2, y = 100, anchor="center")

        ### gif of loading
        frameCnt = 45
        frames = [PhotoImage(file=relative_to_assets("Loading.gif"),format = 'gif -index %i' %(i)) for i in range(frameCnt)]
        label = ttk.Label(self,background='#FFFFFF')
        label.place(x = 850, y = 200, anchor = "center")
        label.pack()
        self.after(0, update, self,0,frameCnt, frames, label)

        ### finish preprocessing
        # wait(self,screen_width)

        self.uploadedER = tk.PhotoImage(file=relative_to_assets("./uploadedImage.png"))
        Label(self, image=self.uploadedER).place(x = screen_width/2, y = 755,width=550,height=260, anchor="center")

        ## button for next step
        button1 = ttk.Button(self, text ="Move To Next Step ...",style='W.TButton',
        command = lambda : [controller.show_frame(Page2), enableSideButtons()])
        button1.place(x = screen_width/2, y = screen_height-140, width = 350.0, height = 70.0, anchor = "center")

# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        screen_width = self.winfo_screenwidth()
        label = ttk.Label(self, text ="SQL Queries Page ....", style = 'W.TLabel',font=VERYLARGEFONT)
        label.place(x = screen_width/2, y = 90, anchor="center")

class Page3(tk.Frame):
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

app = tkinterApp()
app.mainloop()
