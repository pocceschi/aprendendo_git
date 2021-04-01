# para copiar um dicionário sem possibilidade de alteração em ambos, usar o comando
# copy.deepcopy()
# o primeiro passo é importar o modo copy com o comando import copy

import copy

d1 = {1: "a", 2: "b", 3: "c", 4: "d"}
v = copy.deepcopy(d1)

print(d1)
print(v)

print()
#alteração somente no dicionario d1:
d1[1] = "J"

print(d1)
print(v)

#dicionario V continua da mesma forma, não foi alterado pois é uma cópia profunda