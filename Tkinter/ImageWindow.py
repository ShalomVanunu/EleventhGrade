from tkinter import *
from PIL import Image, ImageTk

app = Tk()
app.title("My New App")
app.geometry("500x500")
app.iconbitmap('Minion.ico')
app.resizable(False,False)

from PIL import Image, ImageTk

label1 = Label(app, text="Cyber Security",font=('Arial Bold',50))
label1.grid(column=1 , row=0)
load = Image.open("cyber.jpg")
load =load.resize((250,250))
render = ImageTk.PhotoImage(load)
img = Label(app, image=render)
img.grid(column=1, row=3)

app.mainloop()

