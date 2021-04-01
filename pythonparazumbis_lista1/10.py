qtc = int(input("Quantos cigarros você fuma por dia? "))
a = int (input("Por quantos anos você fuma? "))

t = (qtc * a * 365 * 10) / 1440

print(f"O fumante perdeu {t:.1f} dias de vida.")