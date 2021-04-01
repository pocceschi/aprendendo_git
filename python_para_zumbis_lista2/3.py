peso = float(input("Qual o peso dos peixes? "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"Excesso: {excesso:.2f} KG.")
    print(f"Multa: R${multa:.2f}.")
else:
    excesso = 0
    multa = 0
    print(f"Excesso: {excesso:.2f} KG.")
    print(f"Multa: R${multa:.2f}.")