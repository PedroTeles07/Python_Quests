import random

sorteio = random.randint(1,10)

numero = int(input("Escolha um numero de 1 a 10: "))

if numero == sorteio:
    print("Você acertou em cheio!")
else:
    print(f"O numero sorteado foi: {sorteio}! Mais sorte na proxima.")
