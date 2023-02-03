minutos = int(input("Digite a quantidade de minutos: "))

if minutos > 100:
    valor = (minutos - 100) * 2 + 50
else:
    valor = 50

print(f"Valor a pagar: R$ {valor:.2f}")