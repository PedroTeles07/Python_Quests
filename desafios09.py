livros = []

for i in range(3):
    titulo_livro = input(f"Digite o titulo do {i+1}º livro: ")
    livros.append(titulo_livro)

print("===Lista de Livros Cadastrados===")
for livro in livros:
    print(livro)