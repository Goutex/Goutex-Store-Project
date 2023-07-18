import mysql.connector
import importar
import baixarjogo
from connector import user, database, password, host

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def selecionando_jogo():
    while True:
        jogo = input("\nDigite o ID do jogo que você quer (V para voltar, M para mostrar jogos novamente): ").upper()

        if jogo == "V":
            return importar.menujogouser.menu()
        elif jogo == "M":
            importar.menujogos.mostrarjogos.mostrar_jogos()
        else:
            cursor.execute("SELECT nomejogo FROM jogos WHERE idjogo = %s", (jogo,))
            resultado = cursor.fetchone()

            if resultado:
                jogo = resultado[0]
                print(f"\nVocê escolheu {jogo}!")
                return gostaria_de_fazer()
            else:
                print("Jogo não encontrado. Digite novamente.")

def gostaria_de_fazer():
    while True:
        print("\nO que você gostaria de fazer?\n")
        print("B. Baixar Jogo")
        print("V. Voltar")

        fazer = input("> ").upper()

        if fazer == "B":
            baixarjogo.baixar_jogo()
            break
        elif fazer == "V":
            return selecionando_jogo()
        else:
            print("Opção inválida. Digite novamente.")

# selecionando_jogo()
# gostaria_de_fazer()


