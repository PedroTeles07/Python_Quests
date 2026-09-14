disciplinas = ("Matemática", "Português")

alunos = {
    "Ana": (8.0,7.5),
    "Carlos":(7.0,5.0),
    "Pedro":(10.0,9.5)
}

for nome, notas in alunos.items():
    media = (notas[0] + notas[1]) / 2

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"Aluno: {nome}")
    print(f"Média: {media}")
    print(f"Situação: {situacao}")
    print()

print("===Disciplinas Cadastradas===\n")

for disciplina in disciplinas:
    print(disciplina)