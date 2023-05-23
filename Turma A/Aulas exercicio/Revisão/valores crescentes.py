num1 = float(input("Escreva um numero: "))
num2 = float(input("Escreva outro numero: "))

if num1 != num2:
    if num1 < num2:
        print(f"{num1}, {num2}")
    else:
        print(f"{num2}, {num1}")
else:
    print("os numeros não podem ser iguais. :D")