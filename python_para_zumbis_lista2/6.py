gh = int(input("Quanto você ganha por hora? "))
hm = int(input("Quantas horas você trabalha por mês? "))

sb = gh * hm

ir = (sb * 11) / 100
inss = (sb * 8) / 100
sindicato = (sb * 5) / 100

sl = sb - ir - inss - sindicato

print(f"O salário bruto é de: R${sb:.2f}")
print(f"Foi descontado R${ir:.2f} de Imposto de Renda")
print(f"Foi descontado R${inss:.2f} de INSS")
print(f"Foi descontado R${sindicato:.2f} de Sindicato")
print(f"O salário líquido é de: R${sl:.2f}")
