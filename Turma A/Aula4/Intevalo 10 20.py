dentro = 0
fora = 0
for e in range(10):
    num = float(input("Digite um numero: "))
    if num >=10 and num <= 20:
        dentro +=1
    else:
        fora +=1
print(f"Numeros digitados entre 10 e 20: {dentro}")
print(f"Numeros digitados fora de 10 e 20: {fora}")