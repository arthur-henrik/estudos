qnt_alunos = int(input("qual alunos tem na sala de aula?: "))
nomes_alunos = []

for x in range(qnt_alunos):
    nomes_alunos.append(input("digite os nomes do alunos: "))
for y in range(qnt_alunos):
    print(y, nomes_alunos[y])

procurar_aluno = input("qual aluno você quer pesquisar?: ")
for z in range(qnt_alunos):
    if procurar_aluno == procurar_aluno[z]:
        print(nomes_alunos[z], z)
