h = float(input("Digite um horário: "))

if (h >= 0) and (h <= 11):
    print("Bom dia!")
elif (h >= 12) and (h <= 17):
        print("Boa tarde!")
else:
    print("Boa noite!")
