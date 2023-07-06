import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def atualizarJogo():

    idjogo = int(input("Digite o ID do jogo a ser atualizado: "))
    nomejogo = input("Digite o novo nome do jogo: ")
    descricaojogo = input("Digite a nova descricao do jogo: ")
    idgeneroj = int(input("Digite o novo ID do genero do jogo: " ))

    sql = f"UPDATE jogos SET nomejogo = '{nomejogo}', descricaojogo = '{descricaojogo}', idgeneroj = '{idgeneroj}' WHERE idjogo = {idjogo}"
    cursor.execute(sql)
    conexao.commit()
    print("Jogo atualizado com sucesso!")

# atualizarJogo()
# cursor.close()
# conexao.close()

