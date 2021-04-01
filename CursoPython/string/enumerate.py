# a função enumerate é utilizada para enumerar os elementos da lista
# no caso iterar e contar

a = "Café é muito bom."
lista = a.split(" ")

# no comando abaixo, a variável indice será o contador e a varíavel
# valor será o elemento do vetor
for indice, valor in enumerate(lista):
    print(indice, valor)