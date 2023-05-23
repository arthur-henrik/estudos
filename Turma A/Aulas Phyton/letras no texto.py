def letras(t):
    cont = 0
    for letra in t:
        if letra != " ":
            cont += 1
    print(cont)
texto = "O rato roeu a roupa do rei de roma"
letras(texto)
