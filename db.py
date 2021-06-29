import sqlite3
import os


def connect():

    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id Integer PRIMARY KEY, name TEXT, gender TEXT, year_level TEXT, course_code REAL)")
    conn.commit()
    conn.close()

def insert(name,gender,year_level,course_code):
    
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students Values (NULL,?,?,?,?)",(name,gender,year_level,course_code))
    conn.commit()
    conn.close()

def view():
    
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="",gender="",year_level="",course_code=""):
 
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("Select * FROM students WHERE name=? or gender=? or year_level=? or course_code=?",(name,gender,year_level,course_code))
    rows = cur.fetchall()
    conn.close()
    return(rows)

def delete(student_id):

    conn = sqlite3.connect("Students.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id=?",(student_id,))
    conn.commit()
    conn.close()

def update(student_id,name,gender,year_level,course_code):
    
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=?, gender=?, year_level=?, course_code=? WHERE student_id=?",(name,gender,year_level,course_code,student_id))
    conn.commit()
    conn.close()

def delete_data():
   
    if os.path.exists("Students.db"):
        os.remove("Students.db")
    connect()

connect()