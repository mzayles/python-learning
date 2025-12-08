""" Escreva um programa para aprovar um empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai
pagar.

Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será
negado. """

valor = float(input("Informe o valor da casa: "))
salario = float(input("Informe o seu salário: "))
tempo = int(input("Em quantos anos pretende pagar? ")) * 12

prestacao = valor / tempo
valor_excedido = valor * 0.30

if prestacao > valor_excedido:
    print("\nEmpréstimo negado.")
    print(f"Valor: R$ {prestacao:,.2f}.")
else:
    print("\nEmpréstimo aceito.")
    print(f"Valor: R$ {prestacao:,.2f}.")
