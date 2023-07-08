import mysql.connector
from connector import host, user, password, database
from Admin import admin

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def verificar_login():
    cursor = conexao.cursor()

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "admin" and senha == "admin":
        admin.run()
    else:
        sql = "SELECT * FROM cadastrouser WHERE usuario = %s AND senha = %s"
        values = (usuario, senha)

        cursor.execute(sql, values)
        resultado = cursor.fetchone()

        if resultado:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha inválidos.")

    # cursor.close()

# verificarLogin()
