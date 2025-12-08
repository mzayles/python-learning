""" Refazer o DESAFIO 03 escolhendo a letra para contar e desconsiderar espaços. """

frase = input("Digite uma frase: ").upper()
letra = input("Digite a letra para contar: ").upper()

print("")

print(frase.count(letra))
print(frase.find(letra) + 1)
print(frase.rfind(letra))