cont = 0
for y in range(10):
    num = int(input("Digite Números: "))
    if num < 0:
        cont = cont+1
print(f"Numeros negativos: {cont}")
