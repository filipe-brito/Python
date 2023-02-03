preco = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
pagamento = float(input("Dinheiro recebido: "))

troco = pagamento - preco * quantidade
print(f"TROCO = {troco:.2f}")
