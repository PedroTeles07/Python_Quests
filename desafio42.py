matriz_produtos = [
    [2343.45, 36736.90,36435.00],
    [35776.43,2567.65,35478.44],
    [3564.75,7543.46,4367.99]
]

soma = 0

for linha in matriz_produtos:
    for valor in linha:
        soma += valor

print(f"Soma total: R$ {soma:.2f}")