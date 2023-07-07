import mysql.connector
from connector import host, user, password, database
import importar
import Acessando

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

    def EntrarNaLoja(self):
        Acessando.acessando()
        

    def executar(self):
        self.conectar
        self.EntrarNaLoja
        self.desconectar

# Criando uma instância da classe GoutexStore e executando o programa
goutex_store = GoutexStore()
goutex_store.executar()
