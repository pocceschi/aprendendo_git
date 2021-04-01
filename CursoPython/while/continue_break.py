# pode-se utilizar a função continue para saltar durante o while
# e break para parar o código

# ex:

x = 0
while x < 10:
    if x == 5:
        x = x + 1 # é necessário colocar novamente o contador se não bugga
        continue
    print(x)
    x = x + 1
# no código acima imprimiu de 0 a 9 saltando o 5 pois eu informei no
# código que se o x for igual a 5 deve saltar (função continue)


# Eu posso também parar o código usando a função break

print()

y = 0
while y < 10:
    if y == 7:
        y = y + 1
        break
    print(y)
    y = y + 1

# neste código acima imprimiu até 6 pois eu disse no código
# que deve fazer break se o Y for igual a 7