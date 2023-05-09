lista_num = []

processo = int(input('Qauntas vezes você quer repetir a digitação dos numeros?: '))

for numeros in range(1, processo+1):
    lista_num.append(float(input(f'digite o numero para pesquisar se tem numeros iguais: ')))

numero = float(input('digite um numero para verificação: '))

cont = 0
for a in range(processo):
    if numero == lista_num[a]:
        cont += 1
print(f'o numero digitado tem {cont} valores iguais no vetor.')
