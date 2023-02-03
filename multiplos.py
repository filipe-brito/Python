print("Digite dois numeros inteiros:")
x1 = int(input())
x2 = int(input())

if x2 >= x1:
    if x2 % x1 == 0:
        print("Sao multiplos")
    else:
        print("Nao sao multiplos")
else:
    if x1 % x2 == 0:
        print("Sao multiplos")
    else:
        print("Nao sao multiplos")