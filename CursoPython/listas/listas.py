# para adionar uma lista (vetor) usar chaves.
# o conteúdo da lista pode ser escrito (hardcode) ou atribuido
#a variáveis

lista = [1,2,3,4,5,6,]

print(lista)

print()

# ou
n = input("Digite um valor para n: ")
m = input("Digite um valor para m: ")
lista2 = [n,m]

print(lista2)

print()

# ao inves de digitar os números um a um (hardcode), pode-se usar
#o comando list(range):


lista3 = list(range(1,20))
print(lista3)

#no caso acima a lista 3 vai receber os valores de 1 a 19.

#caso eu queria fazer uma lista mas com valores não continuos
#(2 em 2 ou 3 em 3 ou -1 em -1) usar list(range(1,20,2) ou
#list(range(1,20,3) ou list(range(1,20,-1)
#ex:

print()

lista4 = list(range(20,1,-1))
print(lista4)
