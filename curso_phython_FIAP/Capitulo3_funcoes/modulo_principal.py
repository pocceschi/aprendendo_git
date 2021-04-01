from Capitulo3_funcoes.Identificador_de_funcoes import *

minhaLista = []
print("Preenchendo")
preencher_inventario(minhaLista)
print("Exibindo")
exibir_inventario(minhaLista)

print("Pesquisando")
localizar_por_nome(minhaLista)
print("Alterando")
depreciar_por_nome(minhaLista)

print("Excluindo")
print(excluir_por_serial(minhaLista))
exibir_inventario(minhaLista)

print("Resumindo")
resumir_valores(minhaLista)