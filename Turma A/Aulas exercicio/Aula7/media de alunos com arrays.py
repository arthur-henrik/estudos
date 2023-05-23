notas = []

for x in range(5):
    notas.append(float(input(f"digite as nota do aluno: ")))

soma = 0
for y in range(5):
    soma += notas[y]
media = soma / 5
print(media)

cont = 0
for z in range(5):
    if notas[z] >= media:
        cont += 1

        print(cont)


