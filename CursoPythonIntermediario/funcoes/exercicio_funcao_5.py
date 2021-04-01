# criar uma função1 que recebe uma função 2 como parâmetro
# e retorne o valor da função 2 executada

def func1(x):
    return x

def func2(a, b):
    return a + b


valor = func2(int(input("Digite um valor: ")), int(input("Digite outro valor: ")))
print(func1(valor))
