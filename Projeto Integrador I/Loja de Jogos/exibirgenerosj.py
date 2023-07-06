import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def exibirGenerosJ():
    cursor.execute("SELECT * FROM generosjogo")
    generos = cursor.fetchall()
    print("Lista de Gêneros:")
    for genero in generos:
        print(f"{genero[0]}. {genero[2]}")

# exibirGenerosJ()
# cursor.close()
# conexao.close()


    



