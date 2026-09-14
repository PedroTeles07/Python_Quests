def contar_caracteres(texto, caractere):
    return texto.count(caractere)

texto = input("Digite uma string:")
caractere = input("Digite um caractere: ")

resultado = contar_caracteres(texto,caractere)

print(f"O caractere aparece {resultado} vezes na string!")