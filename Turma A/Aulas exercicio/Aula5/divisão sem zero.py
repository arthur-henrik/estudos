num1 = float(input("digite um numero: "))
num2 = float(input("digite o segundo numero: "))

while num2 == 0:
    num2 = float(input("Numero 0 é invalido, digite outro numero: "))
resultado = num1 / num2
print(resultado)
