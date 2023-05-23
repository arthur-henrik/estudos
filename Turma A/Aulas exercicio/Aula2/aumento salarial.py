nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
percentual = float(input("Digite percentual e aumento: "))

resultado = salario + percentual / 100 * salario

print("\nO seu novo salário será de: R$",resultado,)

nome = input("Insira Seu Nome ")
idade = input("Insira a sua Idade ")
salario = float(input("Insira s seu Salário "))
aumento = float(input("Insira o percentual de aumento de Salário"))
percentual = (aumento/100)*salario
print("Nome:",nome)
print("Idade:",idade)
print("Salário:",salario)
print("Salário com Aumento:",salario+percentual)