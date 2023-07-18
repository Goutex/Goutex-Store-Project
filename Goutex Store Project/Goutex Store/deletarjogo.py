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

            cursor.execute("SELECT nomejogo FROM jogos WHERE idjogo = %s", (idjogo,))
            resultado = cursor.fetchone()
            jogo = resultado[0]
            print(jogo)
            cursor.execute("DELETE FROM baixados WHERE jogosbaixados = %s", (jogo,))
            cursor.execute("DELETE FROM jogos WHERE idjogo = %s", (idjogo,))

            conexao.commit()
            print("\nJogo deletado com sucesso!")
            break

        except mysql.connector.Error as error:
            print(f"Erro ao deletar o jogo: {error}")
            continue

        break

# deletar_jogo()

