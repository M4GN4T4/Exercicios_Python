Jg = dict()
gols = []
Jogador = []
while True:
    Jg['nome'] =  str(input("Nome do Jogador:"))
    P = int(input(f"Quantas partidas {Jg['nome']} jogou:"))
    gols = []
    for i in range(0, P):
        g = int(input(f"Quantos gols na partida {i+1} ?:"))
        gols.append(g)
    Jg['gols'] = gols
    Jg['total'] = sum(gols)
    Jogador.append(Jg.copy())
    Jg.clear()
    while True:
        op = str(input("Quer Continuar ? [S/N]")).upper()[0]
        if op in "SN":
            break
    if op == "N":
        break
print(45 * "=")
print(f"{'Cod':<4} {'Nome':<6}{'Gols':>15}{'Total':>15}")
print(45 * "-")
for c, p in enumerate(Jogador):
    print(f"{c:<4} {p['nome']:<6}{str(p['gols']):>15}{str(p['total']):>15}")

while True:
    op1 = int(input("Mostrar dados de qual jogador ? (999 para parar):"))
    if op1 == 999:
        print("<< Volte Sempre >>")
        break    
    if op1 > len(Jogador)-1 or op1 < 0:
        print(f"Erro! Não existe jogador com código {op1}!")
    else:
        print(f"   O Jogador {Jogador[op1]['nome']:<3} Fez:")
        for i, g in enumerate(Jogador[op1]['gols']):
                print(f"   -No Jogo {i+1}º Fez {g} gols")
            