""" Desenvolva um programa que leia quatro números inteiros pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares. """


tupla = tuple(int(input(f"Digite o {x+1}º número: ")) for x in range(4))

print(tupla)

print(f"\nQuantidade de valores [9]: {tupla.count(9)}.")
print(f"Posição do primeiro valor [3]: {tupla.index(3) + 1}." if 3 in tupla else "Não existe valor [3].")

print("Números pares digitados: ", end="")
for i in range(len(tupla)):
    if tupla[i] % 2 == 0:
        print(tupla[i], end=" | ")