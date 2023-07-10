import mysql.connector
import importar

from connector import user, database, password, host

class Loja:
    def __init__(self,nome):
        self.nome = nome
        self.conexao = mysql.connector.connect(
            host = host,
            user = user,
            password= password,
            database= database
        )
        self.cursor = self.conexao.cursor()

    def pesquisar_jogos():
        importar.menujogouser.menu()

# Loja.pesquisar_jogos()
