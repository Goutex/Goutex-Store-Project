import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",#SUA SENHA
    database = "projetinho", #SEU DATABASE
)
cursor = conexao.cursor()
def adicionarGeneroj():

    nomegeneroj = input("Digite um nome para o Genero: ")
    descricaogeneroj = input("Digite uma descricao para o Genero: ")
    
    sql = f"INSERT INTO generosjogo (nomegeneroj, descricaogeneroj) VALUES ('{nomegeneroj}','{descricaogeneroj}')"
    cursor.execute(sql)
    conexao.commit()
    print("Genero de jogo adicionado com sucesso!")

# adicionarGeneroj()
# cursor.close()
# conexao.close()