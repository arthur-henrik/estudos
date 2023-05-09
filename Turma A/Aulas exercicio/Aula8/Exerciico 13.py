numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'resolução do item 1 do exercicio 13.'

for a in range(10):
    numeros.append(int(input('digite numeros: ')))

for b in range(10):
    if numeros[b] % 2 == 0:
        print(numeros[b])

v_maior = numeros[0]
for c in range(10):
    if numeros[c] > v_maior:
        v_maior = numeros[c]

v_menor = numeros[0]
for d in range(10):
    if numeros[c] < v_menor:
        v_menor = numeros[d]

soma = 0
for e in range(10):
    soma += numeros[e]
media = soma / 10

cont = 0
for f in range(10):
    if media < numeros[f]:
        cont += 1
print(cont)

