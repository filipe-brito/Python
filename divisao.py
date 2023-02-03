n = int(input("Quantos casos voce vai digitar? "))

for loop in range(0,n):
    numerador = int(input("Entre com o numerador: "))
    denominador = int(input("Entre com o denominador: "))

    if denominador == 0:
        print("DIVISAO IMPOSSIVEL")
    else:
        quociente = numerador / denominador
        print(f"DIVISAO = {quociente:.2f}")