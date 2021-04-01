x: int; soma: int

x = int(input("Digite o primeiro número: "))

soma = 0

while x != 0:
    x = int(input("Digite outro número: "))
    soma = soma + x

print("SOMA = ", soma)