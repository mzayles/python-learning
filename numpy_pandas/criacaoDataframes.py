import pandas as pd
import numpy as np

# arrays > dataframe
arr = np.random.randint(10, 55, size=(4, 4))
df1 = pd.DataFrame(arr, index=["a", "b", "c", "d"], columns=["w", "x", "y", "z"])

print(df1)

# listas > dataframe
lista = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]]
df2 = pd.DataFrame(lista, index=["A", "B"], columns=["V", "W", "X", "Y", "Z"])

print(df2)

# dict > dataframe
dados = {
    "produtos":["videogame", "pc", "teclado", "microfone", "mouse"],
    "preco": [2500, 2450, 300.50, 59.99, 140]
}

df3 = pd.DataFrame(data=dados)
print(df3)

df3["custo"] = [1900, 2000, 500, 70.30, 65.40]
print(df3)

df3["lucro"] = df3["preco"] - df3["custo"]
print(df3)