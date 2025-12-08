""" Escreva um programa em Python que solicite ao usuário uma nota inteira entre 0 e 10.
Use o comando `match case` para classificar a nota de acordo com a tabela a seguir:

- 0-4: Nota Baixa
- 5-7: Nota Média
- 8-9: Nota Alta
- 10: Nota Excelente

Exiba a classificação correspondente. """

nota = int(input("Digite uma nota inteira entre 0 e 10: "))

match(nota):
    case 0 | 1 | 2 | 3 | 4:
        print(f"\nNota Baixa.")
    case 5 | 6 | 7:
        print(f"\nNota Média")
    case 8 | 9:
        print(f"\nNota Alta")
    case _:
        print(f"\nNota Excelente.")