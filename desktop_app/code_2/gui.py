
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
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

canvas.create_text(
    558.0,
    872.0,
    anchor="nw",
    text="Running Preprocessing ...",
    fill="#0F1136",
    font=("Inter", 40 * -1)
)

# image_image_1 = PhotoImage(
#     file=relative_to_assets("Loading.gif"), format="gif -index 2")

# frameCnt = 12
# frames = [PhotoImage(file='mygif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

# image_image_1 = PhotoImage(file=relative_to_assets("Loading.gif"))
# canvas.create_image(800.0,704.0,image=image_image_1)

frameCnt = 12
frames = [PhotoImage(file=relative_to_assets("Loading.gif"),format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    
    label.configure(image=frame)
    label.place(x=750.0,y=650.0)
    window.after(100, update, ind)
label = Label(window,bg='#FFFFFF')
label.pack()
window.after(0, update, 0)

# image_1 = canvas.create_image(
#     800.0,
#     704.0,
#     image=image_image_1
# )

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    799.0,
    305.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
