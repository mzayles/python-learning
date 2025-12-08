""" Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, exemplo:
    APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    SOCORRAM ME SUBI NO ONIBUS EM MARROCOS """

frase = input("Digite uma frase: ").lower().replace(" ", "")

if frase[::-1] == frase:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")



