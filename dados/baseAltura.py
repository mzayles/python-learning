""" Crie um programa para entrar com a base e a altura de um retângulo e imprimir
respectivamente o perímetro e a área correspondente. """

base = float(input("Informe a base do retângulo: "))
altura = float(input("Informe a altura do retângulo: "))

print(f"\nPerímetro: {(base + altura) * 2}")
print(f"\Área: {(base * altura) / 2}")