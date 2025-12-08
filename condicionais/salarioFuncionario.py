""" Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00, calcule um aumento de
10%.

Para salários inferiores ou iguais, o aumento é de 15%. """

salario = float(input("Informe o salário: "))

if salario > 1250.00:
    print(f"\nSalário com aumento de 10%: R$ {salario + (salario * 0.10):,.2f}.")
else:
    print(f"\nSalário com aumento de 15%: R$ {salario + (salario * 0.15):,.2f}.")