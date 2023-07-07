import importar

import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def menu():

    while True:
        print("\n--- Sistema de manutencao dos jogos ---")
        print("1. Mostrar Jogos")
        print("2. Mostrar informacoes do Jogos")
        # print("3. Baixar Jogo")
        # print("4. Favoritar Jogo")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            importar.menujogos.mostrarjogos.mostrarJogos()
            conexao.commit()

        elif opcao == "2":
            importar.menujogos.informacoesdosjogos.exibirInformacoesDosJogos()
            conexao.commit()

        elif opcao == "3":
            pass
        
        elif opcao == "4":
            pass

        elif opcao == "0":
            break
        
        else:
            print("Opção inválida. Digite novamente.")

# menu()

# cursor.close()
# conexao.close()