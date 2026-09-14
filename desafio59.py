def menor_ou_maior_numero(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b

n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))

resultado = menor_ou_maior_numero(n1,n2)

if n1 % 2 == 0 and n1 % 2 == 0: 
    print(f"Menor numero: {resultado}")
else:
    print(f"Maior numero: {resultado}")