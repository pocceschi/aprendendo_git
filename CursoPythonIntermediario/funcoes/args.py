# a função *args (usar a exclamação mesmo, args é usado por convenção mas pode ser qualquer palavra)
# é utilizada para desempacotar argumentos em uma função definida
# ex abaixo com e sem o *args:

def func(*x):
    print(x)


variavel = [10, 20, 30]


variavel2 = [40, 50, 60]


func(variavel, variavel2)
#desta forma sem o * está imprimindo como se fossem duas listas:
#([10, 20, 30], [40, 50, 60])

func(*variavel, *variavel2)
#desta forma com o * imprime os argumentos juntos, formando uma só lista
#(10, 20, 30, 40, 50, 60)

func(*variavel, 70, 80, 90)
#desta forma também funciona, os valores se juntam em uma lista