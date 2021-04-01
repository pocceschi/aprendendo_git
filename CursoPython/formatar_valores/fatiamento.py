# a string pode ser fatiada
# para isso, utilizar entre as chaves o índice inicial : índice final
# ex:
# indice  012345
string = "Barata"

#quero imprimir o 'ra' (indice 2 e 3)
#para isso, colocar entre chaves [2:4] - o 4 não será lido, somente 2 e 3

string_formatada = string[2:4]
print(string_formatada)

#irá imprimir 'ra'
#caso eu queria imprimir do início até um certo índice, colocar :indice
#ex:
#quero imprimir do ínicio até a terceira letra

nova_string = string[:4]
print(nova_string)
#irá imprimir 'Bara'

#caso eu queira imprimir somente o final, utilizar [3:] irá imprimir do indice 3 pra frente

nova_string2 = string[4:]
print(nova_string2)
#irá imprimir 'ta'

#caso eu queria trabalhar com o índice negativo, pensar nas posiçoes como:
# indice  -654321
#string = "Barata"

#se eu quiser imprimir o 'Ba' então seria [-6:-4]
nova_string3 = string[-6:-4]
print(nova_string3)
#irá imprimir o 'Ba'

#se eu quiser imprimir 'arata' [-5:]
nova_string4 = string[-5:]
print(nova_string4)
#irá imprimir 'arata'

#pode-se ainda imprimir saltando os índices
#para isso, utilizar as chaves informando o salto
#ex: quero imprimir 'Almondega' mas saltando 1 indice:

#indice     012345678
string_a = "Almondega" # 0 é o inicio, 9 final e 2 é quanto deve saltar
string_a_formatada = string_a[0:9:2]
print(string_a_formatada)
#irá imprimir 'Amnea' ou seja, saltou as letras L O D G
#se eu quiser ir do início até o final da string, poderia ser também
#[0::2] - ou seja do índice inicial '0' até o final saltando 2