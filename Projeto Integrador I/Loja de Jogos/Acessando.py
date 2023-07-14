import importar
import Cadastro
import Login

import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


def acessando():
    print("\n         --- Seja Bem Vindo a Goutex Store --- ")

    while True:
        print(f"\n                --- Area de Acesso --- \n")
        print("E. Entrar")
        print("F. Fazer Cadastro")
        print("S. Sair")
        opcao = input("> ").upper()

        if opcao == "E":
            Login.verificar_login()

        elif opcao == "F":
            Cadastro.cadastro()

        elif opcao == "S":
            print("\nTchau Tchau")
            break

# acessando()
