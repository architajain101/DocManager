import sqlite3 #used to create & use database
import os
DB_PATH = os.path.join("data","documents.db") #  Database file will be stored at: DB_PATH 

def get_connection():   #Open connection to database file
    return sqlite3.connect(DB_PATH)

def init():  #Initialize database (create table)
    conn = get_connection()  #connection to DB
    cursor = conn.cursor() #used to run SQL queries

   # document table schema
    cursor.execute("""
            CREATE TABLE IF NOT EXIST documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                path TEXT,
                thumbnail_path TEXT,
                tags TEXT,
                description TEXT,
                upload_date TEXT,
                lecture_date TEXT,
                total_pages INTEGER 
            )
    """)
    conn.commit()
    print("DB operation successfull")
    conn.close()

    
    
    
    
