n = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(n)]

for loop in range(0, n):
    vet[loop] = int(input("Digite um numero: "))

print("Numeros negativos:")
for loop in range(0, n):
    if vet[loop] < 0:
        print(vet[loop])