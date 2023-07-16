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

def cadastro():
    print("\n                   --- Bem-vindo! ---")
    print("Para acessar a Goutex Store, você precisa fazer seu cadastro!")

    while True:
        print("\n--- Podemos começar? ---")
        print("S. Sim")
        print("N. Não")
        opcao = input("> ").upper()

        if opcao == "S":
            importar.cadastrousuario.cadastro_usuario()
            print("\nAgora que você terminou o cadastro, pode fazer o login!")
            break

        elif opcao == "N":
            break

        else:
            print("Opção inválida. Digite novamente.")

# cadastro()
