matriz_valores = [
    [2343.45, 36736.90,36435.00],
    [35776.43,2567.65,35478.44],
    [3564.75,7543.46,4367.99]
]

maior_valor = 0

for linha in matriz_valores:
    for valor in linha:
        if valor > maior_valor:
            maior_valor = valor

print(f"Maior valor encontrado: {maior_valor}")