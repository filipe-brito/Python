print("Digite dois numeros: ")
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print("CRESCENTE")
    else:
        print("DECRESCENTE")

    x = int(input())
    y = int(input())