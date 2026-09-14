import traceback

def processar_dados(dados):

    for dado in dados:

        try:
            numero = int(dado)
            resultado = numero * 2
            print(f"Resultado: {resultado}")

        except (TypeError, ValueError):
            print("Erro ao processar o dado:")
            traceback.print_exc()


dados = ["10", "20", "abc", None, "30"]

processar_dados(dados)