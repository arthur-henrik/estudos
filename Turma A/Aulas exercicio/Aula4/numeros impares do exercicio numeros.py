num = int(input("digite um numero: "))
y = 0
z = 0
for x in range(1, num+1):
    if x %2 != 0:
        y=y+1
    else:
        z=z+1
print(y)
print(z)