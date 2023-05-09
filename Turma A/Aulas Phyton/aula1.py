def somar(a, b):
    return a+b

def subitrair(a, b):
    subtra = 0
    subtra = a-b
    return subtra

def dividir(a, b):
    divisao = 0
    divisao = a/b
    return divisao

def multiplicar(a, b):
    multipl = 0
    multipl = a*b
    return multipl

while True:
    print("""
    [1] Somar
    [2] Subtrair
    [3] Dividir
    [4] Multiplicar
    [5] Sair
    """)

    menu = int(input("digite a função do MENU: "))
    if menu == 5:
        print("xau e bença")
        break
    elif menu < 1 or menu > 5:
        print("Opção invalida!!!")
    else:
        num1 = float(input("digite um numero: "))
        num2 = float(input("digite outro numero: "))

    if menu == 1:
        print(somar(num1, num2))
    elif menu == 2:
        print(subitrair(num1, num2))
    elif menu == 3:
        print(dividir(num1, num2))
    elif menu == 4:
        print(multiplicar(num1, num2))

