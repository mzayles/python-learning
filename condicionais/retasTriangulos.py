""" Refaça o DESAFIO dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:

Equilátero: Todos os lados iguais
Isósceles: Dois lados iguais
Escaleno: Todos os lados diferentes """

a = float(input("Digite o comprimento da 1º reta: "))
b = float(input("Digite o comprimento da 2º reta: "))
c = float(input("Digite o comprimento da 3º reta: "))

if (a == c) and (a == b):
    print("\nAs retas podem formar um triângulo equilátero.")
elif (a == b) or (a == c) or (b == c):
    print("\nAs retas podem formar um triângulo isósceles.")
else:
    print("\nAs retas podem formar um triângulo escaleno.")