import mysql.connector
import importar

from connector import user, database, password, host

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()



def selecionando_jogo():
        
    jogo = int(input("\nDigite o ID do jogo que você quer: "))

    cursor.execute("SELECT nomejogo FROM jogos WHERE idjogo = %s", (jogo,))
    resultado = cursor.fetchone()
    if resultado:
        jogo = resultado[0]
        print(jogo)
        return 

# selecionando_jogo()