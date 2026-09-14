temperaturas = []
soma = 0

for i in range(1,6):
    temperatura = float(input(f"Digite a temperatura registrada no {i}º dia[°C]:"))
    temperaturas.append(temperatura)
    soma += temperatura

temp_media = soma/len(temperaturas)

print("\n===Temperaturas registradas===")
for temp in temperaturas:
    print(f"{temp}°C")

print(f"\nTemperatura média: {temp_media}")

if temp_media >= 18 and temp_media <= 28:
    print("Temperatura na faixa ideal de cultivo!")
else:
    print("Temperatura fora da faixa idela de cultivo!")