import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def deletar_generoj():
    while True:
        try:
            idgeneroj = input("\nDigite o ID do gênero a ser deletado: ")

            if not idgeneroj.isdigit():
                print("ID inválido. Digite novamente.")
                continue

            cursor = conexao.cursor()
            sql = f"DELETE FROM generosjogo WHERE idgeneroj = '{idgeneroj}'"
            cursor.execute(sql)
            conexao.commit()
            print("\nGênero deletado com sucesso!")
            break

        except mysql.connector.Error as error:
            print(f"Erro ao deletar o gênero: {error}")
            continue

        break

# deletar_generoj()

# conexao.close()
