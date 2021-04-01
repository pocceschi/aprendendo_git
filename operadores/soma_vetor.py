n = int(input("Quantos números você vai digitar? "))


vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um número: "))


print("Valores: ", end="")
for i in range(0, n):
    print(f"{vet[i]:.1f} ", end=" ")

soma = 0
for i in range(0, n):
    soma = soma + vet[i]

media = soma / n

print()
print(f"Soma: {soma:.2f}")

print(f"Media: {media:.2f}")
