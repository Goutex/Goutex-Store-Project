import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
)

cursor = conexao.cursor()

def tabela_cadastro():

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cadastrouser (
            idcadastro INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            usuario VARCHAR(20),
            senha VARCHAR(20),
            data_nascimento DATE,
            email VARCHAR(50),
            telefone VARCHAR(15)
        )
    ''')

def criar_tabela_jogos():
    
    cursor.execute('''
        "CREATE TABLE IF NOT EXISTS jogos (
            idjogo INT AUTO_INCREMENT PRIMARY KEY,
            nomejogo VARCHAR(45),
            descricaojogo VARCHAR(255),
            idgeneroj INT,
            FOREIGN KEY (idgeneroj) REFERENCES generosjogo(idgeneroj)
        )          
    ''')

def criar_tabela_usuario():
    
    cursor.execute('''
        "CREATE TABLE IF NOT EXISTS usuario (
            nick VARCHAR(20) PRIMARY KEY,
            FOREIGN KEY (idcadastro) REFERENCES cadastrouser(idcadastro)
        )          
    ''')

# criarTabelaJogos()
tabela_cadastro()
criar_tabela_usuario()

conexao.commit()
conexao.close()


