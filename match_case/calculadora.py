""" Implemente uma calculadora simples que realiza as operações de adição, subtração, multiplicação e divisão.
O usuário deve inserir dois números e, em seguida, selecionar a operação desejada (+, -, *, /).
Use o comando match case para realizar a operação correta e exibir o resultado. """

numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))

opcao = int(input("""
    Escolha a operação desejada:
              
    [1] Adição
    [2] Subtração
    [3] Multiplicação
    [4] Divisão\n
"""))

match(opcao):
    case 1:
        print(f"\nAdição: {numero1 + numero2}.")
    case 2:
        print(f"\nSubtração: {numero1 - numero2}.")
    case 3:
        print(f"\nMultiplicação: {numero1 * numero2}.")
    case 4:
        print(f"\nDivisão: {numero1 / numero2}.")
    case _:
        print(f"\nInválido!")