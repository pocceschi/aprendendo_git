vm = float(input("Digite o valor da mercadoria: "))
pd = float(input("Digite o percentual de desconto: "))

desc = (vm * pd) / 100
pap = vm - desc

print(f"O desconto é de: R${desc:.2f}")
print(f"O preço à pagar é de: R${pap:.2f}")


