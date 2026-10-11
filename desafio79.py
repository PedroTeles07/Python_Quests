def cadastrar_produto(nome, preco, quantidade):

    if nome.strip() == "":
        raise ValueError("O nome do produto não pode ser vazio.")

    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    return "Produto cadastrado com sucesso!"


try:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade: "))

    mensagem = cadastrar_produto(nome, preco, quantidade)
    print(mensagem)

except ValueError as erro:
    print(f"Erro: {erro}")
