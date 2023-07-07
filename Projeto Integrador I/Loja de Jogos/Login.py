import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def verificarLogin():
    cursor = conexao.cursor()

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    sql = "SELECT * FROM cadastrouser WHERE usuario = %s AND senha = %s"
    values = (usuario, senha)

    cursor.execute(sql, values)
    resultado = cursor.fetchone()

    if resultado:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha inválidos.")

    cursor.close()

# Exemplo de uso
# verificarLogin()
