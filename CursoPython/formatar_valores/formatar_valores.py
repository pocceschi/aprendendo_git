# :s - texto (sting)
# :d - inteiro (int)
# :f - número com ponto flutuante (float)
# em caso de formatar a variável posso fazer {variavel:.2f} o 2f quer dizer duas casas decimais
# para formatar com números antes, depois ou entre as variáveis fazer:
# print(f"{variavel:0>5}") para adicionar antes da variável: 0000variavel
# print(f"{variavel:0<5}") para adicionar depois da variável: variavel0000
# print(f"{variavel:0^30}") para adicionar antes e depois da variável: 00000000Pedro Augusto000000000

nome = "Pedro Augusto"

print(f"{nome:0^30}")

