codigo = int(input("Digite o codigo do equipamento: "))

if codigo % 2 == 0:
    print("Classificação: par;\nSetor: Administrativo;")
else:
    print("Classificação: ímpar;\nSetor: Operacional;")