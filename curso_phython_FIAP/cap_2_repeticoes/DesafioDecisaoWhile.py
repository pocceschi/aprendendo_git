resposta = "SIM"

while resposta == "SIM":

    nivel_acesso = input("Qual o seu nível de acesso? Responda com ADM, USR ou GUEST.").upper()
    genero = input("Qual o seu gênero? Responda com M para masculino ou F para feminino.").upper()

    if nivel_acesso == "ADM":
        if genero == "F":
            print("Olá administradora!")
        elif genero == "M":
            print("Olá administrador!")
        else:
            print("Gênero diferente de M ou F.")
    elif nivel_acesso == "USR":
        if genero == "F":
            print("Olá usuária!")
        elif genero == "M":
            print("Olá usuário!")
        else:
            print("Gênero diferente de M ou F.")
    elif nivel_acesso == "GUEST":
        print("Olá visitante!")
    else:
        print("Olá desconhecido(a)!")
    resposta = input("Digite SIM para continuar: ").upper()