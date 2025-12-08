""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o ultimo nome separadamente.

Exemplo: Leandro Gomes Andrade

Primeiro: Leandro
Ultimo: Andrade """

nome = input("Digite seu nome completo: ")

print("")

print(nome.split()[0].capitalize())
print(nome.split()[-1].capitalize())