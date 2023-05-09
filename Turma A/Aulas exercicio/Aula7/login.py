login = []
senha = []
print("""
[1] Login
[2] Cadastar um novo usuário
[3] Alterar senha
[4] Sair 
""")
escolha = input('digite uma opção: ')

if escolha != '1234':
    if escolha == 1:
        for a in range(1):
            login.append(input("digite seu login: "))
            senha.append(input("digite sua senha: "))

            print("Login e senhas criados.")

    #if escolha == 2:
        #login_confirma = input("digite seu login para entrar: ")
        #senha_confirma = input("agora, digite sua senha: ")

    #if login_confirma in login and senha_confirma in senha:
        #print("usuario validado corretamente, bom jogo.")
#else:
#print("vaza daqui meu")
