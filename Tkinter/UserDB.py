
import sqlite3
from sqlite3 import Error

def create_connection():
    connection= None
    try:
        connection = sqlite3.connect('users.db')
        print("connection OK")

    except Error as e:
        print(f"the error {e} ")
    return  connection

def create_db():
    create_db ="CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, username TEXT, email TEXT, password TEXT)"
    execute_query(create_db)

def execute_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query execute")

    except Error as e:
        print(f"the error {e} ")


def insert(name, username,email,password):
    execute_query(f"INSERT INTO Users (name, username, email, password) VALUES ('{name}','{username}','{email}','{password}')")


def fetch():
    query = "SELECT * FROM Users"
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()
        print("query execute")
        return result

    except Error as e:
        print(f"the error {e} ")