salario = float(input("Digite o salário atual: "))
porcen = float(input("Digite o percentual de aumento: "))

nsalario = ((salario * porcen) / 100) + salario

print(f"O novo salário é de: R${nsalario:.2f}")