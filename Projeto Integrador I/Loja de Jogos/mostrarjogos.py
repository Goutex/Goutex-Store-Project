import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sen@c2021",#SUA SENHA
    database = "projetinho", #SEU DATABASE
)
cursor = conexao.cursor()

def mostrarJogos():
    cursor.execute("SELECT * FROM jogos")
    jogos = cursor.fetchall()
    print("Lista de Jogos:")
    for jogo in jogos:
        print(f"{jogo[0]}. {jogo[1]}")