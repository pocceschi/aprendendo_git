# Se o parâmetro da função for divisível por 2, retorne fizz
# Se for divisivel por 5, retorne buzz
# Se for divisivel por 5 e por 3 retorne FizzBuzz
# caso contrário retorne o número enviado

def funcao(x):
    if x % 2 == 0:
        return "Fizz"
    if (x % 5 == 0) and (x % 3 == 0):
        return "FizzBuzz"
    if x % 5 == 0:
        return "Buzz"
    return x

# eu não preciso fazer o código acima com elif ou else pois se uma
# a primeira condição não for verdadeira, ele irá pular para a próxima.


resultado = funcao(int(input("Digite um número: ")))

if resultado:
    print(resultado)
