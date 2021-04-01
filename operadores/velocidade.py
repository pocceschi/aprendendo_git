v = int(input("Qual a velocidade do carro? "))

if v > 110:
    p = (v - 110) * 5
    print(f"Você foi multado! O valor da multa é de: R${p:.2f}")
else:
    print("Você estava dentro do limite de velocidade e não foi multado.")