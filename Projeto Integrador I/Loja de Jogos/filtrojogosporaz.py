import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

# Executar a consulta SELECT
selecionando = "SELECT * FROM jogos WHERE nomejogo LIKE 'A%' ORDER BY nomejogo ASC"
cursor.execute(selecionando)

jogos = cursor.fetchall()
print("Lista de Jogos:")
for jogo in jogos:
    print(f"{jogo[0]}. {jogo[1]}")

# Fechar cursor e conexão
# cursor.close()
# conexao.close()
