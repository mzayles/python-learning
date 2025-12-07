""" Crie um programa que dados o valor, da taxa e o tempo, efetuar o cálculo do valor de
uma prestação em atraso.
    FÓRMULA: valor da prestação + (valor da prestação * (taxa / 100) * tempo) """

valor = float(input("Informe o valor da prestação: "))
taxa = int(input("Informe a taxa (%): "))
tempo = int(input("Informe o tempo (dias) de atraso: "))

valor_final = valor + (valor * (taxa / 100) * tempo)
print(f"\nO valor da prestação em atraso é de R$ {valor_final:,.2f}.")