resp = 's'
while resp == 's':
    num = int(input('diigte um numero para verificação: '))
    if num != 0:
        if num % 2 == 0:
            print('o numero digitado é par')
        else:
            print('o numero digitado é impar')
    else:
        print('o numero não pode ser igual a zero')

    resp = input('deseja realizar outra verificação? s/n: ')
