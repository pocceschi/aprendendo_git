while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if (nota > 0) and (nota < 10):
        break
    else:
        nota = float(input("Valor inválido. Digite uma nota entre 0 e 10: "))