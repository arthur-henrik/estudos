login = []
senha = []
for a in range(5):
    login.append(input('digite seu login: '))
    senha.append(input('digite sua senha: '))
    print('usuario e senha criados.')

print('Area de Login')

login_entrar = input('Digite o Ususario: ')
senha_entrar = input('digite sua seenha: ')

cont = 0
for b in range(5):
    if login_entrar == login[b] and senha_entrar == senha[b]:
        print('Bem Vindo, {} Chega pro baile!'.format(login_entrar))
        break
    else:
        cont = cont + 1
if cont == 5:
    print('digita o login e senha certo, minha fera !!!')

