import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "180957",#SUA SENHA
    database = "projeto1", #SEU DATABASE
)

cursor = conexao.cursor()

def exibirGenerosJ():
    cursor.execute("SELECT * FROM generosjogo")
    generos = cursor.fetchall()
    print("Lista de Gêneros:")
    for genero in generos:
        print(f"{genero[0]}. {genero[1]}")

# exibirGenerosJ()
# cursor.close()
# conexao.close()


    



