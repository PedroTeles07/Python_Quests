def parse_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido.")

    return cpf

def main():
    cpf = input("Digite seu CPF: ")

    try:
        cpf = parse_cpf(cpf)
        print(f"CPF válido: {cpf}")

    except ValueError as erro:
        print(f"Erro: {erro}")

main()