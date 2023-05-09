soma = 0
num = 1

alunos = int(input("quantos alunos na sala?: "))

while num <= alunos:
    notas = float(input("nota de alunos: "))
    soma += notas
    num += 1
media = soma / alunos
print(media)