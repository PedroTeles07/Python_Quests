medicamentos = {}

for i in range (1,6):
    nome = input(f"\nDigite o nome do {i}° medicamento: ").lower()
    estoque = int(input("Digite a quantidade disponivel em estoque desse medicamento: "))
    medicamentos[nome] = [estoque]

consulta = input("\nDigite o nome do medicamento a ser consultado: ").lower()

if consulta in medicamentos:
    print(f"\nEstoque disponível: {medicamentos[consulta]}")
else:
    print("\nProduto não encontrado!") 
