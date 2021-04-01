while True:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    if usuario != senha:
        break
    else:
        print("O usuário não pode ser igual a senha.")