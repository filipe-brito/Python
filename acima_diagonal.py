N = int(input("Qual a ordem da matriz? "))

mat = [[0 for loop in range(N)]for loop in range(N)]

for loopl in range(N):
    for loopc in range(N):
        mat[loopl][loopc] = int(input(f"Elemento [{loopl},{loopc}]: "))

soma = 0
for loopl in range(N):
    for loopc in range(loopl+1, N):
        soma = soma + mat[loopl][loopc]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}")
