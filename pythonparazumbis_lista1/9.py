km = float(input("Digite a quantidade de quilômetros rodados: "))
dias = int(input("Por quantos dias o carro foi alugado? "))

preco = (60 * dias) + (km * 0.15)

print(f"O preço a pagar pelo aluguel do carro é de: R${preco}")