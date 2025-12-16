""" Crie um programa que gere cinco números aleatórios para uma tupla.
Mostre a listagem de números gerados, indique o menor e o maior valor. """

import random

lista = []

for i in range(5):
    lista.append(random.randint(1, 50))

tupla = tuple(lista)
print(tupla)

print(f"\nMaior: {max(tupla)}")
print(f"Menor: {min(tupla)}")