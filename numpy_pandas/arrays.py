import numpy as np

# listas > arrays
qtde = [2, 5, 10, 20, 35]
custo = [100, 150, 450, 320, 195]

arr1 = np.array(qtde)
arr2 = np.array(custo)

estoque = arr1 * arr2
print(estoque)

custo2 = [100, 300, 500, 130]
venda = [125, 200, 120, 300]

arr3 = np.array(custo2)
arr4 = np.array(venda)

lucro = arr4 - arr3
print(lucro)

# arange()
np.arange(1, 20)
np.arange(10, 21, 2)
np.arange(10, 101, 2, dtype=float)

# linspace: elementos igualmente espaçados
np.linspace(0, 10, 10)

# random
np.random.rand(10)
np.random.randn(15)

arr = np.random.randint(10, 100, 30)
len(arr)

# matriz
np.zeros((5, 4))
np.ones((5, 5))
np.eye(6)