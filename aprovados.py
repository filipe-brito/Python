N = int(input("Quantos alunos serao digitados? "))

vetNome = [0 for loop in range(N)]
vetN1 = [0 for loop in range(N)]
vetN2 = [0 for loop in range(N)]
vetMedia = [0 for loop in range(N)]

for loop in range(0, N):
    print(f"Digite nome, primeira e segunda nota do {loop+1}o aluno: ")
    vetNome[loop] = input()
    vetN1[loop] = float(input())
    vetN2[loop] = float(input())
    vetMedia[loop] = (vetN1[loop] + vetN2[loop]) / 2

print("Alunos aprovados: ")

for loop in range(0, N):
    if vetMedia[loop] >= 6.0:
        print(vetNome[loop])
