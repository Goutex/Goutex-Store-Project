import importar
import Cadastro
import Login
import sys

import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


def acessando():
    print("\n--- Seja Bem Vindo à Goutex Store ---")

    while True:
        print("\n--- Área de Acesso ---")
        print("E. Entrar")
        print("F. Fazer Cadastro")
        print("S. Sair")
        opcao = input("> ").upper()

        if opcao == "E":
            Login.verificar_login() 

        elif opcao == "F":
            Cadastro.cadastro()  

        elif opcao == "S":
            print("\n --- Tchau Tchau --- \n")
            sys.exit()  

        else:
            print("\nOpção inválida. Digite novamente.")

   

# acessando()
