# pode-se utilizar o while para 'iterar' ou seja
# passar por cada índice de uma string ou variável automaticamente

#indice  0123456789....14
frase = "Bom dia pessoal"
tamanho_frase = len(frase) #funçao len serve para contar o indice da string

contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador) # nesta linha eu mando imprimir a letra correspondente ao indice lido
    contador += 1 # += 1 é a mesma coisa que contador = contador + 1