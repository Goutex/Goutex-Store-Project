import mysql.connector
import importar
from connector import user, database, password, host

class Admin:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = host,
            user = user,
            password= password,
            database= database
        )
        self.cursor = self.conexao.cursor()

    def exibir_menu_jogos(self):

        importar.menujogos.menu()

    def exibir_menu_generos(self):

        importar.menugenerosj.menu()

    def run(self):
        while True:
            print("\n--- Loja de Jogos ---\n")
            print("1. Gerenciar Jogos")
            print("2. Gerenciar Gêneros")
            print("0. Sair")

            opcao = input("\nDigite a opção desejada: ")

            if opcao == "1":
                self.exibir_menu_jogos()

            elif opcao == "2":
                self.exibir_menu_generos()

            elif opcao == "0":
                return

            else:
                print("\nOpção inválida. Digite novamente.")

        self.cursor.close()
        self.conexao.close()

admin = Admin()
admin.run()
