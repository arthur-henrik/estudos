eleitores = float(input("Qual o total de eleitores?: "))
v_brancos = float(input("Qual o total de votos brancos?: "))
v_nulos = float(input("Qual o total de votos nulos?: "))
v_validos = float(input("Qual o total de votos validos?: "))

porc_brancos = (v_brancos/eleitores) * 100
porc_nulos = (v_nulos/eleitores) * 100
porc_validos = (v_validos/eleitores) * 100

total = v_brancos + v_nulos + v_validos

if total > eleitores:
    print("a quantidade dos votos não pode ultrapassar a qnt de eleitores.")
else:
    print(f'''total de eleitores {eleitores}.
    a porcentagem de votos brancos representa: {porc_brancos}%.
    a porcentagem de votos nulos representa: {porc_nulos}%.
    a porcentagem de votos validos representa: {porc_validos}%.''')
