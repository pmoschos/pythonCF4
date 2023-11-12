import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'coding2023',
    port = '3306'
)

cursor = conn.cursor()

cursor.execute('BEGIN')

# Create tables
cursor.execute('''CREATE TABLE teachers
               (id INTEGER PRIMARY KEY,
               firstname VARCHAR(50),
               lastname VARCHAR(50),
               age INTEGER)''')

cursor.execute('''CREATE TABLE students
               (id INTEGER PRIMARY KEY,
               firstname VARCHAR(50),
               lastname VARCHAR(50))''')

conn.commit()
conn.close()