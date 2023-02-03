preco = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
valor = float(input("Dinheiro recebido: "))

preco = preco * quantidade
if valor >= preco:
    troco = valor - preco
    print(f"TROCO = {troco:.2f}")
else:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {preco - valor:.2f} REAIS")