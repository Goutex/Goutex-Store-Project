import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",#SUA SENHA
    database = "projetinho", #SEU DATABASE
)
cursor = conexao.cursor()

def atualizarGeneroJ():

    idgeneroj = int(input("Digite o ID do jogo a ser atualizado: "))
    nomegeneroj = input("Digite o novo nome do jogo: ")
    descricaogeneroj = input("Digite a nova descricao do jogo: ")

    sql = f"UPDATE generosjogo SET nomegeneroj = '{nomegeneroj}', descricaogeneroj = '{descricaogeneroj}', WHERE idgeneroj = {idgeneroj}"
    cursor.execute(sql)
    conexao.commit()
    print("Genero atualizado com sucesso!")

# atualizarJogo()
# cursor.close()
# conexao.close()
