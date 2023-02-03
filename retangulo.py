import math

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura
print(f"AREA = {area:.4f}")

perimetro = base * 2 + altura * 2
print(f"PERIMETRO = {perimetro:.4f}")

diagonal = math.sqrt(base ** 2 + altura ** 2)
print(f"DIAGONAL = {diagonal:.4f}")
