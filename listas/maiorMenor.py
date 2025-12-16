""" Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e as suas respectivas posições na lista. """

valores = []

for i in range(0, 5):
    numero = int(input(f"Digite o {i+1}º número: "))
    valores.append(numero)

print(f"\nMaior valor: {max(valores)} | Indíce: {valores.index(max(valores))}")
print(f"Menor valor: {min(valores)} | Indíce: {valores.index(min(valores))}")