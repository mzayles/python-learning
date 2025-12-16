""" Faça com que o programa anterior possa cadastrar uma quantidade de alunos escolhida pelo usuário.
No final apresente as informações tabuladas. """

dicionario = {}
alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    nome = input(f"\nDigite o nome do {i+1}º aluno: ")
    media = float(input(f"Digite a média do {i+1}º aluno: "))

    if media < 5:
        situacao = "Reprovado"
    elif media < 7:
        situacao = "Exame"
    else:
        situacao = "Aprovado"

    dicionario["nome"] = nome
    dicionario["media"] = media
    dicionario["situacao"] = situacao

    alunos.append(dicionario.copy())

print("") 
for i in range(len(alunos)):
    print(f"Nome: {alunos[i]["nome"].title()}, Média: {alunos[i]["media"]}, Situação: {alunos[i]["situacao"]}")