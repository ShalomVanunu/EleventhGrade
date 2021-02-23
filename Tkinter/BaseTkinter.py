
from tkinter import *

app = Tk()

app.title("My New App")
app.geometry("500x500")
app.iconbitmap("heart.ico")
app.resizable()

label1 = Label(app, text="Cyber Security", font=("Arial",40))
label1.grid(column=1, row=1)
label2 = Label(app, text="Covid19", bg='black',fg='yellow')
label2.grid(column=1, row=3)
label3 = Label(app,font=("Arial",20))
label3.grid(column=1,row=9)

entry_text= StringVar()
entry1 = Entry(app, width =15, textvariable=entry_text)
entry1.grid(column=1,row=2)
entry1.focus() # bring the cursor to this point

def clickme():
    label3.configure(text =entry_text.get())

def textclick():
    text.insert(1.0,entry_text.get())

btn1 = Button(app, text="Click Me!", command=clickme)
btn1.grid(column=0,row=4)
btn2 = Button(app, text="Send to Text Obj",command=textclick)
btn2.grid(column=0,row=5)

text = Text(app,width="20", height="10")
text.grid(column=1,row=10)

app.mainloop()