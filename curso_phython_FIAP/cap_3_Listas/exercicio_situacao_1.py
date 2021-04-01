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


depreciar = "S"

while depreciar == "S":
    busca_equipamento = input("Digite o nome do equipamento que quer buscar: ")
    for indice in range(0,len(equipamento)):
        if busca_equipamento == equipamento[indice]:
            valor[indice] = valor[indice] - (valor[indice] * 0.10)
            print("O novo valor após depreciamento é de: ", valor[indice])
    depreciar = input("Digite S para depreciar outro equipamento: ").upper()
