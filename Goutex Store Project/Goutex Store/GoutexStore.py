import mysql.connector
from connector import host, user, password, database
import importar
from importar import Login, Cadastro

class GoutexStore:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None
        self.usuario = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conexao.cursor()
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

    def desconectar(self):
        if self.conexao:
            self.conexao.close()

    def entrar_na_loja(self):
        print("\n         --- Seja Bem Vindo a Goutex Store --- ")

        while True:
            print(f"\n                --- Área de Acesso --- \n")
            print("E. Entrar")
            print("F. Fazer Cadastro")
            print("S. Sair")
            opcao = input("> ").upper()

            try:
                if opcao == "E":
                    Login.verificar_login()

                elif opcao == "F":
                    Cadastro.cadastro()

                elif opcao == "S":
                    print("\nTchau Tchau")
                    break
                else:
                    raise ValueError("\nOpção inválida! Por favor, selecione uma opção válida.")
            except Exception as e:
                print(f"{e}")

    def executar(self):
        try:
            self.conectar()
            self.entrar_na_loja()
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            self.desconectar()

goutex_store = GoutexStore()
goutex_store.executar() 