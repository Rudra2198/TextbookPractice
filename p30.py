import mysql.connector
db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Swami@232",
)

print(db_connection)
db_cursor = db_connection.cursor()
db_cursor.execute("create database HiveMind2")
db_cursor.execute("show databases")
for db in db_cursor:
    print(db)
