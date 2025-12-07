""" Crie um programa e declare uma constante PI utilizando 4 casas
decimais. Dados o raio e a altura, calcule e apresente o volume de um
objeto cilíndrico.
    Fórmula: volume = PI * r² * altura """

PI = 3.1415

raio = float(input("Informe o raio do cilindro: "))
altura = float(input("Informe a altura do cilindro: "))

volume = PI * (raio ** 2) * altura
print(f"\nO volume do objeto cilíndrico é {volume:,.2f}m³.")