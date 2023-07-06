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
        while True:
            print("\n--- Sistema de manutenção dos jogos ---")
            print("1. Adicionar jogo")
            print("2. Atualizar jogo")
            print("3. Mostrar Jogos")
            print("4. Mostrar informações dos jogos")
            print("5. Deletar Jogo")
            print("0. Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                importar.exibirgenerosj.exibirGenerosJ()
                importar.adicionarjogo.adicionarJogo()
                self.conexao.commit()

            elif opcao == "2":
                importar.informacoesdosjogos.exibirInformacoesDosJogos()
                importar.atualizarjogo.atualizarJogo()
                self.conexao.commit()

            elif opcao == "3":
                importar.mostrarjogos.mostrarJogos()

            elif opcao == "4":
                importar.informacoesdosjogos.exibirInformacoesDosJogos()

            elif opcao == "5":
                importar.deletarjogo.deletarJogo()

            elif opcao == "0":
                break

            else:
                print("Opção inválida. Digite novamente.")

    def exibir_menu_generos(self):
        while True:
            print("\n--- Sistema de manutenção de gêneros dos jogos ---")
            print("1. Adicionar Gênero")
            print("2. Exibir Gêneros")
            print("3. Atualizar Gênero")
            print("4. Exibir descrição do Gênero")
            print("5. Deletar Gênero")
            print("0. Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                importar.adicionargeneroj.adicionarGeneroj()

            elif opcao == "2":
                importar.exibirgenerosj.exibirGenerosJ()

            elif opcao == "3":
                importar.atualizargeneroj.atualizarGeneroJ()

            elif opcao == "4":
                importar.descricaogeneroj.exibirDescricaoGeneroJ()

            elif opcao == "5":
                importar.deletargeneroj.deletarGeneroJ()

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("\nOpção inválida. Digite novamente.")

    def run(self):
        while True:
            print("\n--- Loja de Jogos ---")
            print("1. Gerenciar Jogos")
            print("2. Gerenciar Gêneros")
            print("0. Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.exibir_menu_jogos()

            elif opcao == "2":
                self.exibir_menu_generos()

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("\nOpção inválida. Digite novamente.")

        self.cursor.close()
        self.conexao.close()


admin = Admin()
admin.run()
