N = int(input("Quantos casos de teste serao digitados? "))

somaT = 0
somaC = 0
somaR = 0
somaS = 0
percC = 0
percR = 0
percS = 0

for loop in range(0, N):
    quantidade = int(input("Quantidade de cobaias: "))
    somaT = somaT + quantidade

    tipo = input("Tipo de cobaia: ")
    if tipo == 'c':
        somaC = somaC + quantidade
    elif tipo == 'r':
        somaR = somaR + quantidade
    elif tipo == 's':
        somaS = somaS + quantidade

print()
print("RELATORIO FINAL:")

print(f"Total: {somaT} cobaias")
print(f"Total de coelhos: {somaC}")
print(f"Total de ratos: {somaR}")
print(f"Total de sapos: {somaS}")

print(f"Percentual de coelhos: {somaC * 100 / somaT:.2f}%")
print(f"Percentual de ratos: {somaR * 100 / somaT:.2f}%")
print(f"Percentual de sapos: {somaS * 100 / somaT:.2f}%")
