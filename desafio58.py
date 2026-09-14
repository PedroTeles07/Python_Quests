def calcular_gorjeta(conta):
    return conta * 0.1

conta = float(input("Digite o valor da conta[R$]: "))

gorjeta = calcular_gorjeta(conta)

print(f"Gorjeta do garçom: R$ {gorjeta:.2f}")