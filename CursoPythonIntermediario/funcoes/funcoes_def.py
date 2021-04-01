# def serve para definir uma função. Desta forma você pode chamar
# a função ao invés de digita-la novamente.

def funcao():
    print("Teste.")

funcao()
funcao()

print()

# chamando a função: funcao() eu posso rodar a função repetidas vezes
# com apenas esta linha de código.

def funcao2():
    a = 2 + 5
    print(a)

funcao2()

print()

def saudacao(msg="Olá", nome="usuário"):
    print(msg, nome)

saudacao() #a função com apenas os parenteses sem nada, irá imprimir o valor padrão

saudacao("Oi", "Pedro") #a função com os valores irá trocar o valor padrão para o que eu colocar