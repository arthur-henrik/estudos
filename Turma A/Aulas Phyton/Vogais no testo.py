texto = 'O rato roeu a roupa do rei de roma'
cont = 0

for vog in texto:
    if vog in 'aeiouAEIOU':
        cont += 1
print(cont)
