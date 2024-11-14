import mysql.connector
from config import MYSQL_CONFIG

conn = mysql.connector.connect(**MYSQL_CONFIG)
cursor = conn.cursor()

def create_mysql_entry(data):
    query = "INSERT INTO teachers (name, subject) VALUES (%s, %s)"
    values = (data["name"], data["subject"])
    cursor.execute(query, values)
    conn.commit()
    return cursor.lastrowid