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

    jogo = (input("\nDigite o ID do jogo que você quer:\n\nou\n\nV. Voltar\nM. Mostrar jogos novamente\n\n> ")).upper()

    if jogo == "V":
        return importar.menujogouser.menu()
    elif jogo == "M":
        importar.menujogos.mostrarjogos.mostrar_jogos()
        return selecionando_jogo()

    cursor.execute("SELECT nomejogo FROM jogos WHERE idjogo = %s", (jogo,))
    resultado = cursor.fetchone()
    
    jogo = resultado[0]
    print(f"\nVoce escolheu {jogo}!")
    return gostaria_de_fazer()

def gostaria_de_fazer():

    print("\nO que voce gostaria de fazer?\n")
    print("B. Baixar Jogo")
    print("V. Voltar\n")

    fazer = input("> ").upper()

    if fazer == "B":
        baixarjogo.baixar_jogo()
        
    else:
        return selecionando_jogo()

# selecionando_jogo()
# gostaria_de_fazer()


