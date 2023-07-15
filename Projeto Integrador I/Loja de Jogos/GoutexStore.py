import mysql.connector
from connector import host, user, password, database
import importar
import Acessando
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

    def entrar_na_loja(self):
        
        print("\n         --- Seja Bem Vindo a Goutex Store --- ")

        while True:
            print(f"\n                --- Area de Acesso --- \n")
            print("E. Entrar")
            print("F. Fazer Cadastro")
            print("S. Sair")
            opcao = input("> ").upper()

            if opcao == "E":
                importar.Login.verificar_login()

            elif opcao == "F":
                importar.Cadastro.cadastro()

            elif opcao == "S":
                print("\nTchau Tchau")
                break
        

    def executar(self):
        self.conectar()
        self.entrar_na_loja()
        self.desconectar()

goutex_store = GoutexStore()
goutex_store.executar()

#This file is the start
