M = int(input("Qual a quantidade de linhas da matriz? "))
N = int(input("Qual a quantidade de colunas da matriz? "))

mat = [[0 for loopc in range(N)]for loopl in range(M)]
vet = [0 for loopl in range(M)]

for loopl in range(M):
    print(f"Digite os elementos da {loopl+1}a. linha:")
    soma = 0
    for loopc in range(N):
        mat[loopl][loopc] = float(input())
        soma = soma + mat[loopl][loopc]
        vet[loopl] = soma

print("VETOR GERADO:")
for loopl in range(M):
    print(vet[loopl])
