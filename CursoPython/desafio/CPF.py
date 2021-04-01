cpf = str(input("Digite um CPF sem os digitos validadoes (ultimos 2 digitos): "))
soma = 0
cont = 10

for iterar in cpf:
    iterar = int(iterar)
    if cont >= 2:
        soma = soma + (iterar * cont)
    cont -= 1

validador_digito_1 = 11 - (soma % 11)

if validador_digito_1 > 9:
    validador_digito_1 = 0

print(f"O dígito validador 1 é: {validador_digito_1}")

cont2 = 11
soma2 = 0

cpf = str(cpf)
validador_digito_1 = str(validador_digito_1)

cpf2 = cpf + validador_digito_1

for iterar2 in cpf2:
    iterar2 = int(iterar2)
    if cont2 >= 2:
        soma2 = soma2 + (iterar2 * cont2)
    cont2 -= 1

validador_digito_2 = 11 - (soma2 % 11)

if validador_digito_2 > 9:
    validador_digito_2 = 0

print(f"O dígito validador 2 é: {validador_digito_2}")




