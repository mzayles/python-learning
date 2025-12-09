""" Faça um programa que leia um ano qualquer e mostre se ele é
BISSEXTO.
O ano bissexto ocorre a cada 4 anos (exceto em anos múltiplos
de 100 que não são múltiplos de 400) """

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if (ano % 100 == 0) or (ano % 400 == 0):
        print("Ano bissexto.")
else:
    print("Ano não bissexto.")