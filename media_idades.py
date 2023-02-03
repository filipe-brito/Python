print("Digite as idades: ")
x = int(input())

media = 0
soma = 0

if x < 0:
    print("IMPOSSIVEL CALCULAR ")
else:
    while x >= 0:
        media = media + x
        soma = soma + 1
        x = int(input())

    media = media / soma
    print(f"MEDIA = {media:.2f}")
