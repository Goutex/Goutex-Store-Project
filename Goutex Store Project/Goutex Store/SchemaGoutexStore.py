#This file creates the tables in the MySql Schema used in the Project

import mysql.connector
from importar import host, user, password, database
# Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(
    
    host=host,
    user=user,
    password=password,
    database=database

)

# Criação do cursor para executar as consultas SQL
cursor = conexao.cursor()

# Código SQL para criar as tabelas
create_table_queries = [
    """
    CREATE TABLE IF NOT EXISTS cadastrouser (
        idcadastro INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        usuario VARCHAR(20) NOT NULL,
        senha VARCHAR(20) NOT NULL,
        data_nascimento DATE NOT NULL,
        email VARCHAR(50) NOT NULL,
        telefone VARCHAR(15) NOT NULL,
        PRIMARY KEY (idcadastro),
        UNIQUE KEY email_UNIQUE (email),
        UNIQUE KEY usuario_UNIQUE (usuario),
        UNIQUE KEY telefone_UNIQUE (telefone)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS baixados (
        usuario VARCHAR(20) NOT NULL,
        jogosbaixados VARCHAR(45) NOT NULL,
        PRIMARY KEY (usuario, jogosbaixados),
        FOREIGN KEY (usuario) REFERENCES cadastrouser (usuario)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS generosjogo (
        idgeneroj INT NOT NULL AUTO_INCREMENT,
        nomegeneroj VARCHAR(45) NOT NULL,
        descricaogeneroj VARCHAR(150) NOT NULL,
        PRIMARY KEY (idgeneroj),
        UNIQUE KEY nomegeneroj_UNIQUE (nomegeneroj)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS jogos (
        idjogo INT NOT NULL AUTO_INCREMENT,
        nomejogo VARCHAR(45) NOT NULL,
        descricaojogo VARCHAR(255) NOT NULL,
        idgeneroj INT NOT NULL,
        PRIMARY KEY (idjogo),
        UNIQUE KEY nomejogo_UNIQUE (nomejogo),
        FOREIGN KEY (idgeneroj) REFERENCES generosjogo (idgeneroj)
    )
    """
]

# Execução dos comandos SQL para criar as tabelas
for query in create_table_queries:
    cursor.execute(query)

# Código SQL para inserir dados nas tabelas
insert_data_queries = [
    
    """
    INSERT INTO cadastrouser (nome, usuario, senha, data_nascimento, email, telefone)
    VALUES ('Matheus Silva Dos Santos', 'oclarkzin', 'Matheus123', '2005-06-22', 'matheus00fernanda@gmail.com', '48988756369')
    """,

]

# Execução dos comandos SQL para inserir dados
for query in insert_data_queries:
    cursor.execute(query)

# Confirma as alterações no banco de dados
conexao.commit()

# Fechar a conexão com o banco de dados
cursor.close()
conexao.close()
