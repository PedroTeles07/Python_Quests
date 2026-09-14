matriz_valores = [
    [2343.45, 36736.90,36435.00],
    [35776.43,2567.65,35478.44],
    [3564.75,7543.46,4367.99]
]

for linha in matriz_valores:
    for valor in linha:
        if valor == matriz_valores[0][0]:
            menor_valor = valor
        elif valor < menor_valor:
            menor_valor = valor

print(f"Maior valor encontrado: {menor_valor}")