x = input("Digite um número inteiro: ")

if x.isnumeric():
    x = int(x)
    if x % 2 == 0:
        print("Número par.")
    else:
        print("Número ímpar.")
else:
    print("O número não é inteiro.")




