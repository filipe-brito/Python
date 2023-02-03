x1 = float(input("Digite a primeira nota: "))

while x1 < 0 or x1 > 10:
    x1 = float(input("Valor invalido! Tente novamente: "))

x2 = float(input("Digite a segunda nota: "))

while x2 < 0 or x2 > 10:
    x2 = float(input("Valor invalido! Tente novamente: "))

media = x1 + x2
print(f"MEDIA = {media / 2:.2f}")