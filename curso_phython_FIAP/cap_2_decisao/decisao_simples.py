nome_paciente = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
prioridade = "Não"


if idade >= 65:
    prioridade = "Sim"

print("O paciente" + nome_paciente + " possui atendimento prioritário? " + prioridade)



