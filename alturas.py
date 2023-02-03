N = int(input("Quantas pessoas serao digitadas? "))

vetN = [0 for loop in range(N)]
vetI = [0 for loop in range(N)]
vetA = [0 for loop in range(N)]

menor = 0
media = 0
for loop in range(0, N):
    print(f"Dados da {loop + 1}a pessoa: ")
    vetN[loop] = input(f"Nome: ")

    vetI[loop] = int(input("Idade: "))
    if vetI[loop] < 16:
        menor = menor + 1

    vetA[loop] = float(input("Altura: "))
    media = media + vetA[loop]
print()

media = media / N
print(f"Altura média: {media:.2f}")

menor = menor * 100 / N
print(f"Pessoas com menos de 16 anos: {menor:.1f}%")

for loop in range(0, N):
    if vetI[loop] < 16:
        print(vetN[loop])
