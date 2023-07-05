import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="180957",
    database="projeto1"
)

cursor = conexao.cursor()

def exibirInformacoesDosJogos():
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
        print(f"Descricao do Genero do Jogo: {row[5]}\n")
        # print("\n")

# exibirInformacoesDosJogos()
# cursor.close()
# conexao.close()
