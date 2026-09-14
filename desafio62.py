def numero_perfeito(numero):
    soma = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma += divisor

    return soma == numero

numero = int(input("Digite um numero inteiro: "))

if numero_perfeito(numero):
    print("O número é perfeito!")
else:
    print("O número não é perfeito!")