def perguntar():
    perguntar = input("Escolha uma ação para o sistema:"
                  + "Digite <I> para Inserir"
                  + "Digite <P> para Pesquisar"
                  + "Digite <E> para Excluir"
                  + "Digite <L> para Listar"
                  + "Digite <S> para Sair"
                  ).upper()
    return perguntar


def inserir(dicionario):
    verif_chave = input("Digite o código do lançamento: ").upper()
    while verif_chave in dicionario:
        print("Já existe um login com este código.")
        verif_chave = input("Digite o código do lançamento: ").upper()
    dicionario[verif_chave] = [input("Login do usuário: ").upper(),
                               input("Nome do usuário: ").upper(),
                               input("Horário do acesso: "),
                               input("Data do ultimo acesso: "),
                               input("Ultima estação acessada: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Login: " + lista[0])
        print("Nome: " + lista[1])
        print("Horário ultimo acesso: " + lista[2])
        print("Data último acesso: " + lista[3])
        print("Última estação: " + lista[4])


def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Eliminado.")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Código do lançamento: ", chave)
        print("Dados: ", valor)