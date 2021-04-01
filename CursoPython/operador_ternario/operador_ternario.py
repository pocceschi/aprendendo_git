# esta função serve para encurtar os códigos.
# por exemplo, para checar se um usuário está logado seria:

logged_user = False

if logged_user:
    msg = "O usuário está logado."
else:
    msg = "Favor realizar loggin."

print(msg)

# para encurtar, posso fazer:

logged_user2 = True
msg2 = "O usuário está logado." if logged_user2 else "Favor realizar loggin."

print(msg2)