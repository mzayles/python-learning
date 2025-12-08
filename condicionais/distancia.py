""" Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem cobrando R$
0,50 por Km para viagens de até 200 Km e R$ 0,45 para
viagens mais longas. """

distancia = float(input("Informe a distância da viagem (km): "))

if distancia <= 200:
    print(f"\nPreço da passagem: R$ {distancia * 0.50:,.2f}.")
else:
    print(f"\nPreço da passagem: R$ {distancia * 0.45:,.2f}.")