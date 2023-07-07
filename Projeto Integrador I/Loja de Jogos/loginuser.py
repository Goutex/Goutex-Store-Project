import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        login VARCHAR(50) NOT NULL,
        senha VARCHAR(50) NOT NULL
    )
""")

conexao.commit()

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

cursor.execute("""
    SELECT * FROM usuarios
    WHERE login = %s AND senha = %s
""", (login, senha))

resultado = cursor.fetchone()

if resultado:
    print("Login concluido. ")
else:
    print("Login ou senha incorretos.")