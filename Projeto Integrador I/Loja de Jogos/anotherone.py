import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def cadastro_usuario():
    nome = input("\nDigite seu nome completo: ")
    usuario = input("Digite o seu nome de Usuário: ")
    senha = input("Digite uma senha: ")
    ano = input("Digite o ano que você nasceu: ")
    mes = input("Digite o mês que você nasceu, Ex: 6 ou 12 ")
    dia = input("Digite o dia que você nasceu: ")
    data_nascimento = f"{ano}-{mes}-{dia}"
    email = input("Digite seu email: ")
    telefone = input("Digite seu número de telefone: ")

    try:
        
        cursor.execute("SELECT * FROM cadastrouser WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()  

        if resultado:
            print("Usuário já existente. Por favor, escolha um nome de usuário diferente.")
        else:
            
            cursor.execute("INSERT INTO cadastrouser (usuario, senha, nome, email, data_nascimento, telefone) VALUES (%s, %s, %s, %s, %s, %s)",
                           (usuario, senha, nome, email, data_nascimento, telefone))
            conexao.commit()
            print("Usuário cadastrado com sucesso!")

            
    except mysql.connector.Error as error:
        print(f"Erro ao cadastrar usuário: {error}")


