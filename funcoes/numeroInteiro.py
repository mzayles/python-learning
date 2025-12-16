""" Faça um programa que receba um número inteiro de 0 a 9.
Crie uma função que apresente o resultado da tabuada deste número. """

def tabuada(numero):
    for i in range(0, 11):
        print(f"{numero} x {i} = {numero * i}")

usuario = int(input("Digite a tabuada que deseja exibir (0 a 9): "))
print("")
tabuada(usuario)