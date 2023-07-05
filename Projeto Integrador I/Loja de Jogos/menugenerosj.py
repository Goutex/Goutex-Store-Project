import adicionargeneroj
import exibirgenerosj
import descricaogeneroj
import atualizargeneroj
import deletargeneroj
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sen@c2021",#SUA SENHA
    database = "projetinho", #SEU DATABASE
)
cursor = conexao.cursor()

def menu():
    
    while True:
        print("\n--- Sistema de manutencao de generos dos jogos ---")
        print("1. Adicionar Genero")
        print("2. Exibir Generos")
        print("3. Atualizar Genero")
        print("4. Exibir descricao do Genero")
        print("5. Deletar Genero")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
    
            adicionargeneroj.adicionarGeneroj()

        elif opcao == "2":
            exibirgenerosj.exibirGenerosJ()

        elif opcao == "3":
            atualizargeneroj.atualizarGeneroJ()

        elif opcao == "4":
            descricaogeneroj.exibirDescricaoGeneroJ()

        elif opcao == "5":
            deletargeneroj.deletarGeneroJ()
        
        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("\nOpção inválida. Digite novamente.")

menu()

cursor.close()
conexao.close()