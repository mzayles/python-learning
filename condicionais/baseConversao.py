""" Escreva um programa que leia um número inteiro e peça para o
usuário escolher qual será a base de conversão:

    1 para binário bin()
    2 para octal oct()
    3 para hexadecimal hex() """

numero = int(input("Digite um número inteiro: "))
usuario = int(input("""
    Qual será a base de conversão?
                    
    [1] Binário
    [2] Octal 
    [3] Hexadecimal 
                    
"""))

if usuario == 1:
    print(f"\nNúmero: {numero} | Binário: {bin(numero)}.")
elif usuario == 2:
    print(f"\nNúmero: {numero} | Binário: {oct(numero)}.")
else:
    print(f"\nNúmero: {numero} | Binário: {hex(numero)}.")