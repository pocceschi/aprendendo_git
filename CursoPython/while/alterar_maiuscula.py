# posso iterar na função while para por exemplo trocar uma letra
# para maíusculo automaticamente

frase = "bom dia beus abigos"
tamanho_frase = len(frase)
contador = 0
frase_corrigida = "" # a frase corrigida inicialmente é declarada vazia
# também será necessário usar outra variável, mas não é necessário
# declarar esta. No caso será a variável 'letra'.

print(frase)

tornar_maiuscula = input("Qual letra você quer tornar maiúscula? ")

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == tornar_maiuscula:
        frase_corrigida += tornar_maiuscula.upper()
    else:
        frase_corrigida += letra
    contador += 1

print(frase_corrigida)