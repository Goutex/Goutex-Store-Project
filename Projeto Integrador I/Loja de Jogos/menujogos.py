import adicionarjogo
import atualizarjogo
import exibirgenerosj
import informacoesdosjogos
import mostrarjogos
import deletarjogo

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
        print("\n--- Sistema de manutencao dos jogos ---")
        print("1. Adicionar jogo")
        print("2. Atualizar jogo")
        print("3. Mostrar Jogos")
        print("4. Mostrar informacoes dos jogos")
        print("5. Deletar Jogo")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            exibirgenerosj.exibirGenerosJ()
            adicionarjogo.adicionarJogo()
            conexao.commit()

        elif opcao == "2":
            informacoesdosjogos.exibirInformacoesDosJogos()
            atualizarjogo.atualizarJogo()
            conexao.commit()

        elif opcao == "3":
            mostrarjogos.mostrarJogos()
        
        elif opcao == "4":
            informacoesdosjogos.exibirInformacoesDosJogos()

        elif opcao == "5":
            deletarjogo.deletarJogo()

        elif opcao == "0":
            break
        
        else:
            print("Opção inválida. Digite novamente.")

menu()

cursor.close()
conexao.close()