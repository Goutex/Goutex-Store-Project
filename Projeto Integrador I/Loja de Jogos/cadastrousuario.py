import mysql.connector
from connector import host, user, password, database
import re

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def validar_data(data):
    # Verifica se a data possui o formato correto (YYYY-MM-DD)
    if re.match(r"\d{4}-\d{2}-\d{2}", data):
        return True
    return False

def validar_email(email):
    # Verifica se o email possui o formato correto
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def validar_telefone(telefone):
    # Verifica se o telefone possui o formato correto (entre 10 e 14 dígitos)
    if re.match(r"\d{10,14}", telefone):
        return True
    return False

def validar_nome(nome):
    # Verifica se o nome possui pelo menos duas palavras (nome e sobrenome)
    if re.match(r"\b\w+\b \b\w+\b", nome):
        return True
    return False

def validar_senha(senha):
    # Verifica se a senha atende aos critérios necessários
    if len(senha) >= 8:
        return True
    return False

def cadastro_usuario():
    nome = input("\nDigite seu nome completo: ")
    while not validar_nome(nome):
        print("Nome inválido. Digite novamente.")
        nome = input("Digite seu nome completo: ")

    data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")
    while not validar_data(data_nascimento):
        print("Data de nascimento inválida. Digite novamente.")
        data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")

    email = input("Digite seu email: ")
    while not validar_email(email):
        print("Email inválido. Digite novamente.")
        email = input("Digite seu email: ")

    telefone = input("Digite seu número de telefone (entre 10 e 14 dígitos): ")
    while not validar_telefone(telefone):
        print("Telefone inválido. Digite novamente.")
        telefone = input("Digite seu número de telefone (entre 10 e 14 dígitos): ")

    usuario = input("Digite o seu nome de Usuário: ")
    while True:
        senha = input("Digite uma senha (mínimo 8 caracteres): ")
        if validar_senha(senha):
            break
        else:
            print("Senha inválida. Digite novamente.")

    try:
        cursor.execute("SELECT * FROM cadastrouser WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            print("Usuário já existente. Por favor, escolha um nome de usuário diferente.")
            cadastro_usuario()  # Chama novamente a função para recomeçar o cadastro
        else:
            cursor.execute("INSERT INTO cadastrouser (usuario, senha, nome, email, data_nascimento, telefone) VALUES (%s, %s, %s, %s, %s, %s)",
                           (usuario, senha, nome, email, data_nascimento, telefone))
            conexao.commit()
            print("Usuário cadastrado com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao cadastrar usuário: {error}")

# cadastro_usuario()
