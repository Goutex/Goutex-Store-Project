import mysql.connector
import importar
import baixarjogo

from connector import user, database, password, host

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()



def selecionando_jogo():

    jogo = int(input("\nDigite o ID do jogo que você quer:\n\nou\n\n0. Voltar\n1. Mostrar jogos novamente\n\n> "))

    if jogo == 0:
        return importar.menujogouser.menu()
    elif jogo == 1:
        return importar.menujogos.mostrarjogos.mostrar_jogos()

    cursor.execute("SELECT nomejogo FROM jogos WHERE idjogo = %s", (jogo,))
    resultado = cursor.fetchone()
    
    jogo = resultado[0]
    print(f"\nVoce escolheu {jogo}!")
    return gostaria_de_fazer()

def gostaria_de_fazer():

    print("\nO que voce gostaria de fazer?\n")
    print("1. Baixar Jogo")
    print("0. Voltar\n")

    fazer = int(input("> "))

    if fazer == 1:
        baixarjogo.baixar_jogo()
        
    else:
        return selecionando_jogo()

# selecionando_jogo()
# gostaria_de_fazer()


