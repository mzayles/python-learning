# read
arq = open("manipulacao_arquivos/usuarios.txt", "r")
arq.close()

# write
arq = open("manipulacao_arquivos/usuarios2.txt", "w")
arq.close()

# append
arq = open("manipulacao_arquivos/usuarios.txt", "a")
arq.close()

# read and write
arq = open("manipulacao_arquivos/usuarios.txt", "r*")
arq.close()

# with
with open("manipulacao_arquivos/usuarios.txt") as arq:
    dados = arq.read()
print(dados)
print(arq.closed)

# ler
arq = open("manipulacao_arquivos/usuarios.txt", "r")
print(arq.read())
arq.close()

# ler linha por linha
arq = open("manipulacao_arquivos/usuarios.txt", "r")

for linha in arq:
    print(linha.replace("\n", ""), end=" | ")
arq.close()

# ler como uma lista
arq = open("manipulacao_arquivos/usuarios.txt", "r")
print(arq.readlines())

with open("manipulacao_arquivos/usuarios2.txt", "a") as arq:
    valor = ("Resposta", 42)
    s = str(valor)
    print(arq.write(s)) # devolve bytes

arq.tell() # em que ponto da leitura está
arq.seek() # mudar a posição inicial