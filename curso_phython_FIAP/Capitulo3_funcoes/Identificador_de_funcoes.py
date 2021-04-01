# para criar funcoes, usar o padrao:
# def <identificador de funcao> (<parametro>)
#     <código que será executado>
#     return <dado que será retornado, caso seja necessário>

def preencher_inventario(lista):
    resp="S"
    while resp == "S":
        equipamentos = [input("Equipamento: "),
                  float(input("Valor: ")),
                  input("Serial: "),
                  input("Departamento: ")]
        lista.append(equipamentos)
        resp = input("Digite S para adicionar outro equipamento: ").upper()

def exibir_inventario(lista):
    for elemento in lista:
        print("Equipamento: ", elemento[0])
        print("Valor: ", elemento[1])
        print("Serial: ", elemento[2])
        print("Departamento: ", elemento[3])

def localizar_por_nome(lista):
    busca = input("Digite o equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor: ", elemento[1])
            print("Serial: ", elemento[2])

def depreciar_por_nome(lista, porc):
    depreciar = input("Digite o equipamento a ser depreciado: ")
    for elemento in lista:
        if depreciar == elemento[0]:
            elemento[1] = elemento[1] * (1 - porc / 100)

def excluir_por_serial(lista):
    excluir_serial = input("Digite o serial a ser excluido: ")
    for elemento in lista:
        if excluir_serial == elemento[2]:
            lista.remove(elemento)
    return "Itens excluidos."


def resumir_valores(lista):
    preco = []
    for elemento in lista:
        preco.append(elemento[0])
    if len(preco) > 0:
        print("O equipamento mais caro custa: ", max(preco))
        print("O equipamento mais barato custa: ", min(preco))
        print("O valor somado dos equipamentos é de: ", sum(preco))