from tkinter import *

app = Tk()
app.title("My New App")
app.geometry("500x500")
app.iconbitmap('Minion.ico')
app.resizable(False,False)

from tkinter import messagebox
label1 = Label(app, text="Cyber Security",font=('Arial Bold',50))
label1.grid(column=1 , row=0)

def clicked():
    messagebox.showinfo('Message title', 'Message content')
appbtn = Button(app,text='Click here', command=clicked)
appbtn.grid(column=1,row=1)

app.mainloop()
"""
res = messagebox.askquestion('Message title','Message content')
res = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')
"""
