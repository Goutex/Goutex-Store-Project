import mysql.connector
import re
from connector import database, user, password, host

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
        cursor.execute("SELECT * FROM cadastrouser WHERE email = %s", (email,))
        resultado = cursor.fetchone()
        if resultado:
            print("\nEmail em uso. Por favor, use um email diferente.\n")
            return False
        return True
    else:
        return False

def validar_telefone(telefone):
    # Verifica se o telefone possui o formato correto (entre 10 e 14 dígitos)
    if re.match(r"\d{10,14}$", telefone):
        cursor.execute("SELECT * FROM cadastrouser WHERE telefone = %s", (telefone,))
        resultado = cursor.fetchone()
        if resultado:
            print("\nTelefone em uso. Por favor, use um número diferente.\n")
            return False
        return True
    else:
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
    nome = input("\nDigite seu nome completo: ").capitalize()
    while not validar_nome(nome):
        print("Nome inválido. Digite novamente.")
        nome = input("Digite seu nome completo: ")

    data_nascimento = input("Digite a data de nascimento (2023-07-17): ")
    while not validar_data(data_nascimento):
        print("Data de nascimento inválida. Digite novamente.")
        data_nascimento = input("Digite a data de nascimento (2023-07-17): ")

    email = input("Digite seu email: ")
    while not validar_email(email):
        print("Email inválido. Digite novamente.\n")
        email = input("Digite seu email: ")

    telefone = input("Digite seu número de telefone (entre 10 e 14 dígitos): ")
    while not validar_telefone(telefone):
        print("Telefone inválido. Digite novamente.\n")
        telefone = input("Digite seu número de telefone (entre 10 e 14 dígitos): ")

    while True:
        usuario = input("Digite o seu nome de Usuário: ")
        cursor.execute("SELECT * FROM cadastrouser WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            print("\nUsuário já existente. Por favor, escolha um nome de usuário diferente.\n")
        else:
            while True:
                senha = input("Digite uma senha (mínimo 8 caracteres): ")
                if validar_senha(senha):
                    cursor.execute("INSERT INTO cadastrouser (usuario, senha, nome, email, data_nascimento, telefone) VALUES (%s, %s, %s, %s, %s, %s)",
                            (usuario, senha, nome, email, data_nascimento, telefone))
                    conexao.commit()
                    print("Usuário cadastrado com sucesso!")
                    break
                else:
                    print("Senha inválida. Digite novamente.")

# cadastro_usuario()
