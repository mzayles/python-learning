""" Dada a lista com 32 Times, faça o sorteio para outras duas listas (A e B).
Ao final, cada nova lista deve conter 16 times.
random.choice(times) """

import random 

times = ["Flamengo", "Palmeiras", "São Paulo", "Athletico-PR", "Atlético-MG",
       "Corinthians" ,"Fluminense", "Grêmio", "Fortaleza", "Internacional", "Bahia",
       "Botafogo", "Red Bull Bragantino", "Atlético-GO", "Ceará", "Cuiabá", 'Goiás',
       'Vasco', 'Juventude', 'Sport', 'CRB', 'Vitória', 'Criciúma', 'Sampaio Corrêa',
       'Operário-PR' ,'Botafogo-SP', 'Brusque', 'Ypiranga-RS', 'América-RN', 'Amazonas',
       'Águia de Marabá', 'Sousa-PB']

timeA = []
timeB = []

for i in range(len(times)):
    time = random.choice(times)

    if len(times) % 2 == 0:
        timeA.append(time)
    else:
        timeB.append(time)

    times.remove(time)

print(f"Time A: {timeA}")
print(f"\nTime B: {timeB}")