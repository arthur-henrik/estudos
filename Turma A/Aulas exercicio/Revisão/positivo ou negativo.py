resp = 's'
while resp == 's':
    num = int(input('diigte um numero para verificação: '))
    if num != 0:
        if num < 0:
            print('o numero digitado é NEGATIVO')
        else:
            print('o numero digitado é POSITIVO')
    else:
        print('o numero não pode ser igual a zero')

    resp = input('deseja realizar outra verificação? s/n: ')

print('xau')
