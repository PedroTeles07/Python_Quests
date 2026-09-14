def calcular_animais():
    for galinhas in range(36):
        coelhos = 35 - galinhas

        if galinhas * 2 + coelhos * 4 == 94:
            return galinhas, coelhos

galinhas, coelhos = calcular_animais()

print(f"Galinhas: {galinhas}")
print(f"Coelhos: {coelhos}")
