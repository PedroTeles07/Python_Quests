produtos = []

for i in range(1,6):
    item = input(f"Digite o nome do {i} produto: ")
    produtos.append(item)

print("===Lista de Produtos===")
for produto in produtos:
    print(produto)