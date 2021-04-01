# a funcao sort pode ser utilizada para ordernas uma lista
# a lista tem de estar dentro de outra lista, caso contrário será interpretado como tuple
# no exemplo foi criada esta lista com dois argumentos. O argumento 0 é o nome do produto e o 1 o valor do produto.

lista = [["P1", 10], ["P2", 574], ["P3", 204], ["P4", 24], ["P5", 154]]

def func(item):
    return item[1]
# necessário definir a funcao informando qual indice deverá ser utilizado, no caso foi o indice [1] dos valores

lista.sort(key = func)

print(lista)

# será impressa a lista ordenada pelos valores do indice 1, ou seja, os valores dos produtos (indice 0 é o nome do produto e o 1 o valor do produto)

lista2 = [["P1", 10], ["P2", 574], ["P3", 204], ["P4", 24], ["P5", 154]]

lista2.sort(key = func, reverse=True)

print(lista2)

#para ordenar do maior para o menor, usar na função sort o reverse=True