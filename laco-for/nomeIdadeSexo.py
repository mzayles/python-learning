""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final  do programa mostre:
	A média de idade do grupo
	Qual é o nome do homem mais velho
	Quantas mulheres tem menos de 20 anos """

media = 0
maior = 0
quantidade = 0

for i in range(1, 5):
    nome = input(f"Digite o {i}º nome: ")
    idade = int(input(f"Digite a {i}º idade: "))
    sexo = input(f"Digite o {i}º sexo: ").upper()

    print("")

    media += idade
    
    if sexo == "M" or sexo == "MASCULINO":
        if idade > maior:
            homem = nome
            maior = idade

    if sexo == "F" or sexo == "FEMININO":
        if idade < 20:
            quantidade += 1

print(f"Média de idade do grupo: {media / 4}.")
print(f"O nome do homem mais velho é {homem.title()} com {maior} anos.")
print(f"A quantidade de mulheres com menos de 20 anos é {quantidade}.")