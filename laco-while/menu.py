""" Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. """

while True:
    numero1 = float(input("Digite o 1º número: "))
    numero2 = float(input("Digite o 2º número: "))

    opcao = int(input("""
        Escolha uma opção:
                  
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa\n
    """))
    
    match(opcao):
        case 1:
            print(f"\n{numero1} + {numero2} = {(numero1 + numero2):,.2f}\n")
        case 2:
            print(f"\n{numero1} x {numero2} = {(numero1 * numero2):,.2f}\n")
        case 3:
            print(f"\nMaior valor entre {numero1} e {numero2}: {max(numero1, numero2)}\n")            
        case 4:
            print("\nAdicione novos números!\n")
        case 5:
            print("\nSaindo...")
            break
        case _:
            print("\nInválido!")