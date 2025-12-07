""" Solicite ao usuário o valor do salário atual, em seguida solicite o
percentual de aumento e imprima o valor do salário atualizado. """

salario_atual = float(input("Digite o seu salário atual: "))
percentual = int(input("Digite o percentual de aumento: "))

salario_atualizado = salario_atual + (salario_atual * (percentual / 100))
print(f"\nSeu salário atualizado é R$ {salario_atualizado:,.2f}.")