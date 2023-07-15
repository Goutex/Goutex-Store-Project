import mysql.connector
from connector import host, user, password, database
import re
from nameparser import HumanName

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
    # Verifica se o telefone possui o formato correto (apenas números e tamanho de 10 dígitos)
    if re.match(r"\d{10}", telefone):
        return True
    return False

def validar_nome(nome_completo):
    # Verifica se o nome possui pelo menos um sobrenome
    name = HumanName(nome_completo)
    if name.last:
        return True
    return False

def cadastro_usuario():
    while True:
        nome = input("\nDigite seu nome completo: ")
        usuario = input("Digite o seu nome de Usuário: ")
        senha = input("Digite uma senha: ")
        ano = input("Digite o ano que você nasceu: ")
        mes = input("Digite o mês que você nasceu (Ex: 6 ou 12): ")
        dia = input("Digite o dia que você nasceu: ")
        data_nascimento = f"{ano}-{mes}-{dia}"
        email = input("Digite seu email: ")
        telefone = input("Digite seu número de telefone (apenas números, 10 dígitos): ")

        if not validar_data(data_nascimento):
            print("Data de nascimento inválida. Digite novamente.")
            continue

        if not validar_email(email):
            print("Email inválido. Digite novamente.")
            continue

        if not validar_telefone(telefone):
            print("Telefone inválido. Digite novamente.")
            continue

        if not validar_nome(nome):
            print("Nome inválido. Digite novamente.")
            continue

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
                break

        except mysql.connector.Error as error:
            print(f"Erro ao cadastrar usuário: {error}")

cadastro_usuario()
