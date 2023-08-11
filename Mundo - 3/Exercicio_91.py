from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1º': randint(1, 6),
        'Jogador 2º': randint(1, 6),
        'Jogador 3º': randint(1, 6),
        'Jogador 4º': randint(1, 6)}
print("=====Valores_Sorteados=====")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1))
print("==========Ranking==========")
for j, r in enumerate(ranking):
    print(f"{j+1} ºLugar {r[0]} tirou {r[1]}")
    sleep(0.75)