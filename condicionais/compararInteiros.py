""" Escreva um programa que leia dois números inteiros e
compare- os, mostrando na tela uma mensagem:

O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais """

numero1 = int(input("Digite o 1º número inteiro: "))
numero2 = int(input("Digite o 2º número inteiro: "))

if numero1 > numero2:
    print("\nO 1º valor é maior.")
elif numero2 > numero1:
    print("\nO 2º valor é maior.")
else:
    print("\nNão existe valor maior, os dois são iguais.")