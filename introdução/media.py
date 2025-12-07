nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"\nA sua média final é {media:,.2f}.")

if media > 5:
    print('Aprovado!')
else:
    print('Reprovado!')