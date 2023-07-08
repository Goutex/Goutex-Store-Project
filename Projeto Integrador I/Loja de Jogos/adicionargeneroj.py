import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def adicionar_generoj():

    nomegeneroj = input("Digite um nome para o Genero: ")
    descricaogeneroj = input("Digite uma descricao para o Genero: ")
    
    sql = f"INSERT INTO generosjogo (nomegeneroj, descricaogeneroj) VALUES ('{nomegeneroj}','{descricaogeneroj}')"
    cursor.execute(sql)
    conexao.commit()
    print("Genero de jogo adicionado com sucesso!")

# adicionarGeneroj()
# cursor.close()
# conexao.close()