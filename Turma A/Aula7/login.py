login = []
senha = []
for a in range(1):
    login.append(input("digite seu login: "))
    senha.append(input("digite sua senha: "))
    print("Login e senhas criados.")

login_confirma = input("digite seu login para entrar: ")
senha_confirma = input("agora, digite sua senha: ")

if login_confirma in login and senha_confirma in senha:
    print("usuario validado corretamente, bom jogo.")
else:
    print("vaza daqui meu")