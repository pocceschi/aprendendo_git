# para converter tuplas ou listas em dicionarios:

tupla = (
    ("t1", 1),
    ("t2", 2),
    ("t2", 3),
)

lista = [
    ["l1", 4],
    ["l2", 5],
    ["l3", 6],
]

print(tupla, type(tupla))
print(lista, type(lista))

print()

tupla = dict(tupla)
lista = dict(lista)

print(tupla, type(tupla))
print(lista, type(lista))