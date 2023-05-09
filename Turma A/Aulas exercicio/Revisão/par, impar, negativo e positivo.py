resp = 'sS'
while resp in 'sS':
    num = int(input('diigte um numero para verificação: '))
    if num % 2 == 0:
        if num > 0:
            print('o numero digitado é PAR e POSITIVO')
        else:
            print('o numero digitado é PAR e NEGATIVO')
    else:
        if num > 0:
            print("o numero é IMPAR e POSITIVO")
        else:
            print("o numero é IMPAR e NEGATIVO")

    resp = input('deseja realizar outra verificação? s/n: ')