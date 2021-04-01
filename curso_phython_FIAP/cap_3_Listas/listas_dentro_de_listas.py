lista1 = []

resposta = "S"

while resposta == "S":
    lista2 = [input("Equipamento: "),
              float(input("Valor: ")),
              input("Serial: "),
              input("Departamento: ")]
    lista1.append(lista2)
    resposta = (input("Digite S para adicionar mais equipamentos: ")).upper()

for elemento in lista1:
    print("Equipamento: ", elemento[0])
    print("Valor: ", elemento[1])
    print("Serial: ", elemento[2])
    print("Departamento: ", elemento[3])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for elemento in lista1:
    if busca == elemento[0]:
        print("Serial: ", elemento[2])
        print("Departamento: ", elemento[3])

depreciacao = input("Digite o nome do equipamento a ser depreciado: ")
for elemento in lista1:
    if depreciacao == elemento[0]:
        elemento[1] = elemento[1] * 0.9


serial = input("Digite o serial do equipamento vencido: ")
for elemento in lista1:
    if elemento[2] == serial:
        lista1.remove(elemento)


for elemento in lista1:
    print("Equipamento: ", elemento[0])
    print("Valor: ", elemento[1])
    print("Serial: ", elemento[2])
    print("Departamento: ", elemento[3])

precos = []

for elemento in lista1:
    precos.append(elemento[1])
if len(precos) > 0 :
    print("O equipamento mais caro custa: ", max(precos))
    print("O equipamento mais barato custa: ", min(precos))
    print("O valor somado dos equipamentos é de: ", sum(precos))

