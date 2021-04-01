# para iterar é mais fácil com o comando for
# para isso basta usar o comando for e in
# a variavel 'exemplo' usada para imprimir os indices não precisa ter
#valor atribuido.

texto = "Pedro"

for exemplo in texto:
    print(exemplo)


print()

# no codigo acima vai imprimir letra a letra de "Pedro".
#caso eu queira que mostre o indice também, posso usar o comando
#"enumerate" conforme o exemplo abaixo:



for n, exemplo in enumerate(texto):
    print(n, exemplo)