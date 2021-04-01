x = 1
soma = 0
cont = 0

while True:
    x = int(input("Digite um número para somar. Digite 0 para parar."))
    if x == 0:
        break
    else:
        soma = soma + x
        print(soma)
        cont = cont + 1

media = soma / cont


print(f"Soma dos números: {soma}. A média é de: {media}")