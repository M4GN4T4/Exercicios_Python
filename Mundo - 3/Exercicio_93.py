Jg = dict()
gols = []

Jg['nome'] =  str(input("Nome do Jogador:"))
P = int(input(f"Quantas partidas {Jg['nome']} jogou:"))
for i in range(0, P):
     g = int(input(f"Quantos gols na partida {i+1} ?:"))
     gols.append(g)
Jg['gols'] = gols
Jg['total'] = sum(gols)

print(30 * "-=")
print(Jg)

print(30 * "-=")
for k, v in Jg.items():
     print(f"O Campo {k} tem o valor {v}")
print(30 * "-=")

print(f"O Jogador {Jg['nome']} jogou {P} Partidas.")
for _, i  in enumerate(Jg['gols']):
    print(f"  => Na Partida {_+1}, fez {i} gols.")
print(f"Foi um total de {Jg['total']} gols")