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
        print("A. Adicionar Genero")
        print("E. Exibir Generos")
        print("T. Atualizar Genero")
        print("X. Exibir descricao do Genero")
        print("D. Deletar Genero")
        print("S. Sair")

        opcao = input("Digite a opção desejada: ").upper()

        if opcao == "A":
    
            adicionargeneroj.adicionar_generoj()

        elif opcao == "E":
            exibirgenerosj.exibir_generosj()

        elif opcao == "T":
            atualizargeneroj.atualizar_generoj()

        elif opcao == "X":
            descricaogeneroj.exibir_descricao_generoj()

        elif opcao == "D":
            deletargeneroj.deletar_generoj()
        
        elif opcao == "S":
            print("Saindo...")
            break

        else:
            print("\nOpção inválida. Digite novamente.")

# menu()

# cursor.close()
# conexao.close()