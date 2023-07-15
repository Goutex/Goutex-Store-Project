import mysql.connector
from connector import host, user, password, database
import importar

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def mostrar_jogos():
    while True:
        cursor.execute("SELECT * FROM jogos")
        jogos = cursor.fetchall()
        print("\nLista de Jogos:\n")
        for jogo in jogos:
            print(f"{jogo[0]}. {jogo[1]}")

        print("\nS. Selecionar jogo")
        print("V. Voltar")
        selecionar = input("> ").upper()
        if selecionar == "S":
            importar.selecionandojogo.selecionando_jogo()
            break
        elif selecionar == "V":
            importar.menujogouser.menu()
            break
        else:
            print("\nOpção inválida. Digite novamente.")

    conexao.commit()
