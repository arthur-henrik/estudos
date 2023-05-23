num1 = float(input('digite um numero: '))
num2 = float(input('digite outro numero: '))
num3 = float(input('digite mais um numero: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} é maior!')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é maior!')
else:
    print(f'{num3} é maior!')