import mysql.connector

# # Importing modules from correct files
# import exibirgenerosj 
# import adicionargeneroj

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sen@c2021",
    database="projetinho"
)

cursor = conexao.cursor()

def joinJogoGenero():
    cursor.execute("""
        SELECT jogos.*, generosjogo.nomegeneroj, generosjogo.descricaogeneroj 
        FROM jogos 
        INNER JOIN generosjogo ON jogos.idgeneroj = generosjogo.idgeneroj
    """)

    print("\nMostrando informacoes dos jogos:\n")

    result = cursor.fetchall()
    for row in result:
        print(f"ID do Jogo: {row[0]}")
        print(f"Nome do Jogo: {row[1]}")
        print(f"Descricao do Jogo: {row[2]}")
        print(f"ID do Genero do Jogo: {row[3]}")
        print(f"Nome do Genero do Jogo: {row[4]}")
        print(f"Descricao do Genero do Jogo: {row[5]}")
        print("\n")

joinJogoGenero()

cursor.close()
conexao.close()
