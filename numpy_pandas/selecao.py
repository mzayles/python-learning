import numpy as np

cadastro = np.random.randint(15, 50, size=[50,10])
print(cadastro)

cadastro_maior18 = cadastro > 18
print(cadastro[cadastro_maior18])

arr3 = cadastro[cadastro > 18]
print(len(arr3))

cadastro_maior18.sum() # binário (True)

arr4 = cadastro[cadastro > 25]
print(len(arr4))

condicao = cadastro[cadastro > 20]
extraido = np.extract(condicao, cadastro)

print(extraido)