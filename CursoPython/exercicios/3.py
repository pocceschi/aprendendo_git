n = input("Digite o primeiro nome do usuário: ")

x = len(n)

if x <= 4:
    print("Seu nome é curto.")
elif (x >= 5) and (x <= 6):
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")