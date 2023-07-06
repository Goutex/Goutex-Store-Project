import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def adicionarJogo():

    nomejogo = input("Digite o nome do jogo: ")
    idgeneroj= input("Digite o ID do gênero do jogo: ")
    descricaojogo = input("Digite uma descricao para o jogo: ")
    sql = "INSERT INTO jogos (nomejogo, idgeneroj, descricaojogo) VALUES (%s, %s, %s)"
    valores = (nomejogo, idgeneroj, descricaojogo)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Jogo adicionado com sucesso!")

# adicionarJogo()
# cursor.close()
# conexao.close()

