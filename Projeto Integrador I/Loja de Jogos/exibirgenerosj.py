import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sen@c2021",#SUA SENHA
    database = "projetinho", #SEU DATABASE
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


    



