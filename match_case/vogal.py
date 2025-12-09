""" Crie um programa que peça ao usuário para inserir uma letra. O programa deve utilizar match case
para verificar se a letra é uma vogal. """

letra = input("Digite uma letra: ").upper()

match(letra):
    case "A" | "E" | "I" | "O" | "U":
        print("\nÉ vogal.")
    case _:
        if letra.isalpha():
            print("\nÉ consoante.")
        else:
            print("\nInválido!")