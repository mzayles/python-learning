""" Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artificio, indo de 10 até 0, com uma pausa
de 1 segundo entre eles.
Utilizar a Biblioteca TIME | time.sleep(segundos) """

import time
import os

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
    
os.system("clear")
print("\nEstouro de fogos!")