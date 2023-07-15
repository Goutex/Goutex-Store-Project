import mysql.connector
from connector import host, user, password, database
import selecionandojogo

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def baixar_jogo():
    while True:
        try:
            print("\nPara baixar o jogo:\n")
            
            while True:
                jogo = input("Digite o ID do jogo novamente: ")
                if not jogo.isdigit():
                    print("ID inválido. Digite novamente.")
                else:
                    break
            
            usuariozinho = input("Digite seu Usuário: ")
            
            cursor.execute("SELECT idjogo, nomejogo FROM jogos WHERE idjogo = %s", (jogo,))
            resultado = cursor.fetchone()

            if resultado:
                nomejogo = resultado[1]

                cursor.execute("SELECT usuario FROM cadastrouser WHERE usuario = %s", (usuariozinho,))
                informacoes = cursor.fetchone()

                if informacoes:

                    cursor.execute("INSERT INTO baixados (usuario, jogosbaixados) VALUES (%s, %s)", (usuariozinho, nomejogo))
                    conexao.commit()
                    print("\nJogo baixado com sucesso!")
                    return selecionandojogo.selecionando_jogo()
                else:
                    print("Usuário não encontrado.")
                    return
            else:
                print("Jogo não encontrado.")
                return

        except Exception as e:
            print("Erro ao baixar o jogo", str(e))
            continue

        break

# baixar_jogo()

# cursor.close()
# conexao.close()
