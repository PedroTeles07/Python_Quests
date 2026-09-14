soma = 0

while True:
    avaliacao = float(input("Digite sua nota de satisfação de 0 a 10 [0 para encerrar]:"))

    if avaliacao > 0:
        soma += avaliacao
    else:
        break

print(f"Soma das notas: {soma}")