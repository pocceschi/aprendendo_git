# Crie uma função que receba 2 números. O primeiro é um valor e o segundo
# é um percentual (ex. 10%). retorne (return) o valor do primeiro número somado
# do aumento do percentual do mesmo.

def conta(x, y):
    return ((x * y) / 100) + x

result = conta(int(input("Digite um valor: ")), int(input("Digite um percentual: ")))
print(f"O valor somado ao percentual é de: R${result:.2f}")