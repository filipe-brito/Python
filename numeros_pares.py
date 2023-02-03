N = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for loop in range(N)]

pares = 0
for loop in range(0, N):
    vet[loop] = int(input("Digite um numero: "))
    if vet[loop] % 2 == 0:
        pares = pares + 1
print()

print("NUMEROS PARES: ")
for loop in range(0, N):
    if vet[loop] % 2 == 0:
        print(vet[loop], end="  ")
print()
print()

print(f"QUANTIDADE DE PARES = {pares}")