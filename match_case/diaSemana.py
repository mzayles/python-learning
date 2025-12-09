""" Crie um programa que peça ao usuário para inserir um número de 1 a 7,
onde cada número representa um dia da semana (1 para domingo, 2 para segunda-feira e assim por diante).
Use match case para imprimir o nome do dia da semana correspondente. """

numero = int(input("Digite um número de 1 a 7 para obter o dia da semana: "))

match(numero):
    case 1:
        print("\nDomingo") 
    case 2:
        print("\nSegunda-feira.") 
    case 3:
        print("\Terça-feira.") 
    case 4:
        print("\Quarta-feira.") 
    case 5:
        print("\nQuinta-feira.") 
    case 6:
        print("\nSexta-feira.") 
    case 7:
        print("\nSábado.") 
    case _:
        print("\nInválido!") 