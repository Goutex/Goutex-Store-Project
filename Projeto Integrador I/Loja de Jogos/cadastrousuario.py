import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

# Criando o cursor
cursor = conexao.cursor()

def cadastroUsuario():
    nome = input("Digite seu nome completo: ")

    usuario = input("Digite o seu nome de Usuario: ")
    senha = input("Digite uma senha: ")

    ano = input("Digite o ano que voce nasceu: ")
    mes = input("Digite o mes que voce nasceu com somente um digito, Ex: 6\n> ")
    dia = input("Digite o dia que voce nasceu: ")
    
    data_nascimento = (f"{ano}0{mes}{dia}")

    email = input("Digite seu email: ")
    telefone = input("Digite seu numero de telefone: ")
    sql = '''
        INSERT INTO cadastrouser (nome, usuario, senha, data_nascimento, email, telefone)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    values = (nome, usuario, senha, data_nascimento, email, telefone)
    cursor.execute(sql, values)
    conexao.commit()
    print("Usuário cadastrado com sucesso!")

cadastroUsuario()

# Fechando a conexão com o banco de dados
# conexao.close()
