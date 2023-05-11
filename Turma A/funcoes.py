def somar(*numeros):
    return numeros

def subitrair(a, b):
    subtra = 0
    subtra = a-b
    return subtra

def dividir(a, b):
    divisao = 0
    divisao = a/b
    return divisao

def multiplicar(a, b):
    multipl = 0
    multipl = a*b
    return multipl

def imprime_nome(nome):
    print(f"olá: {nome}")

def letras(t):
    cont = 0
    for letra in t:
        if letra != " ":
            cont += 1
    print(cont)

def num_sequencia(n):
    for a in range(1, n+1):
        print()
        for b in range(1, a):
            print(b, end=" ")

def vogal(t):
    cont = 0
    for voga in t:
        if voga in 'aeiouAEIOU':
            cont += 1
    print(cont)


def estoq(prod, qntd, valr):
    return prod, qntd * valr

def numero(n):
    if n != 0:
        if n > 0:
            return "P"
        else:
            return "N"
    else:
        return "Z"

def somatoria(*num):
    soma = 0
    for n in num:
        soma+=n
