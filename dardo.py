print("Digite as tres distancia: ")
d1 = float(input())
d2 = float(input())
d3 = float(input())

maior = d1
if d2 > d1:
    maior = d2
elif d3 > d2:
    maior = d3

print(f"MAIOR DISTANCIA = {maior:.2f}")
