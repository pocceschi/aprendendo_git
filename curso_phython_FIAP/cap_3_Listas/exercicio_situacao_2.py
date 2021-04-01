equipamento = []
valor = []
serial = []
departamento = []

continuar = "S"

while continuar == "S":
    equipamento.append(input("Informe o equipamento: "))
    valor.append(float(input("Digite o valor do equipamento: ")))
    serial.append(input("Digite o serial do equipamento: "))
    departamento.append(input("Digite o departamento: "))
    continuar = input("Digite S caso queria continuar: ").upper()



del_serial = "S"

verificar_serial = input("Digite o serial do equipamento vencido: ")
for indice in range(0,len(equipamento)):
    if serial[indice] == verificar_serial:
        del equipamento[indice]
        del valor[indice]
        del serial[indice]
        del departamento[indice]
        break


for indice in range(0,len(equipamento)):
    print("Equipamento: ", (indice+1))
    print("Nome: ", equipamento[indice])
    print("Valor: ", valor[indice])
    print("Serial: ", serial[indice])
    print("Departamento: ", departamento[indice])


