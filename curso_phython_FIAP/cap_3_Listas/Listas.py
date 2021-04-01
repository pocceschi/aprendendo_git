# lista preenchida estaticamente: valores inputados ao criar a lista:

lista_estatica = ["Exemplo", True]
lista_estatica2 = ["João", 1]


# lista preenchida dinamicamente: valores serão inputados na lista ao rodar o programa:

lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))]
# no exemplo acima é necessário converter o valor de str para int para só depois converter para boolean. Não há como converter str para boolean.
lista_dinamica2 = [input("Digite um usuário: "), int(input("Digite a idade do usuário: "))]

print(lista_dinamica)
print()
print(lista_dinamica2)

# lista vazia:

lista_vazia = []