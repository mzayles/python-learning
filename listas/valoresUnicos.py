""" Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final serão exibidos
todos os valores únicos digitados, em ordem crescente. """

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

valores.sort()
print(f"Valores: {valores}.")