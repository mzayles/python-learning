import pandas as pd
import numpy as np
np.random.seed(100)

indices = ["janeiro", "março", "maio", "julho", "agosto", "outubro", "novembro"]

colunas = np.arange(1, 32)
print(colunas)

dados = np.random.randint(492, 2050, size=[7, 31])
print(dados)

df = pd.DataFrame(data=dados, index=indices, columns=colunas)

# colunas
df[2]
df[[2, 3, 4]]

# linhas
df[1][2]
df[3:5] 
df[2:]

df.loc["julho", 30]

df.iloc[3, 30]
df.iloc[[1, 2, 3], [1, 2, 3]]

# quanto vendeu no dia 10 de todos os meses
print(df[10])

# quanto vendeu nos dias 10, 20 e 30 de todos os meses
print(df[[10, 20, 30]])

# quanto vendeu no dia 15 de março
print(df.loc["março", 15])

# quanto vendeu em janeiro, março e maio
print(df[0:3])

# vendas de julho, agosto e outubro nos dias 25 a 31
print(df.loc[["julho", "agosto", "outubro"], 25:31])
print(df.iloc[[3, 4, 5], [24, 25, 26, 27, 28, 29, 30]])

df.rename({"novembro":"dezembro"}, inplace=True)

# seleção com condições
df[df > 1000]
df[df > 1000].fillna("-")

# vendas maiores que 1000 em janeiro, março e maio
df[df > 1000][0:3]

# vendas maiores que 1000 nos dia 1 ao 5 de todos os meses
df[df > 1000][:][[1, 2, 3, 4, 5]].fillna("-")

# seleção com mais de uma condição
df[(df[10] > 1000) & (df[15] > 1500)]
df[(df[10] > 1000) | (df[15] > 1500)]