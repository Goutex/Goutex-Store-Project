import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def atualizar_jogo():
    while True:
        idjogo = input("Digite o ID do jogo a ser atualizado: ")
        if not idjogo.isdigit():
            print("ID inválido. Digite novamente.")
        else:
            break

    while True:
        nomejogo = input("Digite o novo nome do jogo: ")
        if not nomejogo.strip():
            print("Nome inválido. Digite novamente.")
        else:
            break

    while True:
        descricaojogo = input("Digite a nova descrição do jogo (mínimo 30 letras): ")
        if len(descricaojogo) < 30:
            print("A descrição deve conter no mínimo 30 letras. Digite novamente.")
        else:
            break

    while True:
        idgeneroj = input("Digite o novo ID do gênero do jogo: ")
        if not idgeneroj.isdigit():
            print("ID de gênero inválido. Digite novamente.")
        else:
            break

    sql = f"UPDATE jogos SET nomejogo = '{nomejogo}', descricaojogo = '{descricaojogo}', idgeneroj = {idgeneroj} WHERE idjogo = {idjogo}"
    cursor.execute(sql)
    conexao.commit()
    print("Jogo atualizado com sucesso!")

# atualizar_jogo()


