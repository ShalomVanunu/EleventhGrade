from tkinter import *

app = Tk()
app.title("My New App")
app.geometry("500x500")
app.iconbitmap('Minion.ico')
app.resizable(False,False)

from tkinter.ttk import *
label1 = Label(app, text="Cyber Security",font=('Arial Bold',50))
label1.grid(column=1 , row=0)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(app, text='Choose', var=chk_state)
chk.grid(column=1, row=2)
print(chk_state.get())

combo = Combobox(app)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=1, row=3)
choose = combo.get()
app.mainloop()

