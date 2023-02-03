N = int(input("Digite o valor de N: "))

fatorial = 0
if N == 0:
    print("FATORIAL = 1")
else:
    fatorial = N
    for loop in range(N-1, 0, -1):
        fatorial = fatorial * loop

    print(f"FATORIAL = {fatorial}")