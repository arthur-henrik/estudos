numeros = []
qntd_escolha = int(input("Quantas vezes você quer repetir o processo: "))
for a in range(qntd_escolha):
    numeros.append(input(f"Digite o {a+1}° numero."))

from funcoes import somatoria

total = somatoria(a)
print(total)
