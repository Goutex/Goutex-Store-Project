import mysql.connector


def conectando():

    conexao = mysql.connector.connect(
        host = "localhost",
        user = "Sen@c2021",
        password = "Sen@c2021",#SUA SENHA
        database = "projetinho", #SEU DATABASE
    )
    cursor = conexao.cursor()

conectando()