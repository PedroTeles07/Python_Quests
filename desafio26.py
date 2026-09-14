codigos = [101,102,103,104,105]

codigo = int(input("Digite o código do produto: "))

if codigo in codigos:
    print(f"Código encontrado!")
else:
    print("Código não encontrado!")