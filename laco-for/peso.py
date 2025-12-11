""" Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos. """

for i in range(1, 6):
    peso = float(input(f"Digite o {i}º peso: "))

    if i == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print("")
print(f"\nMaior peso: {maior}.")
print(f"Menor peso: {menor}.")