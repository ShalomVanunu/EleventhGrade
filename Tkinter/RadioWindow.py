from tkinter import *

app = Tk()
app.title("My New App")
app.geometry("500x500")
app.iconbitmap('Minion.ico')
app.resizable(False,False)

from tkinter.ttk import *

selected = IntVar()
rad1 = Radiobutton(app,text='First', value=1, variable=selected)
rad2 = Radiobutton(app,text='Second', value=2, variable=selected)
rad3 = Radiobutton(app,text='Third', value=3, variable=selected)
def clicked():
    print(selected.get())
btn = Button(app, text="Click Me", command=clicked)
rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)
rad3.grid(column=2, row=3)
btn.grid(column=3, row=3)

app.mainloop()

