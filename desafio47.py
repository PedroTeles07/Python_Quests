matriz = [
    [1, -2, 3],
    [-4, 5, 6],
    [7, 8, -9]
]

valores_positivos = 0

for linha in matriz:
    for valor in linha:
        if valor > 0:
            valores_positivos = valores_positivos + 1

print(f"Quantidades de numeros positivos: {valores_positivos}")

