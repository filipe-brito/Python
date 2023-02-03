N = int(input("Quantos elementos vai ter o vetor? "))

vet = [0 for loop in range(N)]

nPar = 0
somaPar = 0
for loop in range(0, N):
    vet[loop] = int(input("Digite um numero: "))
    if vet[loop] % 2 == 0:
        nPar = nPar + 1
        somaPar = somaPar + vet[loop]

if nPar == 0:
    print("NENHUM NUMERO PAR ")
else:
    media = somaPar / nPar
    print(f"MEDIA DOS PARES = {media:.1f}")
