import mysql.connector
from connector import host, user, password, database
import importar

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

# Criando o cursor
cursor = conexao.cursor()

def cadastro():

    print("\n                      --- Bem Vindo! --- \n")
    print(" Para acessar a Goutex Store voce precisa fazer seu cadastro! ")

def menu():
    while True:
        print("\n--- Podemos comecar? ---:")
        print("1. Sim")
        print("2. Nao")
        opcao = input("> ")

        if opcao == "1":
            importar.cadastrousuario.cadastroUsuario()

        elif opcao == "2":
            print("Tchau Tchau")
            break

cadastro()
menu()



