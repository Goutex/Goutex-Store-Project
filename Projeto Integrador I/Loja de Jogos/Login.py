import mysql.connector
from connector import host, user, password, database
from Admin import admin
from Loja import Loja

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def verificar_login():
    cursor = conexao.cursor()

    usuario = input("\nDigite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "admin" and senha == "admin":
        admin.run()
    else:
        sql = "SELECT * FROM cadastrouser WHERE usuario = %s AND senha = %s"
        values = (usuario, senha)

        cursor.execute(sql, values)
        resultado = cursor.fetchone()

        if resultado:
            print("\nLogin realizado com sucesso!")
            Loja.pesquisar_jogos()
        else:
            print("Usuário ou senha inválidos.")

