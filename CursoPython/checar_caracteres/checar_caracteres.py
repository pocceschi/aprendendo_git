usuario = input("Digite o usuário: ")
qtd_caracteres = len(usuario)

if qtd_caracteres >= 8:
    print("Usuário cadastrado no sistema.")

# No exemplo estou checando se o usuário possui pelo menos 8 caracteres.
# Caso não tenha, será solicitado digitar o usuário novamente.

while qtd_caracteres < 8:
    print("O usuário possui menos de 8 caracteres. Favor digitar novamente.")
    usuario = input("Digite o usuário: ")
    qtd_caracteres = len(usuario)
    if qtd_caracteres >= 8:
        print("Usuário cadastrado no sistema.")
