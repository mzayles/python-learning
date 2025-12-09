""" Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
Condições Necessárias:

a + b > c
a + c > b
b + c > a """

a = float(input("Digite o comprimento da 1º reta: "))
b = float(input("Digite o comprimento da 2º reta: "))
c = float(input("Digite o comprimento da 3º reta: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("\nAs retas podem formar um triângulo.")
else:
    print("\nAs retas não podem formar um triângulo.")