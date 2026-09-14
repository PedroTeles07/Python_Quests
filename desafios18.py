fatura_semanal = 0

for i in range(1,8):
    fatura_diaria = float(input("Digite a fatura do dia: "))
    fatura_semanal += fatura_diaria

print(f"Fatura semanal: R${fatura_semanal}")