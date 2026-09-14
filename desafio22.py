notas = []
maior_nota = 0

for i in range(1,5):
    nota = float(input(f"Digite a nota do {i}º aluno:"))
    notas.append(nota)
    if nota > maior_nota:
        maior_nota = nota;

print(f"Maior nota: {maior_nota}")