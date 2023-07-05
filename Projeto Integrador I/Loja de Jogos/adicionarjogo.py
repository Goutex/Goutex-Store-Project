import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "180957",#SUA SENHA
    database = "projeto1", #SEU DATABASE
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

