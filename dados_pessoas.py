N = int(input("Quantas pessoas serao digitadas? "))

vetaltura = [0 for x in range(N)]
vetgenero = [0 for x in range(N)]

maior = 0
mediaM = 0
homens = 0
mulheres = 0
for loop in range(0, N):
    vetaltura[loop] = float(input(f"Altura da {loop+1}a pessoa: "))
    vetgenero[loop] = input(f"Genero da {loop+1}a pessoa: ")

    if vetaltura[loop] > maior:
        maior = vetaltura[loop]

    if vetgenero[loop] == 'F':
        mediaM = mediaM + vetaltura[loop]
        mulheres = mulheres + 1
    else:
        homens = homens + 1

menor = vetaltura[0]
for loop in range(0, N):
    if vetaltura[loop] < menor:
        menor = vetaltura[loop]

mediaM = mediaM / mulheres

print(f"Menor altura = {menor:.2f}")
print(f"Maior altura = {maior:.2f}")
print(f"Media das alturas das mulheres = {mediaM:.2f}")
print(f"Numero de homens = {homens}")

