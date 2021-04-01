m = int(input("Você ligou quantos minutos este mês? "))

if m < 200:
    p = m * 0.2
elif (m >= 200) and (m <= 400):
    p = m * 0.18
elif (m > 400) and (m < 800):
    p = m * 0.15
else:
    p = m * 0.8

print(f"O valor da sua conta este mês é de: R${p:.2f}")