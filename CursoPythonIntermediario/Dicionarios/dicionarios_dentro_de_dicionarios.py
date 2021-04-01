# pode criar dicionários dentro de dicionários(filhos):

clientes = {
    "cliente  1" : {
        "nome" : "Pedro",
        "sobrenome" : "Augusto"
    },
    "cliente 2" : {
        "nome" : "Lucas",
        "sobrenome" : "Souza"
    },
    "cliente 3" : {
        "nome" : "Minerva",
        "sobrenome" : "Jack"
    },
}

for clientes, nomes in clientes.items():
    print(f"Exibindo {clientes}")
    for v_cliente, v_nome in nomes.items():
        print(f"\t{v_cliente} = {v_nome}")