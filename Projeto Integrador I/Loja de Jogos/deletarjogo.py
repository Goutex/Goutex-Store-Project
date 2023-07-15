import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def deletar_jogo():
    while True:
        try:
            idjogo = input("\nDigite o ID do jogo a ser deletado: ")

            if not idjogo.isdigit():
                print("ID inválido. Digite novamente.")
                continue

            cursor = conexao.cursor()
            sql = f"DELETE FROM jogos WHERE idjogo = '{idjogo}'"
            cursor.execute(sql)
            conexao.commit()
            print("\nJogo deletado com sucesso!")
            break

        except mysql.connector.Error as error:
            print(f"Erro ao deletar o jogo: {error}")
            continue

        break

# deletar_jogo()

# conexao.close()
