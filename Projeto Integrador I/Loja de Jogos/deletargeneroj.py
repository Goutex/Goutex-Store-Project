import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def deletar_generoj():
    cursor = conexao.cursor()
    idgeneroj = input("Digite o ID do genero a ser deletado: ")
    sql = f"DELETE FROM generosjogo WHERE idgeneroj = '{idgeneroj}'"
    cursor.execute(sql)
    conexao.commit()
    print("Genero deletado com sucesso!")