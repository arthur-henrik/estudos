def vogal(t):
    cont = 0
    for voga in t:
        if voga in 'aeiouAEIOU':
            cont += 1
    print(cont)
texto = "O rato roeu a roupa do rei de roma"
vogal(texto)
