medias = []
resp = 's'
while resp == 's':
    num1 = float(input('digite um numero: '))
    num2 = float(input('digite outro numero: '))
    media = (num1 + num2) / 2
    print(media)

    if media >= 7:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
    medias.append(media)
    resp = input('deseja iniciar um novo calculo? - s/n: ')
    print(medias)
