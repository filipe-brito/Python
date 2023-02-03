import math

N = int(input("Qual a ordem da matriz? "))

mat = [[0 for loop in range(N)]for loop in range(N)]

soma = 0
for loopl in range(N):
    for loopc in range(N):
        mat[loopl][loopc] = float(input(f"Elemento [{loopl},{loopc}]: "))
        if mat[loopl][loopc] > 0:
            soma = soma + mat[loopl][loopc]
print()

print(f"SOMA DOS POSITIVOS: {soma:.1f}")
print()

indice = int(input("Escolha uma linha: "))
print("LINHA ESCOLHIDA: ", end="  ")
for loopc in range(N):
    print(f"{mat[indice][loopc]:.1f}", end="  ")
print()
print()

indice = int(input("Escolha uma coluna: "))
print("COLUNA ESCOLHIDA:", end="  ")
for loopl in range(N):
    print(f"{mat[loopl][indice]:.1f}", end="  ")
print()
print()

print("DIAGONAL PRINCIPAL: ", end="  ")
for loop in range(N):
    print(f"{mat[loop][loop]:.1f}", end="  ")
print()
print()

print("MATRIZ ALTERADA: ")
for loopl in range(N):
    for loopc in range(N):
        if mat[loopl][loopc] < 0:
            alterar = math.pow(mat[loopl][loopc], 2)
            print(f"{alterar:.1f}", end="  ")
        else:
            print(f"{mat[loopl][loopc]:.1f}", end="  ")
    print()
