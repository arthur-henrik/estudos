produto = 0
total = 0
resp = "s"

while resp == "s":
    produto = float(input("Digite o valor do produto: "))
    total = total + produto
    print(f"R$ {total}")
