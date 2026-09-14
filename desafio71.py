class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente")

    return saldo - valor

saldo = 500

try:
    saldo = sacar(saldo, 700)
    print(f"Saque realizado. Saldo restante: R$ {saldo:.2f}")
    
except SaldoInsuficienteError as erro:
    print(erro)