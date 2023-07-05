import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sen@c2021",  # SUA SENHA
    database="projetinho",  # SEU DATABASE
)

cursor = conexao.cursor()

def deletarGeneroJ():
    cursor = conexao.cursor()
    idgeneroj = input("Digite o ID do genero a ser deletado: ")
    sql = f"DELETE FROM generosjogo WHERE idgeneroj = '{idgeneroj}'"
    cursor.execute(sql)
    conexao.commit()
    print("Genero deletado com sucesso!")