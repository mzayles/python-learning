""" Refaça o DESAFIO 01 considerando notas decimais. """

nota = float(input("Digite uma nota entre 0 e 10: "))

match(nota):
    case _ if nota < 0:
        print("\nNota inválida!")
    case _ if nota < 5:
        print(f"\nNota Baixa.")
    case _ if nota < 8:
        print(f"\nNota Média")
    case _ if nota < 10:
        print(f"\nNota Alta")
    case 10:
        print(f"\nNota Excelente.")
    case _:
        print(f"\nNota inválida!")