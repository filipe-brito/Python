N = int(input("Qual a ordem da matriz? "))

mat = [[0 for loop in range(N)]for loop in range(N)]

negativos = 0
for loopl in range(N):
    for loopc in range(N):
        mat[loopl][loopc] = int(input(f"Elemento [{loopl},{loopc}]: "))
        if mat[loopl][loopc] < 0:
            negativos = negativos + 1

print("DIAGONAL PRINCIPAL: ")
for loop in range(N):
    print(mat[loop][loop], end="  ")
print()

print(f"QUANTIDADE DE NEGATIVOS = {negativos}")
