""" A confederação Nacional de Natação precisa de uma programa
que leia o ano de nascimento de uma atleta e mostre sua
categoria, de acordo com a idade.

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 24 anos: SÊNIOR
Acima: MASTER """

ano = int(input("Digite seu ano de nascimento: "))
idade = 2025 - ano

if idade < 10:
    print("\nMIRIM.")
elif idade < 15:
    print("\INFANTIL.")
elif idade < 20:
    print("\JUNIOR.")
elif idade < 25:
    print("\SÊNIOR.")
else:
    print("\MASTER.")