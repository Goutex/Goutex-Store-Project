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
        print("M. Mostrar jogos da Loja")
        print("J. Mostrar meus jogos")
        print("S. Sair")

        opcao = input("\nDigite a opção desejada: ").upper()

        if opcao == "S":
    
            importar.Acessando.acessando()
        
        elif opcao == "M":
            importar.menujogos.mostrarjogos.mostrar_jogos()

            print("\nS. Selecionar jogo")
            print("V. Voltar")
            selecionar = input("> ").upper()
            if selecionar == "S":
                importar.selecionandojogo.selecionando_jogo()
            elif selecionar == "V":
                return menu()
            

            conexao.commit()

        elif opcao == "J":
            importar.jogosusuario.jogos_usuario()
        
        elif opcao == "4":
            pass
 
        else:
            print("Opção inválida. Digite novamente.")

