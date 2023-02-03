N = int(input("Serao digitados dados de quantos produtos? "))

vetnome = [0 for x in range(N)]
vetC = [0 for x in range(N)]
vetV = [0 for x in range(N)]

lucro1 = 0
lucro2 = 0
lucro3 = 0
totalL = 0
totalC = 0
totalV = 0
lucro = 0
for loop in range(0, N):
    print(f"Produto {loop+1}:")
    vetnome[loop] = input("Nome: ")
    vetC[loop] = float(input("Preco de compra: "))
    vetV[loop] = float(input("Preco de venda: "))

    totalC = totalC + vetC[loop]
    totalV = totalV + vetV[loop]

    lucro = vetV[loop] - vetC[loop]
    totalL = totalL + lucro
    if lucro * 100 / vetC[loop] < 10:
        lucro1 = lucro1 + 1
    elif lucro * 100 / vetC[loop] <= 20:
        lucro2 = lucro2 + 1
    else:
        lucro3 = lucro3 + 1

print()

print("RELATORIO:")
print(f"Lucro abaixo de 10%: {lucro1}")
print(f"Lucro entre 10% e 20%: {lucro2}")
print(f"Lucro acima de 20%: {lucro3}")
print(f"Valor total de compra: {totalC:.2f}")
print(f"Valor total de venda: {totalV:.2f}")
print(f"Lucro total: {totalL:.2f}")