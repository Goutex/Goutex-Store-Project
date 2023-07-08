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
        print(f"\n      --- Fazer Login --- | --- Sou Novo Aqui --- \n")
        print("1. Entrar")
        print("2. Fazer Cadastro")
        print("3. Sair")
        opcao = input("> ")

        if opcao == "1":
            Login.verificar_login()

        elif opcao == "2":
            Cadastro.cadastro()

        elif opcao == "3":
            print("Tchau Tchau")
            break

acessando()
