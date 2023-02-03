M = int(input("Qual a quantidade de linhas da matriz? "))
N = int(input("Qual a quantidade de colunas da matriz? "))

mat = [[0 for loopc in range(N)]for loopl in range(M)]

for loopl in range(M):
    for loopc in range(N):
        mat[loopl][loopc] = int(input(f"Elemento [{loopl},{loopc}]:"))

print("VALORES NEGATIVOS: ")

for loopl in range(M):
    for loopc in range(N):
        if mat[loopl][loopc] < 0:
            print(mat[loopl][loopc])