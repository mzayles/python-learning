""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até
ter um valor correto. """

while True:
    sexo = input("Digite o seu sexo: [F] ou [M]: ").upper()

    if sexo == "F" or sexo == "M":
        print(f"\nOk!")
        print("O seu sexo é feminino." if sexo == "F" else "O seu sexo é masculino.")
        break
    else:
        print("\nInválido!")