ips = {}

resp = "S"

while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois ultimos octetos: "))] = input("Nome da máquina: ")
    resp = input("Digite <S> para continuar: ").upper()

print("Exibindo ip's: ")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])

#print("Exibindo máquinas com o mesmo endereço: ")
#pesquisa = input("Digite os dois ultimos octetos: ")

#for ip, nome in ips.items():
    #print("Máquinas com o mesmo endereço (redes diferentes)")
    #if (ip[1] == pesquisa):
       # print(nome)


pesquisa_ip = input("Para listar as máquinas na rede, digite os dois primeiros octetos do IP: ")

for ip, nome in ips.items():
    if ip[0] == pesquisa_ip:
        print("Maquinas na rede: ")
        print(nome)
