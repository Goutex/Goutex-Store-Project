import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "180957",#SUA SENHA
    database = "projeto1", #SEU DATABASE
)
cursor = conexao.cursor()

def exibirDescricaoGeneroJ():
        
        cursor.execute("SELECT * FROM generosjogo")
        informacoes = cursor.fetchall()
        print("\nMostrando descricao dos generos: \n")
        if informacoes:
            for informacao in informacoes:

                print("ID do Genero:", informacao[0])
                print("Nome do Genero:", informacao[1])
                print(f"Descricao do Genero:, {informacao[2]}\n")

        else:
            print("Nenhuma informacao foi cadastrada.")

# exibirDescricaoGeneroJ()
# cursor.close()
# conexao.close()        

