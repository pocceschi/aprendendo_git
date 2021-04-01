# criar uma função1 que recebe uma função 2 como parâmetro
# e retorne o valor da função 2 executada
# faça a função 1 executar duas funções que recebam um número diferente
# de argumentos.

def func1(x):
    return x

def func2(a, b):
    return a + b

def func3(c, d):
    return c - d

valor = func2(int(input("Digite um valor: ")), int(input("Digite outro valor: ")))
valor2 = func3(int(input("Digite um valor: ")), int(input("Digite outro valor: ")))



print(func1(valor * valor2))