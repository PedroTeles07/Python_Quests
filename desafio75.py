def conectar_api():
    tentativas = 0

    while tentativas < 3:
        try:
            print("Tentando conectar à API...")

            conexao = True

            if conexao:
                print("Conexão realizada com sucesso!")
                break

        except ConnectionError:
            tentativas += 1
            print(f"Falha na conexão. Tentativa {tentativas} de 3.")

    if tentativas == 3:
        print("Falha após 3 tentativas.")
        print("Encerrando a operação com segurança.")


conectar_api()