import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def adicionar_jogo():

    nomejogo = input("\nDigite o nome do jogo: ")
    idgeneroj= input("\nDigite o ID do gênero do jogo: ")
    descricaojogo = input("\nDigite uma descricao para o jogo: ")
    sql = "INSERT INTO jogos (nomejogo, idgeneroj, descricaojogo) VALUES (%s, %s, %s)"
    valores = (nomejogo, idgeneroj, descricaojogo)
    cursor.execute(sql, valores)
    conexao.commit()
    print("\nJogo adicionado com sucesso!")

# adicionarJogo()
# cursor.close()
# conexao.close()

