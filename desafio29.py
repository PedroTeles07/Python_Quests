vendas = (2890, 3429, 4009, 3899)
maior_venda = 0

for venda in vendas:
    if venda > maior_venda:
        maior_venda = venda

print(f"Maior venda: R${maior_venda}")