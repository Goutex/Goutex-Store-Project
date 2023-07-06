import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(

    host = host,
    user = user,
    password= password,  
    database= database,  
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
