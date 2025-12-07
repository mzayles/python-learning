""" Dado a nota das provas P1, P2 e P3, calcular a média (aritmética) das notas do aluno. """

prova1 = float(input("Digite a nota da 1º prova: "))
prova2 = float(input("Digite a nota da 2º prova: "))
prova3 = float(input("Digite a nota da 3º prova: "))

media = (prova1 + prova2 + prova3) / 3
print(f"\nMédia aritmética: {media:,.2f}.")