total_cestas = 0

for i in range(1,11):
    cestas = int(input(f"{i}º - Digite o numero de cestas basicas arrecadadas: "))
    total_cestas += cestas

print(f"Total de cestas basicas arrecadadas: {total_cestas}")