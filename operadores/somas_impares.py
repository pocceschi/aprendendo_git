print("Digite dois números: ")
x = int(input())
y = int(input())

soma = 0

if x > y:
    troca = x
    x = y
    y = troca


for i in range(x+1, y):
        if i % 2 != 0:
            soma = soma + i


print(f"Soma dos impares: {soma}")