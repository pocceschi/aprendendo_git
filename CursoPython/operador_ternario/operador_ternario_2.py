# outro exemplo de uso:

idade = input("Digite a sua idade.")

if not idade.isnumeric():
    print("Você precisa digitar apenas números.") # Verif. se o valor digitado para idade é numérico e inteiro.
else:
    idade = int(idade)

check_idade = (idade >= 18) # nesta linha ocorre a verif. se o usuário é maior de 18. Se sim, o valor será True.
msg = "Pode acessar." if check_idade else "Não pode acessar."

print(msg)