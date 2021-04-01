# para imprimir somente os valores do dicionário:

d1 = {
    "chave1" : 1234,
    "chave2" : "abcde",
    "chave3" : 100.57,
    "chave4" : (5, 4, 1, 5, 4),
}

for v in d1.values():
    print(v) # irá imprimir os valores de todas as chaves

# para um valor especifico:

print()

print(d1["chave2"])
print(d1["chave3"])

print()

# para imprimir as duplas:

for k in d1.items():
    print(k)

print()

# para imprimir as duplas separadamente:

for i, j in d1.items():
    print(i, j)