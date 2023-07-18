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
    while True:
        usuario = input("\nDigite o nome de usuário (ou 'S' para sair): ")

        if usuario.upper() == "S":
            print("\nTchau Tchau")
            break

        senha = input("Digite a senha: ")

        if usuario == "admin" and senha == "admin":
            admin.run()
            break
        else:
            cursor = conexao.cursor()
            sql = "SELECT * FROM cadastrouser WHERE usuario = %s AND senha = %s"
            values = (usuario, senha)

            cursor.execute(sql, values)
            resultado = cursor.fetchone()

            if resultado:
                print("\nLogin realizado com sucesso!")
                Loja.pesquisar_jogos()
                break
            else:
                print("\nUsuário ou senha inválidos. Tente novamente.")

# verificar_login()


