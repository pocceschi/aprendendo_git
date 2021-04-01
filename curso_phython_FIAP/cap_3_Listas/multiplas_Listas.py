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

for indice in range(0,len(equipamento)):
    print("Equipamento: ", (indice+1))
    print("Nome: ", equipamento[indice])
    print("Valor: ", valor[indice])
    print("Serial: ", serial[indice])
    print("Departamento: ", departamento[indice])


busca_eq = "S"

while busca_eq == "S":
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for indice in range(0,len(equipamento)):
        if busca == equipamento[indice]:
            print("Valor: ", valor[indice])
            print("Serial: ", serial[indice])
    busca_eq = input("Digite S para buscar outro equipamento: ").upper()