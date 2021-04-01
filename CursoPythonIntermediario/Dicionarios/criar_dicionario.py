# dicionários são similares a listas, possuem indices e valores
# a diferença é que os índices são controlados pelo usuário
# para criar um dicionário é necessário informar a chave(indice) e o valor
# strings, números inteiros e tuplas podem ser chaves
# qualquer informação pode ser valor para as chaves (str, int, boolean, float, etc) 

d1 = {"chave1":"Valor da chave"} # para criar um dicionário

# ou

d2 = dict(indice0="Indice 0", indice1=10)

print(d1)
print(d2)

d1["nova_chave"] = "Valor da nova chave" # para adicionar nova chave
d2["indice2"] = 30

print(d1)
print(d2)

print(d1["nova_chave"]) # caso eu queria imprimir um valor específico
print(d2["indice2"])

