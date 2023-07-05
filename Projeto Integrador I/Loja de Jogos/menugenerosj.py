import adicionargeneroj
import exibirgenerosj
import descricaogeneroj
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "180957",#SUA SENHA
    database = "projeto1", #SEU DATABASE
)
cursor = conexao.cursor()

def menu():
    
    while True:
        print("\n--- Sistema de manutencao de generos dos jogos ---")
        print("1. Adicionar Genero")
        print("2. Exibir Generos")
        print("3. Exibir descricao do Genero")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
    
            adicionargeneroj.adicionarGeneroj()

        elif opcao == "2":
            exibirgenerosj.exibirGenerosJ()

        elif opcao == "3":
            descricaogeneroj.exibirDescricaoGeneroJ()
        
        elif opcao == "0":
            break

        else:
            print("\nOpção inválida. Digite novamente.")

menu()

cursor.close()
conexao.close()