import random

sorteio = random.randint(1,10)

while True:
    numero = int(input("\nEscolha um numero de 1 a 10: "))

    if numero == sorteio:
        print("\nVocê acertou em cheio!")
        break
    elif numero > sorteio:
        print("\nSeu numero digitado é maior que o sorteado!")
    elif numero < sorteio:
        print("\nSeu numero digitado é menor que o sorteado!")
