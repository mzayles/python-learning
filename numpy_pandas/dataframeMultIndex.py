import pandas as pd
import numpy as np

lista = [["bra", "bra", "bra", "arg", "arg", "arg"], [2017, 2018, 2019, 2017, 2018, 2019]]

# junção de indexs
tuplas = zip(*lista)

tuplas = list(tuplas)
print(tuplas)

multi = pd.MultiIndex.from_tuples(tuplas)
print(multi)

df = pd.DataFrame(data=np.random.randn(6, 2), index = multi, columns=["exp trigo", "exp ovos"])

df.index.names = ["país", "ano"]
print(df)

# seleção
df["exp ovos"]
df.loc["bra"]

# localizar por seção
df.xs(2017, level=1)

df[:2]

df[["exp trigo", "exp ovos"]]

# visualização do dataframe de outra maneira
df2 = df.unstack()

print(df2)
df2["exp trigo"]

# eixo e nível
df2.xs(2017, axis=1, level=1)