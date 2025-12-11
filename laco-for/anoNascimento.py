""" Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. """

maior = 0
menor = 0

for i in range(1, 8):
    ano = float(input(f"Digite o {i}º ano de nascimento: "))

    if ano <= 2007:
        maior += 1
    else:
        menor += 1

print(f"\nNão atingiram a maioridade: {menor}.")
print(f"\nAtingiram a maioridade: {maior}.")