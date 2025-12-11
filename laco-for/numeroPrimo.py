""" Faça um programa que leia um número inteiro e diga se ele é ou não um numero primo.
> 1 só é divisível por ele mesmo """

numero = int(input("Digite um número inteiro: "))

contador = 0

for i in range(1, numero):
    if numero % i == 0:
        contador += 1
    if contador > 1:
        break

if contador > 1:
    print("\nEsse número não é primo.")
else:
    print("\nEsse número é primo.")