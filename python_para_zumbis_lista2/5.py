a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))


if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")