import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def atualizar_generoj():
    while True:
        idgeneroj = input("Digite o ID do gênero a ser atualizado: ")
        if not idgeneroj.isdigit():
            print("ID inválido. Digite novamente.")
        else:
            break

    while True:
        nomegeneroj = input("Digite o novo nome do gênero: ")
        if not nomegeneroj.strip():
            print("Nome inválido. Digite novamente.")
        else:
            break

    while True:
        descricaogeneroj = input("Digite a nova descrição do gênero (mínimo 30 letras): ")
        if len(descricaogeneroj) < 30:
            print("A descrição deve conter no mínimo 30 letras. Digite novamente.")
        else:
            break

    sql = f"UPDATE generosjogo SET nomegeneroj = '{nomegeneroj}', descricaogeneroj = '{descricaogeneroj}' WHERE idgeneroj = {idgeneroj}"
    cursor.execute(sql)
    conexao.commit()
    print("Gênero atualizado com sucesso!")

# atualizar_generoj()


