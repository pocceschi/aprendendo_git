# Melhorar o código multiplas_listas do capítulo 3:

dic = {}

resp = "S"

while resp == "S":
    equipamento = input("Digite o nome do equipamento: ")
    dic[equipamento] = [
        float(input("Digite o valor do equipamento: ")),
        input("Digite o serial do equipamento: "),
        input("Digite o departamento: ")]
    resp = input("Digite <S> Para continuar: ").upper()


print(dic)


deseja_buscar = "S"

while deseja_buscar == "S":
    busca_equip = input("Digite o equipamento que deseja buscar: ")
    for chave, valor in dic.items():
            if chave == busca_equip:
                print("Equipamento: ", chave)
                print("Valor: ", valor[0])
                print("Serial: ", valor[1])
                print("Departamento: ", valor[2])
    deseja_buscar = input("Digite <S> para buscar outro equipamento ou <N> para sair: ").upper()