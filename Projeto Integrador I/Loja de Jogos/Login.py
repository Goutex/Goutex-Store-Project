import mysql.connector
import importar

class VerificadorLogin:
    def __init__(self):
        self.host = importar.host
        self.user = importar.user
        self.password = importar.password
        self.database = importar.database
        self.conexao = None

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def desconectar(self):
        if self.conexao:
            self.conexao.close()

    def verificar_login(self):
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        self.conectar()
        cursor = self.conexao.cursor()

        sql = "SELECT * FROM cadastrouser WHERE usuario = %s AND senha = %s"
        values = (usuario, senha)

        cursor.execute(sql, values)
        resultado = cursor.fetchone()

        if resultado:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha inválidos.")

        cursor.close()
        self.desconectar()

# Exemplo de uso
verificador = VerificadorLogin()
verificador.verificar_login()
