"""
SQLite
"""
import sqlite3 # import SQLite library

# SQL Create Table
create_table = """
CREATE TABLE IF NOT EXISTS class (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT, 
LastName TEXT,
email TEXT );
"""

# Insert new ROW with data
insert_data = """
INSERT INTO class (name,LastName,email) VALUES ("shalom","vanunu","shalomvanunu@mekifh.edum.org.il")

"""
name = "shalom"

insert_data1 = f"""
INSERT INTO class (name,LastName,email) VALUES ({name},"klainer","itayk@gmail.com")

"""

# function create DB file and create connection object
def connection_db(db_file):
    connection= 0
    try :
        connection = sqlite3.connect(db_file)
    except:
        print(" Error ")
    return connection

# run the SQL syntx on DB
def execute_query(connection,query):
    cursor = connection.cursor() # init DB
    try:
        cursor.execute(query)
        connection.commit()
    except:
        print("Error")


if __name__ == "__main__":
    con = connection_db("Class.db")
    print(type(con))
    execute_query(con,create_table)
    execute_query(con,insert_data)
    execute_query(con,insert_data1)