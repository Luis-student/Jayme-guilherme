#conexão com banco 
import mysql.connector 

banco = mysql.connector.connect(
    host= "localhost",
    port= 3306,
    user= "root",
    password= "Jayme-123",
    database= "jayme_guilherme"

)

#criação do tabela 
cursor = banco.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS jayme_guilherme")

cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuario (id INT PRIMARY KEY, username VARCHAR(255), email VARCHAR(250), senha VARCHAR(100), idade INT)")


#inserrção de dados do usuario 

def cadastro():
    username = input("Username: ")
    email = input("Email: ")
    senha = input("Senha: ")
    idade = int(input("Idade: "))

    cursor.execute(f"INSERT INTO usuario (username, email, senha, idade) VALUES ('{username}', '{email}', '{senha}', {idade})")
    banco.commit()

    print("Usuário cadastrado com sucesso!")


cadastro()
