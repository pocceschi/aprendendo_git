def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


resultado = divisao(int(input("Digite um número: ")), int(input("Digite outro número: ")))

if resultado:
    print(resultado)
else:
    print("Conta inválida.")
