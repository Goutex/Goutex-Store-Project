import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sen@c2021",  # SUA SENHA
    database="projetinho",  # SEU DATABASE
)

cursor = conexao.cursor()

def criarTabelaJogos():
    # Added import statement for the "generosjogo" table
    cursor.execute("CREATE TABLE jogos (idjogo INT AUTO_INCREMENT PRIMARY KEY, nomejogo VARCHAR(45), descricaojogo VARCHAR(255), idgeneroj INT, FOREIGN KEY (idgeneroj) REFERENCES generosjogo(idgeneroj))")

# Call the function to create the table
criarTabelaJogos()

# Commit the changes made to the database
conexao.commit()

# Close the database connection
conexao.close()
