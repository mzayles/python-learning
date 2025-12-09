""" Escreva um programa que converta valores entre diferentes moedas.
O usuário deve inserir o valor em reais e selecionar a moeda para conversão:
D (Dólar), E (Euro), ou L (Libra). Utilize match case para aplicar a conversão
correta com base nas taxas fictícias fornecidas a seguir:

1 Real = 0.18 Dólar
1 Real = 0.16 Euro
1 Real = 0.13 Libra

Símbolos: $ € £ """

valor = float(input("Digite o valor em R$: "))

conversao = input("""
    [D] Dólar 
    [E] Euro
    [L] Libra\n
""").upper()

match(conversao):
    case _ if "D":
        print(f"\nR$ {valor:,.2f} | Dólar: {valor * 0.18:,.2f}.")
    case _ if "E":
        print(f"\nR$ {valor:,.2f} | Euro: {valor * 0.16:,.2f}.")
    case _ if "L":
        print(f"\nR$ {valor:,.2f} | Libra: {valor * 0.13:,.2f}.")
    case _:
        print("\nInválido.")