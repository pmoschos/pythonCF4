import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'coding2023',
    port = '3306'
)

cursor = conn.cursor()

cursor.execute("SELECT id, firstname, lastname FROM teachers")

results = cursor.fetchall()

print(results)
print(type(results))
print()

for result in results:
    print(f"ID: {result[0]}, Firstname: {result[1]}, Lastname: {result[2]}")

cursor.close()
conn.close()