quadrado = 0
graos = 1
soma = 0

while quadrado <= 63:
    quadrado += 1
    if quadrado > 1:
        graos *= 2
        soma += graos
    print(f"Quadrado: {quadrado} - Grãos: {graos}")
    