import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "180957",#SUA SENHA
    database = "projeto1", #SEU DATABASE
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
