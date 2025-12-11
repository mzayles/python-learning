""" Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o 999). """

quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero == 999:
        print("\nCondição de parada! Programa encerrado.")
        break
    else:
        quantidade += 1
        soma += numero

print(f"\nQuantidade de números digitados: {quantidade}")
print(f"Soma dos números digitados: {soma}")