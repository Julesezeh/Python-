#import sqlite3
import sqlite3

#establish a connection to the database 
conn = sqlite3.connect("students.db")

#create a cursor to perform actions 
cur = conn.cursor()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

'''
#CREATING A TABLE
cur.execute("""CREATE TABLE students (
            name TEXT,
            age INTEGER,
            height REAL
    )""")
'''

#cur.execute("INSERT INTO students VALUES  ('Marty',42,1.8)")

all_students = [
	('John',24,1.78),
	("Lupita",21,2.01),
	("Kevin",18,2.05),
]
#cur.executemany("INSERT INTO students VALUES (?,?,?)",all_students)

cur.execute("SELECT * FROM students ")
print(cur.fetchall())

#To commit 
#conn.commit()

#To close the connection
conn.close()    