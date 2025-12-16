""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas. """

valores = []
impares = []
pares = []

while True:
    numero = float(input(f"Digite um número ou [0] para sair: "))

    if numero == 0:
        break
    else:
        valores.append(numero)
        
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\nLista completa: {valores}.")
print(f"Lista de valores pares: {pares}.")
print(f"Lista de valores ímpares: {impares}.")