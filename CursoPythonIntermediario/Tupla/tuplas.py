# tuplas são como listas (vetores) mas seus elementos não podem ser
# alterados e nem pode-se adicionar mais elementos.
# para adicionar uma tupla, basta informar seus elementos

t1 = 1, 2, 3, "Pedro", "Minerva"

for v in t1:
    print(v) # pode-se iterar os elementos das tuplas

print(t1, type(t1))

t2 = 1, #para criar uma tupla com um elemento apenas, criar a varíável com uma ,

print(t2, type(t2))

t3 = t1 + t2 #pode-se juntar os valores (concatenar) uma tupla
print(t3, type(t3))