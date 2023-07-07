import mysql.connector
from connector import host, user, password, database
import importar

class GoutexStore:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        if self.conexao:
            self.conexao.close()

    def cadastro(self):
        print("\n                      --- Bem Vindo! --- \n")
        print(" Para acessar a Goutex Store você precisa fazer seu cadastro! ")

    def menu(self):
        while True:
            print("\n--- Podemos começar? ---:")
            print("1. Sim")
            print("2. Não")
            opcao = input("> ")

            if opcao == "1":
                importar.cadastrousuario.cadastroUsuario()

            elif opcao == "2":
                print("Tchau Tchau")
                break

    def verificar_login(self):
        self.conectar()
        self.cursor = self.conexao.cursor()

        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        sql = "SELECT * FROM cadastrouser WHERE usuario = %s AND senha = %s"
        values = (usuario, senha)

        self.cursor.execute(sql, values)
        resultado = self.cursor.fetchone()

        if resultado:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha inválidos.")

        self.cursor.close()
        self.desconectar()

    def executar(self):
        self.verificar_login()
        self.cadastro()
        self.menu()

# Criando uma instância da classe GoutexStore e executando o programa
goutex_store = GoutexStore()
goutex_store.executar()
