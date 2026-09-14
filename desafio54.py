estacionamento = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

vagas_livres = 0
vagas_ocupadas = 0

for linha in estacionamento:
    for vaga in linha:
        if vaga == 0:
            vagas_livres += 1
        else:
            vagas_ocupadas += 1

print(f"Vagas disponiveis: {vagas_livres}")
print(f"Vagas ocupadas: {vagas_ocupadas}")