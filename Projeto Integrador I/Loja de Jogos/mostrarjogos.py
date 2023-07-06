import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def mostrarJogos():
    cursor.execute("SELECT * FROM jogos")
    jogos = cursor.fetchall()
    print("Lista de Jogos:")
    for jogo in jogos:
        print(f"{jogo[0]}. {jogo[1]}")