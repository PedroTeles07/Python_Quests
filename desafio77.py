def realizar_saque(saldo, valor_saque):

    if valor_saque <= 0:
        raise ValueError("O valor do saque deve ser positivo.")

    if valor_saque > saldo:
        raise ValueError("Saldo insuficiente.")

    return saldo - valor_saque


saldo = 1000

try:
    valor = float(input("Digite o valor do saque: "))
    saldo = realizar_saque(saldo, valor)
    print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")

except ValueError as erro:
    print(f"Erro: {erro}")