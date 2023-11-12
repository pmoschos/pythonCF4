import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'coding2023',
    port = '3306'
)

cursor = conn.cursor()

cursor.execute("INSERT INTO teachers (id, firstname, lastname, age) VALUES (%s, %s, %s, %s)",
               (2, "Bob", "M.", 55))

conn.commit()
conn.close()