""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão. """

primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))

print("")

for i in range(1, 11):
    progressao = primeiro_termo + (i - 1) * razao
    print(progressao)