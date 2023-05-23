time1 = input("digite o primeiro time: ")
time2 = input("digite o segundo time: ")

golstime1 = int(input("Quantos gols o {} fez?: ".format(time1)))
golstime2 = int(input("Quantos gols o {} fez?: ".format(time2)))

if golstime1 == golstime2:
    print("EMPATE")
elif golstime1 > golstime2:
    print("O {} Venceu".format(time1))
else:
    print("O {} Venceu".format(time2))