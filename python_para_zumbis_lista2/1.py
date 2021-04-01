print("Digite os 3 lados de um triângulo: ")
a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if (a > 0 ) or (b > 0) or (c > 0):
    if (a == b) and (b == c):
        print("Triângulo Equilátero")
    elif (a != b) and (b != c) and (c != a):
        print("Trângulo Escaleno")
    else:
        print("Triângulo Isósceles")
else:
    print("A figura não é um triângulo.")