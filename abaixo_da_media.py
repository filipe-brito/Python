N = int(input("Quantos elementos vai ter o vetor? "))

vet = [0 for loop in range(N)]

media = 0
for loop in range(0, N):
    vet[loop] = float(input("Digite um numero: "))
    media = media + vet[loop]
print()

media = media / N
print(f"MEDIA DO VETOR = {media:.3f}")

print("ELEMENTOS ABAIXO DA MEDIA: ")
for loop in range(0, N):
    if vet[loop] < media:
        print(f"{vet[loop]:.1f}")
