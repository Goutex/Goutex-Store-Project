ano = input("Digite o ano que voce nasceu: ")
mes = input("Digite o mes que voce nasceu: ")
dia = input("Digite o dia que voce nasceu: ")
    # data_nascimento = input("Digite sua data de nascimento no formato (AAAA-MM-DD): ")
data_nascimento = (f"{ano}0{mes}{dia}")

print(data_nascimento)