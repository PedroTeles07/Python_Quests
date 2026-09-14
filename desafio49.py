cadastros = {}

for i in range(5):
    nome = input(f"\nDigite o nome do {i+1}º aluno(a): ")
    nota = float(input("Digite a nota do aluno(a): "))
    cadastros[nome] = nota

print("\n===Tabela de Desempenho Academico===\n")
for nome, nota in cadastros.items():
    print(f"{nome} - nota: {nota}")