print("Digite dois numeros:")
x = int(input())
y = int(input())

somaI = 0
if x <= y:
    for loop in range (x+1, y):
        if loop % 2 != 0:
            somaI = somaI + loop
else:
    for loop in range (y+1, x):
        if loop % 2 != 0:
            somaI = somaI + loop

print(f"SOMA DOS IMPARES = {somaI}")