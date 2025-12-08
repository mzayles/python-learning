""" Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
ele foi multado.

A multa custará R$ 7,00 por cada Km acima do limite. """

velocidade = float(input("Informe a velocidade do carro: "))

if velocidade > 80:
    print("\nVocê foi multado por ultrapassar 80km/h!")
    print(f"Multa: R$ {(velocidade - 80) * 7:,.2f}")
else:
    print("Siga em frente.")