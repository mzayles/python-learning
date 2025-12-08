""" Crie um programa que leia o nome de um bairro e diga se
ele começa ou não com o nome Santo. """

bairro = input("Digite o nome do bairro: ").lower()

if "santo" in bairro.split()[0]:
    print("O bairro começa com o nome Santo.")
else:
    print("O bairro não começa com o nome Santo.")
