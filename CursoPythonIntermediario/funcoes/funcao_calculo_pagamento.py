# exemplo de um uso para função:

def calcular_pagamento(qtd_horas, valor_hora):
    qtd_horas = float(qtd_horas)
    valor_hora = float(valor_hora)
    if qtd_horas <= 40:
        salario = qtd_horas * valor_hora
    else:
        h_excd = qtd_horas - 40
        salario = 40 * valor_hora + (h_excd * (1.5 * valor_hora))
    return salario


n_funcionarios = int(input("Digite a quantidade de funcionários: "))

c = 0

while c < n_funcionarios:
    c = c + 1
    a_receber = calcular_pagamento(int(input("Digite a quantidade de horas: ")), int(input("Digite o valor recebido por hora: ")))
    print(f"O funcionário {c} irá receber R${a_receber:.2f}")



