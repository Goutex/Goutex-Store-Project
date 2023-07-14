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

    while True:
        print("\n--- Podemos comecar? ---:")
        print("S. Sim")
        print("N. Nao")
        opcao = input("> ").upper()

        if opcao == "S":
            importar.cadastrousuario.cadastro_usuario()
            print("\nAgora que voce terminou o cadastro pode fazer o login!")
            break

        elif opcao == "N":
            break

# cadastro()
# menu()



