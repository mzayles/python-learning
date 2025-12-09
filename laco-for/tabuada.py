""" Mostre a tabuada de um número que o usuário escolher. """

tabuada = int(input("Digite a tabuada que deseja: "))

print("")

for i in range(0, 11):
    print(f"{tabuada} x {i} = {i * tabuada}")