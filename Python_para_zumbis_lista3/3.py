a = 80000
b = 200000
anos = 0

while True:
    a = a + (a * 3) / 100
    b = b + (b * 1.5) / 100
    anos = anos + 1
    if a >= b:
        break

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.")