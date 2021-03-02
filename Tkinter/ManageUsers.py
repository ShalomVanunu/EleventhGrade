
from tkinter import *
from tkinter import messagebox # this deals with popup messagebox
import hashlib # encrypt the password with md5
import UserDB

def add_item(): # this funtion add the user
    if (name_text.get() == '' or username_text.get()=='' or emailname_text.get()=='' or passwordname_text.get()==''):
        messagebox.showerror('Error','Fill all the Fields')
        #username_entry.configure(bg='red') # color the entry by red
        return
    hash = hashlib.md5(passwordname_text.get().encode('utf'))
    password_hash = hash.hexdigest()
    UserDB.create_db()
    UserDB.insert(name_text.get(), username_text.get(),emailname_text.get(),password_hash)
    clear()

def clear():
    name_entry.delete(0, END)
    username_entry.delete(0,END)
    emailname_entry.delete(0, END)
    passwordname_entry.delete(0,END)
    name_entry.focus()

def fetch_data():
    user_list.delete(0,END)
    results = UserDB.fetch()
    for result in results:
        user_list.insert(END, result)

def clear_user_list():
    user_list.delete(0, END)


# Create windpw object tkinter
app = Tk()
app.title('Users Manager')
app.geometry('800x350')


# Lables of window

#Name of User
name_text =StringVar()
name_label =Label(app,text='Name of User',font=('bold',14))
name_label.grid(row=0, column=0, padx=5)
name_entry = Entry(app,textvariable=name_text)
name_entry.grid(row=0, column=1)
name_entry.focus()

#Username
username_text = StringVar()
username_label =Label(app,text='Username',font=('bold',14))
username_label.grid(row=0, column=2,padx=20)
username_entry = Entry(app,textvariable=username_text)
username_entry.grid(row=0, column=3)


#Email
emailname_text = StringVar()
emailname_label =Label(app,text='Email',font=('bold',14))
emailname_label.grid(row=1, column=0,padx=20)
emailname_entry = Entry(app,textvariable=emailname_text)
emailname_entry.grid(row=1, column=1)

#password
passwordname_text = StringVar()
passwordname_label =Label(app,text='Password',font=('bold',14))
passwordname_label.grid(row=1, column=2,padx=20)
passwordname_entry = Entry(app,show='*',textvariable=passwordname_text)
passwordname_entry.grid(row=1, column=3)


#Buttons

#Add user Button
add_btn= Button(app,text='Add User',command=add_item)
add_btn.grid(row=2, column=1,pady=20)

#Fetch Button
fetch_btn= Button(app,text='Fetch', command=fetch_data)
fetch_btn.grid(row=2, column=2,pady=20)

#Clear Button
clear_btn= Button(app,text='Clear', command=clear_user_list)
clear_btn.grid(row=2, column=3,pady=20)

#ListBox
user_list = Listbox(app, height=8 , width=100, border=3)
user_list.grid(row=4, column=0,  columnspan=4)

app.mainloop()


