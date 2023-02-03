N = int(input("Quantos valores vai ter cada vetor? "))

vetA = [0 for loop in range(N)]
vetB = [0 for loop in range(N)]
vetC = [0 for loop in range(N)]

print("Digite os valores do vetor A: ")
for loop in range(0, N):
    vetA[loop] = int(input())

print("Digite os valores do vetor B: ")
for loop in range(0, N):
    vetB[loop] = int(input())

print("VETOR RESULTANTE: ")
for loop in range(0, N):
    vetC[loop] = vetA[loop] + vetB[loop]
    print(vetC[loop])