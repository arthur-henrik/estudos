senhaa = "eitchola"
cont_senha = 1

senha = str(input("digite sua senha: "))

while senha != senhaa:
    cont_senha = cont_senha + 1
    senha = str(input("senha incorreta, tente novamente: "))
    if cont_senha > 2 and senha != senhaa:
        print("SENHA BLOQUEADA")
        break
else:
    print("olá amigo")
