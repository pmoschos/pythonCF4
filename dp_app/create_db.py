import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root'
)

# Cursor
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE coding2023")