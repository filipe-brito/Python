n = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(n)]

soma = 0
for loop in range(0, n):
    vet[loop] = float(input("Digite um numero: "))
    soma = soma + vet[loop]

print()

print("VALORES = ", end="")
for loop in range(0, n):
    print(f"{vet[loop]:.1f} ", end="")

print()

media = soma / n
print(f"SOMA = {soma:.1f}")
print(f"MEDIA = {media:.2f}")
