import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def exibir_informacoes_dos_jogos():
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
