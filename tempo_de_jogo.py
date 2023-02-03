horaI = int(input("Hora inicial: "))
horaF = int(input("Hora final: "))

if horaI >= horaF:
    duracao = 24 - (horaI - horaF)
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    duracao = horaF - horaI
    print(f"O JOGO DUROU {duracao} HORA(S)")
