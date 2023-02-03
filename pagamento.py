nome = input("Nome: ")
valorH = float(input("Valor por hora: "))
horasT = float(input("Horas trabalhadas: "))

pagamento = valorH * horasT
print(f"O pagamento para {nome} deve ser {pagamento:.2f}")