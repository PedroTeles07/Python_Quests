def converter_celsius(temperatura):
    return (5/9)*(temperatura - 32)

fahrenheit = float(input("Digite a temperatura em °F:"))
celsius = converter_celsius(fahrenheit)

print(f"Temperatura convertida para celsius: {celsius:.2f}°C")