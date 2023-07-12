import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def baixar_jogo():
    
    # try:

        print("\nPara baixar o jogo:\n")
        jogo = int(input("Digite o ID do jogo novamente: "))
        nick = input("Digite seu Usuario: ")

        cursor.execute("SELECT idjogo, nomejogo FROM jogos WHERE idjogo = %s", (jogo,))
        resultado = cursor.fetchone()

        nomejogo = resultado[1]

        cursor.execute("SELECT usuario, usuario FROM cadastrouser WHERE usuario = %s", (nick,))
        informacoes = cursor.fetchone()

        usuariozinho = informacoes[1]

        print(usuariozinho,nomejogo)
        # SELECT WHERE nomejogo and jogo = tal
        cursor.execute("INSERT INTO baixados (usuario, jogosbaixados) VALUES (%s, %s)", (usuariozinho, nomejogo))
        conexao.commit()
        print("Jogo baixado com sucesso!")

    # except:error = voce ja tem esse jogo!
        
# baixar_jogo()
# conexao.close()
