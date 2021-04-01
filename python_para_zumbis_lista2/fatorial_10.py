y = int(input("Leia um número: "))
x = 1
fatorial = 1

while x < y:
    fatorial = fatorial * x
    x = x + 1

print(f"O fatorial de {y} é {fatorial}.")
