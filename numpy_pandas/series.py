import pandas as pd
import numpy as np

# lista > series
lista = [10, 20, 30, 40, 50]
series1 = pd.Series(lista)

print(series1)
print(series1[1])

# dicionário > series
dicionario = {
    "telefone1":"99999-9999",
    "telefone2":"88888-8888",
    "telefone3":"77777-7777"
}

series2 = pd.Series(dicionario)

print(series2)
print(series2[2])
print(series2["telefone2"])

# arrays > series
arr = np.array([10, 20, 30, 40, 50])
series3 = pd.Series(arr)

print(series3)

lista = [100, 200, 300, 400, 500]
series4 = pd.Series(lista)

print(series4)

series5 = pd.Series([1, 2, 3, 4], index=["br", "usa", "uk", "fra"])
print(series5)

labels = ["a", "b", "c", "d"]
series6 = pd.Series(data=[1, 2, 3, 4], index=labels)

print(series6)

labels = ["a", "b", "c", "4"]
series7 = pd.Series(data=[1, 2, 3, 10], index=labels)

print(series7)

print(series6 + series7)