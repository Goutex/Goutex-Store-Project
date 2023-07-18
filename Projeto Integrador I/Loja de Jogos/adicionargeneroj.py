import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def adicionar_generoj():
    while True:
        nomegeneroj = input("Digite um nome para o Gênero: ")
        if not nomegeneroj.strip():
            print("Nome inválido. Digite novamente.")
        else:
            break

    while True:
        descricaogeneroj = input("Digite uma descrição para o Gênero (mínimo 30 letras): ")
        if len(descricaogeneroj) < 30:
            print("A descrição deve conter no mínimo 30 letras. Digite novamente.")
        else:
            break
    
    sql = "INSERT INTO generosjogo (nomegeneroj, descricaogeneroj) VALUES (%s, %s)"
    valores = (nomegeneroj, descricaogeneroj)

    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Gênero de jogo adicionado com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao adicionar o Gênero de jogo: {error}")

# adicionar_generoj()


