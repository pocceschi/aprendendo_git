# **kwargs (com dois * mesmo, kwargs é nome por convenção e pode ser trocado)
# é utilizado para desempacotar argumentos que contenha palavras

def func(*args, **kwargs):
    print(args)
    print(kwargs["nome"], kwargs["sobrenome"]) #definir quais variáveis quer imprimir, no caso nome e sobrenome

variavel = [10, 20, 30]

variavel2 = [40, 50, 60]

func(*variavel, *variavel2, nome="Pedro", sobrenome="Augusto")

#irá imprimir:
#(10, 20, 30, 40, 50, 60) (este por conta do args)
#Pedro Augusto (este por conta do kwargs)