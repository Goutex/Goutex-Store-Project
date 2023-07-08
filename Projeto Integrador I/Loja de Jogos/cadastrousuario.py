import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Criando o cursor
cursor = conexao.cursor()

def cadastro_usuario():
    nome = input("\nDigite seu nome completo: ")
    usuario = input("Digite o seu nome de Usuário: ")
    senha = input("Digite uma senha: ")
    ano = input("Digite o ano que você nasceu: ")
    mes = input("Digite o mês que você nasceu com somente um dígito, Ex: 6\n> ")
    dia = input("Digite o dia que você nasceu: ")
    data_nascimento = f"{ano}-0{mes}-{dia}"
    email = input("Digite seu email: ")
    telefone = input("Digite seu número de telefone: ")

    try:
        # Verificar se já existe um usuário com o mesmo nome de usuário (usuariocol)
        cursor.execute("SELECT * FROM cadastrouser WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            print("Usuário já existente. Por favor, escolha um nome de usuário diferente.")
        else:
            # Inserir o novo usuário
            cursor.execute("INSERT INTO cadastrouser (usuario, senha, nome, email, data_nascimento, telefone) VALUES (%s, %s, %s, %s, %s, %s)",
                           (usuario, senha, nome, email, data_nascimento, telefone))
            conexao.commit()
            print("Usuário cadastrado com sucesso!")

            definirNick(usuario)
    except mysql.connector.Error as error:
        print(f"Erro ao cadastrar usuário: {error}")

def definir_nick(usuario):
    nick = input("Digite seu Nick: ")

    try:
        # Verificar se já existe um registro com o mesmo usuário na tabela 'usuario'
        cursor.execute("SELECT idcadastro FROM cadastrouser WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            idcadastro = resultado[0]
            # Inserir o nick na tabela 'usuario'
            cursor.execute("INSERT INTO usuario (nick, idcadastro) VALUES (%s, %s)", (nick, idcadastro))
            conexao.commit()
            print("Nick adicionado com sucesso!")
        else:
            print("Usuário não encontrado.")
    except mysql.connector.Error as error:
        print(f"Erro ao adicionar nick: {error}")

# Fechando a conexão com o banco de dados
# conexao.close()
