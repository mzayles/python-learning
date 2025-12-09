""" Crie um programa que leia duas notas entre 0 a 10 de um aluno
e calcule sua média, mostrando uma mensagem no final, de
acordo com a média atingida.

Média abaixo de 5.0: REPROVADO
Média entre 5.0 a 6.9: RECUPERAÇÃO
Média igual ou superior a 7.0: APROVADO """

nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

media = (nota1 + nota2) / 2

if media < 6:
    print("\nREPROVADO!")
elif media < 7:
    print("\nRECUPERAÇÃO")
else:
    print("\nAPROVADO!")