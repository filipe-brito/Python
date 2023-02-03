N = int(input("Qual a ordem da matriz? "))

mat = [[0 for loop in range(N)]for loop in range(N)]

for loopl in range(N):
    for loopc in range(N):
        mat[loopl][loopc] = int(input(f"Elemento [{loopl},{loopc}]: "))

print("MAIOR ELEMENTO DE CADA LINHA: ")
for loopl in range(N):
    maior = 0
    for loopc in range(N):
        if mat[loopl][loopc] > maior:
            maior = mat[loopl][loopc]
    print(maior)