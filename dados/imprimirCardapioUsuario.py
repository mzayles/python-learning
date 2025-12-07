""" Utilizando o DESAFIO 12, faça com que o usuário digite o nome
e preço de um produto para acrescentar ao final do cardápio. """

produto = input("Digite o produto: ")
preco = input("Digite o preço do produto: ")

print("")

print(f" CARDÁPIO ".center(40, '#'))
print("\nPastel".ljust(35, '.'), "R$ 6,50")
print("Coxinha".ljust(34, '.'), "R$ 5,50")
print("Risoles de queijo".ljust(34, '.'), "R$ 7,50")
print(f"{produto.ljust(34, '.').capitalize()} R$ {preco}")
