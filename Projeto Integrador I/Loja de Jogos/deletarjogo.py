import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sen@c2021",  # SUA SENHA
    database="projetinho",  # SEU DATABASE
)

cursor = conexao.cursor()

def deletarJogo():
    cursor = conexao.cursor()
    idjogo = input("Digite o ID do jogo a ser deletado: ")
    sql = f"DELETE FROM jogos WHERE idjogo = '{idjogo}'"
    cursor.execute(sql)
    conexao.commit()
    print("Jogo deletado com sucesso!")