try:
    arquivo = open("relatorio_vendas.txt","r")
    conteudo = arquivo.read()
    print(conteudo)

except FileNotFoundError:
    print("Arquivo não encontrado ")

finally:
    print("Encerrando o acesso ao arquivo")