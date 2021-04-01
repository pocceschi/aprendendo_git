# a expressão lambda é utilizada como uma função anônima
# sua utilização pode ser no caso do exemplo da função sort, ao invés de definir
# uma função para escolher qual argumento será o ordenador, pode-se utilizar a função anonima lambda.
# no exemplo anterior do arquivo lista_sort por exemplo, para ordenar com a expressão lambda ficaria:

lista = [["P1", 10], ["P2", 574], ["P3", 204], ["P4", 24], ["P5", 154]]

lista.sort(key=lambda item: item[1])

print(lista)

#ou para ordenar do maior para o menor:

lista2 = [["P1", 10], ["P2", 574], ["P3", 204], ["P4", 24], ["P5", 154]]

lista2.sort(key=lambda item: item[1], reverse=True)

print(lista2)