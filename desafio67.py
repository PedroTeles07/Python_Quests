while True:
    try:
        idade = int(input("Digite sua idade:"))

        if idade < 0:
            print("Idade inválida!")
        else:
            break

    except ValueError:
        print("Digite apenas numeros inteiros.")

print(f"Idade cadastrada: {idade}")
