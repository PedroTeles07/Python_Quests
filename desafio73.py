precos = ["100.00", "50.50", "abc", "80.00"]

for preco in precos:
    try:
        preco = float(preco)

    except ValueError:
        print("Preco inválido.")

    else:
        desconto = preco * 0.10
        preco_final = preco - desconto
        print(f"Preço com desconto: R${preco_final:.2f}")