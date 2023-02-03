salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000:
    aumento = salario / 100 * 20
    print(f"Novo salario = R$ {salario + aumento:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 20 %")
elif salario <= 3000:
    aumento = salario / 100 * 15
    print(f"Novo salario = R$ {salario + aumento:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 15 %")
elif salario <= 8000:
    aumento = salario / 100 * 10
    print(f"Novo salario = R$ {salario + aumento:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 10 %")
else:
    aumento = salario / 100 * 5
    print(f"Novo salario = R${salario + aumento:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 5 %")
