# para inverter valor de variáveis no Python fazer:

x = 10
y = "Hoje"

x, y = y, x

#no código acima eu modifiquei o valor das varíaveis com o sinal
#de "=" trocando a posição das mesmas.

print(x)
print(y)

# x virou "Hoje" e y virou "10"

# funciona com mais de duas variáveis também:

a = 1
b = 2
c = 3

a, b ,c = b, c, a

print (a, b, c)

# imprimiu 2, 3, 1