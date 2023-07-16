import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def adicionar_jogo():
    while True:
        nomejogo = input("\nDigite o nome do jogo: ").capitalize()
        if not nomejogo.strip():
            print("Nome inválido. Digite novamente.")
        else:
            break

    while True:
        idgeneroj = input("\nDigite o ID do gênero do jogo: ")
        if not idgeneroj.isdigit():
            print("ID inválido. Digite novamente.")
        else:
            break

    while True:
        descricaojogo = input("\nDigite uma descrição para o jogo (mínimo 30 letras): ")
        if len(descricaojogo) < 30:
            print("A descrição deve conter no mínimo 30 letras. Digite novamente.")
        else:
            break
    
    sql = "INSERT INTO jogos (nomejogo, idgeneroj, descricaojogo) VALUES (%s, %s, %s)"
    valores = (nomejogo, idgeneroj, descricaojogo)

    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("\nJogo adicionado com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao adicionar o jogo: {error}")

# adicionar_jogo()

# cursor.close()
# conexao.close()
