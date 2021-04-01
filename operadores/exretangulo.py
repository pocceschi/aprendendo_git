b = float(input("Base do retangulo: "))
a = float(input("Altura do retangulo: "))

area = float(a*b)
perimetro = float(a+a+b+b)
diagonal = float((a**2 + b**2) ** 0.5)

print(f"Area: {area:.4f}")
print(f"Perimetro: {perimetro:.4f}")
print(f"Diagonal: {diagonal:.4f}")

