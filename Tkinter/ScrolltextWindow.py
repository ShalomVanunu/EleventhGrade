from tkinter import *

app = Tk()
app.title("My New App")
app.geometry("500x500")
app.iconbitmap('Minion.ico')
app.resizable(False,False)

from tkinter import scrolledtext
label1 = Label(app, text="Cyber Security",font=('Arial Bold',50))
label1.grid(column=1 , row=0)
Entry = Entry(app, width=10)
Entry.focus()
Entry.grid(column=1 , row=4)
def clicked():
    scrolltxt.insert(END,Entry.get())
Btn = Button(app, text="Covid 19",command=clicked)
Btn.grid(column=1 , row=3)

scrolltxt = scrolledtext.ScrolledText(app,width=40,height=10)
scrolltxt.grid(column=1,row=6)
app.mainloop()

