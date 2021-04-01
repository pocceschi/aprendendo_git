# para deletar uma chave, usar o comando pop

d1 = {
    1: 2,
    3: 4,
    5: 6,
    7: 8,
}
print(d1)
print()

d1.pop(5) # irá deletar a chave '5' que possui valor 6

print(d1)

print()
#para eliminar a ultima chave, usar .popitem

d1.popitem()
print(d1) # foi deletada a ultima chave '7' com valor 8
