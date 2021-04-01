d = int(input("Digite a quantidade de dias: "))
h = int(input("Digite a quantidade de horas: "))
m = int(input("Digite a quantidade de minutos: "))
s = int(input("Digite a quantidade de segundos: "))

total = s + (m * 60) + (h * 3600) + (d * 86400)

print(f"O usuário tem um total de {total} segundos")

