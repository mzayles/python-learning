""" Com a lista do DESAFIO anterior, exiba uma lista com o nome da pessoa e o que ela come. """

almoco = [
    {"nome":"Leandro", "comida": "Lanche", "bebida": "Suco de Laranja"},
    {"nome":"Celia", "comida": "Lasanha", "bebida": "Suco de uva"},
    {"nome":"Catarina", "comida": "Pizza", "bebida": "Coca-Cola"}
]

for i in almoco:
    print(f"{i["nome"]} | {i["comida"]}")