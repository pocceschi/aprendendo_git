n = int(input("Digite um número inteiro: "))
cont = 0
x = 0

while True:
    n = n + x
    cont = cont + 1
    if cont == 10:
        break
    else:
        x = n + x
        print(n)
        print(x)



