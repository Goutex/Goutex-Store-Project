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
        print("\n  --- Goutex Store ---\n")
        print("1. Mostrar Jogos")
        print("2. Mostrar informacoes do Jogos")
        # print("3. Baixar Jogo")
        # print("4. Favoritar Jogo")
        print("0. Voltar")

        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            importar.menujogos.mostrarjogos.mostrar_jogos()

            print("\n1. Selecionar jogo")
            print("0. Voltar")
            selecionar = int(input("> "))
            if selecionar == 1:
                importar.selecionandojogo.selecionando_jogo()
            elif selecionar == 0:
                return menu()
            

            conexao.commit()

        elif opcao == "2":
            importar.menujogos.informacoesdosjogos.exibir_informacoes_dos_jogos()
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