""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou não na lista. """

valores = []

while True:
    numero = float(input("\nDigite um valor: "))

    if numero not in valores:
        valores.append(numero)
    else:
        print("Esse número já está na lista.")

    opcao = input("""
    Deseja continuar? 
                  
    [S] Sim
    [N] Não
    \n""").upper()

    if opcao == "S":
        continue
    elif opcao == "N":
        break
    else:
        print("Inválido!")

print(f"Quantidade de números digitados: {len(valores)}.")

valores.sort()
valores.reverse()

print(f"Lista decrescente: {valores}.")

if 5 in valores:
    print("O valor 5 foi digitado, está na lista.")
else:
    print("O valor 5 não foi digitado, não está na lista.")