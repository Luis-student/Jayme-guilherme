import mysql.connector 

conexão = mysql.connector.connect(
    host= "localhost",
    port= 3306,
    user= "root",
    password= "Jayme-123"

)

cursor.execute("CREATE TABLE IF NOT EXISTS Jayme-Guilherme (id INT PRIMARY KEY, username VARCHAR(255), email VARCHAR(250), senha VARCHAR(100), idade INT)")

