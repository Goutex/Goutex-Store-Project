import mysql.connector
from connector import host, user, password, database
import selecionandojogo
import importar

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def jogos_usuario():
    
    usuariozinho = input("\nDigite seu Usuário: ")

    cursor.execute("SELECT * FROM baixados WHERE usuario = %s", (usuariozinho,))

    jogos = cursor.fetchall()
        
    if jogos:
        print("\nSeus jogos:\n")
        for jogo in jogos:
            print(f"{jogo[1]}")
        jogar_voltar()
    else:
        print("\nVoce nao tem jogos.")
        return

def jogar_voltar():
     
    fazer = input("\nO que voce deseja fazer?\nJ. Jogar\nV. Voltar\n> ").upper()

    if fazer == "J":

        jogo = input("\nDigite o nome do jogo que voce quer jogar: ").capitalize()

        cursor.execute("SELECT jogosbaixados FROM baixados WHERE jogosbaixados = %s", (jogo,))
        resultado = cursor.fetchone()
    
        jogo = resultado[0]
        print(f"\nAbrindo {jogo}!")
        importar.menujogouser.menu()
    
    elif fazer == "V":
        importar.menujogouser.menu()
