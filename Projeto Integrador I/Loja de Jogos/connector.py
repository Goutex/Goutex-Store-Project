import mysql.connector


def conectando():

    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",#SUA SENHA
        database = "projetinho", #SEU DATABASE
    )
    cursor = conexao.cursor()

conectando()