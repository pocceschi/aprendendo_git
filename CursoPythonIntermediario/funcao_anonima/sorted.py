# Outra forma de ordenar uma lista é a função sorted
# no caso irá ordenar imprimindo já:

lista = [["P1", 10], ["P2", 574], ["P3", 204], ["P4", 24], ["P5", 154]]

print(sorted(lista, key=lambda i: i[1]))

# ou do maior para o menor:

lista2 = [["P1", 10], ["P2", 574], ["P3", 204], ["P4", 24], ["P5", 154]]

print(sorted(lista2, key=lambda i: i[1], reverse=True))