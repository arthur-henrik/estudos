nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("\nParabéns, você foi APROVADO com media:",media,)
elif media <= 4:
    print("\nVocê está REPROVADO, com media:",media, "se mate de estudar para reverter isso.")
else:
    print("\nVocê está em RECUPERAÇÃO com media:",media, "estude mais!")