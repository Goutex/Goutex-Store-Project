import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def deletar_jogo():
    cursor = conexao.cursor()
    idjogo = input("Digite o ID do jogo a ser deletado: ")
    sql = f"DELETE FROM jogos WHERE idjogo = '{idjogo}'"
    cursor.execute(sql)
    conexao.commit()
    print("Jogo deletado com sucesso!")
    
