produtos = {}

for i in range(1,4):
    nome = input("\nDigite o nome do produto: ")
    estoque = int(input("Digite o estoque do produto: "))
    produtos[nome] = estoque

for produto, quantidade in produtos.items():
    print(f"{produto} : {quantidade} UNI")
