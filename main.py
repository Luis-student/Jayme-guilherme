import mysql.connector 

banco = mysql.connector.connect(
    host= "localhost",
    port= 3306,
    user= "root",
    password= "Jayme-123",
    database= "jayme_guilherme"

)

cursor = banco.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS jayme_guilherme")
