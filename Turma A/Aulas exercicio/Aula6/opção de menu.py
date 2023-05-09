num1 = float(input("digite o 1° numero: "))
num2 = float(input("digite o 2° numero: "))

menu = ("""\npor favor escolha uma opção: 
[1] somar os numeros.
[2] subtrair os numeros.
[3] multiplicar os numeros.
[4] dividir os numeros
[5] digitar um novo numero.
[6] sair

""")

while True:
    escolha = int(input(menu))

    if escolha == 1:
        print(f"{num1+num2}")
    elif escolha == 2:
        print(f"{num1-num2}")
    elif escolha == 3:
        print(f"{num1*num2}")
    elif escolha == 4:
        print(f"{num1/num2}")
    elif escolha == 5:
        num1 = float(input("digite o 1° numero: "))
        num2 = float(input("digite o 2° numero: "))
    elif escolha == 6:
        print("até breve")
        break
