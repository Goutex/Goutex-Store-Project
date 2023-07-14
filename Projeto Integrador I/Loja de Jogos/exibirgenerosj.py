import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def exibir_generosj():
    cursor.execute("SELECT * FROM generosjogo")
    generos = cursor.fetchall()
    print("\nLista de Gêneros:\n")
    for genero in generos:
        print(f"{genero[0]}. {genero[1]}")

# exibirGenerosJ()
# cursor.close()
# conexao.close()


    



