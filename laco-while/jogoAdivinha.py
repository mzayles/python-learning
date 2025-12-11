""" Faça um programa onde o computador vai “pensar” em um número entre 1 a 10.
O jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer. """

import random

computador = random.randint(1, 10)
palpites = 0

while True:
    usuario = int(input("Adivinhe qual número o computador pensou entre 1 a 10: "))

    if usuario != computador:
        palpites += 1
        print("\nVocê errou! Tente novamente.")
    else:
        print("\nParabéns! Você acertou com 1 tentativa!" if palpites == 1 else f"\nParabéns! Você acertou com {palpites} tentativas.")
        break