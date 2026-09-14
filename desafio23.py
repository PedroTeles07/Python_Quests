gastos = []
gasto_mensal = 0

while True:
    valor = float(input("Digite o valor do gasto [0 para encerrar]: "))
    if valor == 0:
        break
    else:
        gastos.append(valor)
        gasto_mensal += valor

print(f"Gasto mensal: R${gasto_mensal}")