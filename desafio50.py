alunos = {}

for i in range(1,6):
    nome = input(f"\nDigite o nome do {i}º aluno:")
    nota = float(input(f"Digite a nota do {i}º aluno:"))
    alunos[nome] = nota

media = sum(alunos.values()) / len(alunos)

print(f"Média geral: {media}")

print("Alunos aprovados:")
for nome, nota  in alunos.items():
    if nota >= 7:
        print(f"{nome} : {nota}")