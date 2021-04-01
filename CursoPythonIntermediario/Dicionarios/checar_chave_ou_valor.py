# para checar se um dicionário possui uma chave ou um valor:
# o dicionário abaixo possui 3 chaves, uma chave com str, uma com
# inteiro e outra com tupla.

d1 = {
    "str" : "abcde",
    1 : 100154,
    (1,2,3,4) : "tupla"
}

if "str" in d1: # verificação se há a chave com nome "str"
    print(d1["str"]) #caso True, imprime valor

# ou

while 1 in d1: # pode verificar com while também
    print(d1[1])
    break  # mas lembrando de usar o break kkkk

# para apenas saber se existe uma chave ou um valor:

print((1,2,3,4) in d1) # irá imprimir True pois existe uma chave 1,2,3,4

print("tupla" in d1.values()) # irá imprimir True pois existe valor "tupla" em uma das chaves