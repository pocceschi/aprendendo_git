# para formatar mais de uma string, utilizar o comando format
# ex: formatar nome e sobrenome para ter 20 caracteres cada

nome = "Pedro"
sobrenome = "Augusto"

nome_formatado = "{0:@>20} {1:#<20}".format(nome,sobrenome)
print(nome_formatado)

# irá sair: @@@@@@@@@@@@@@@Pedro Augusto#############
# o comando {0:@>20} refere-se a primeira varíavel (nome)
# o comando {1:#<20} a segunda varíavel (sobrenome)