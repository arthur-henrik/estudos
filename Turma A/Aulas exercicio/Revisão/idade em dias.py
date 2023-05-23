resp = 's'
while resp == 's':
    anos = int(input("digite sua idade em anos: "))
    mes = int(input("Quantos meses você tem após o seu aniversario?: "))
    dia = int(input("quantos dias se passaram após seu aniversario?: "))

    ano_d = anos * 365
    mes_d = mes * 30

    total_dias = ano_d + mes_d + dia

    print(f"você está a {total_dias} dias na terra!")

    resp = input("deseja fazer outra soma de dias? s/n: ")
    