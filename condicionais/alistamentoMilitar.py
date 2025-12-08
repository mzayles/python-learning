""" Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:

Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou o tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo. """

ano = int(input("Digite seu ano de nascimento: "))
idade = 2025 - ano

if idade < 18:
    print("\nVocê ainda irá se alistar.")
elif idade == 18:
    print("\nÉ hora de se alistar!")
else:
    print("\nJá passou da hora de se alistar!")