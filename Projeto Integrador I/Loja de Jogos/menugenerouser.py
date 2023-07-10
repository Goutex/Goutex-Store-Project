import adicionargeneroj
import exibirgenerosj
import descricaogeneroj
import atualizargeneroj
import deletargeneroj
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
        print("\n--- Goutex Store ---")
        print("1. Adicionar Genero")
        print("2. Exibir Generos")
        print("3. Atualizar Genero")
        print("4. Exibir descricao do Genero")
        print("5. Deletar Genero")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
    
            adicionargeneroj.adicionar_generoj()

        elif opcao == "2":
            exibirgenerosj.exibir_generosj()

        elif opcao == "3":
            atualizargeneroj.atualizar_generoj()

        elif opcao == "4":
            descricaogeneroj.exibir_descricao_generoj()

        elif opcao == "5":
            deletargeneroj.deletar_generoj()
        
        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("\nOpção inválida. Digite novamente.")

# menu()

# cursor.close()
# conexao.close()