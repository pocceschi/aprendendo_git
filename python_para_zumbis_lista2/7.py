m2 = float(input("Quantos metros quadrados serão pintados? "))

if m2 % 54 == 0:
    latas =  m2 / 54
else:
    latas = int(m2 / 54) + 1


print(f"Latas necessárias: {latas}")
print(f"Valor à pagar: R${latas * 80:.2f}")

