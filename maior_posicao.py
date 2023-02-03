N = int(input("Quanto numeros voce vai digitar? "))

vet = [0 for loop in range(N)]

maior = 0
posicao = 0
for loop in range(0, N):
    vet[loop] = float(input("Digite um numero: "))
    if vet[loop] > maior:
        maior = vet[loop]
        posicao = loop
print()

print(f"MAIOR VALOR = {maior}")
print(f"POSICAO DO MAIOR VALOR = {posicao}")
