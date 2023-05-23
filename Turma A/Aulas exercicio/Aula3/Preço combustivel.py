print("\nDigite G para GASOLINA ou E para ETANOL")
print("Preço Gasolina R$ 5,80 --- Preço Etanol R$ 4,90")

tipo_combus = input("\nQual o tipo de combustivel?: ")

if tipo_combus in "GgEe":
    litro = float(input("Quantos litros você quer abastecer?: "))
    if tipo_combus == "G" or tipo_combus == "g":
        print("\nO valor total da gasolina foi de:",(5.80 * litro))
    else:
        print("\nO valor total do Etanol foi de:",(4.90 * litro))
else:
    print("\nCombustivel não cadastrado")