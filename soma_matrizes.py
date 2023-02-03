M = int(input("Quantas linhas vai ter cada matriz? "))
N = int(input("Quantas colunas vai ter cada matriz? "))

matA = [[0 for loopc in range(N)]for loopl in range(M)]
matB = [[0 for loopc in range(N)]for loopl in range(M)]
matC = [[0 for loopc in range(N)]for loopl in range(M)]

print("Digite os valores da matriz A:")
for loopl in range (M):
    for loopc in range (N):
        matA[loopl][loopc] = int(input(f"Elemento [{loopl},{loopc}]: "))

print("Digite os valores da matriz B:")
for loopl in range (M):
    for loopc in range (N):
        matB[loopl][loopc] = int(input(f"Elemento [{loopl},{loopc}]: "))

print("MATRIZ SOMA:")
for loopl in range (M):
    for loopc in range (N):
        matC[loopl][loopc] = matA[loopl][loopc] + matB[loopl][loopc]
        print(matC[loopl][loopc], end="  ")
    print()