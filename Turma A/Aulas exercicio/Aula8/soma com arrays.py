num1 = []
num2 = []
soma = []

tam_var = int(input('quantos nunmeros você quer somar?: '))

for a in range(tam_var):
    num1.append(int(input('Digite o primeiro numero: ')))
    num2.append(int(input('Digite o segundo numero: ')))

for b in range(tam_var):
    soma.append(num1[b] + num2[b])

print(num1)
print(num2)
print(soma)
