# para copiar um dicionario, usar o comando .copy()
# se vc apenas atribuir o dicionário a uma varíavel, eles serão identicos

d1 = {1: ["a", "J"], 2: "b", 3: "c"}
v = d1

v[2] = "D"

print(d1)
print(v)

# no caso acima, quando alterei o indice 2 alterou para os dois
# pois eles utilizam a mesma posição na memória

# para copiar apenas os valores sem ser o mesmo dicionário:

c = d1.copy()

c[2] = "J"
print(c)

# Com o comando copy() os valores do dicionario 'd1' foram copiados para o 'c'
# mas eles permaneceram dicionários diferentes sendo possível alterar um sem mudar o outro

# neste tipo de copia, se o valor de um indice do dicionário for alterado, irá altera no outro também

v[1][1] = "Exemplo"
# estou alterando a chave 1, indice 0 ou seja '1: "a"' para '1: "Exemplo"'

print(v)
print(c) # na chave 1, indice 1 que era J foi atlerado para Exemplo até mesmo no dicionário C que foi copiado.

