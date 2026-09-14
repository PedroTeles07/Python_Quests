class ProdutoInvalidoError(Exception):
    pass


class ValorInvalidoError(Exception):
    pass


class QuantidadeInvalidaError(Exception):
    pass


def registrar_venda(produto, preco, quantidade):

    if produto == "":
        raise ProdutoInvalidoError("O nome do produto não pode ser vazio.")

    if preco <= 0:
        raise ValorInvalidoError("O preço deve ser maior que zero.")

    if not isinstance(quantidade, int) or isinstance(quantidade, bool) or quantidade <= 0:
        raise QuantidadeInvalidaError(
            "A quantidade deve ser um número inteiro positivo."
        )

    total = preco * quantidade

    return {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }


def gerar_relatorio(vendas):

    if len(vendas) == 0:
        print("Nenhuma venda registrada.")
        return

    quantidade_vendas = len(vendas)

    faturamento = 0
    produto_mais_vendido = vendas[0]["produto"]
    maior_quantidade = vendas[0]["quantidade"]

    for venda in vendas:
        faturamento += venda["total"]

        if venda["quantidade"] > maior_quantidade:
            maior_quantidade = venda["quantidade"]
            produto_mais_vendido = venda["produto"]

    ticket_medio = faturamento / quantidade_vendas

    print("\n===== RELATÓRIO DIÁRIO =====")
    print(f"Quantidade de vendas: {quantidade_vendas}")
    print(f"Produto mais vendido: {produto_mais_vendido}")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")


vendas = []

while True:

    produto = input("\nDigite o nome do produto (ou 'fim' para encerrar): ")

    if produto.lower() == "fim":
        break

    try:
        preco = float(input("Digite o preço unitário: R$ "))
        quantidade = int(input("Digite a quantidade vendida: "))

        venda = registrar_venda(produto, preco, quantidade)

    except ProdutoInvalidoError as erro:
        print(f"Erro: {erro}")

    except ValorInvalidoError as erro:
        print(f"Erro: {erro}")

    except QuantidadeInvalidaError as erro:
        print(f"Erro: {erro}")

    except ValueError:
        print("Erro: preço ou quantidade inválidos.")

    else:
        vendas.append(venda)
        print("Venda registrada com sucesso!")

    finally:
        print("Processamento da venda encerrado.")


gerar_relatorio(vendas)