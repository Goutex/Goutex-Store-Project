import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def atualizarGeneroJ():

    idgeneroj = int(input("Digite o ID do genero a ser atualizado: "))
    nomegeneroj = input("Digite o novo nome do genero: ")
    descricaogeneroj = input("Digite a nova descricao do genero: ")

    sql = f"UPDATE generosjogo SET nomegeneroj = '{nomegeneroj}', descricaogeneroj = '{descricaogeneroj}' WHERE idgeneroj = {idgeneroj}"
    cursor.execute(sql)
    conexao.commit()
    print("Genero atualizado com sucesso!")

# atualizarJogo()
# cursor.close()
# conexao.close()
