while True:
    try:
        acionistas = int(input("Digite o numero de acionistas: "))
        lucro = float(input("Digite o lucro do trimestre: "))

        divisao = lucro / acionistas

        print(f"Lucro por acionista: R${divisao:.2f}")
        break
    except ZeroDivisionError:
        print("A quantidade de acionistas não pode ser zero.")

    except ValueError:
        print("Digite apenas numeros.")