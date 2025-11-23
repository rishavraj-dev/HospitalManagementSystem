import mysql.connector
MYSQL_PASSWORD = "password123"
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="hospital_db"
    )
    return conn
