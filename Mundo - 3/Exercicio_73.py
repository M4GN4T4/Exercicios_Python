Tabela = ("Botafogo","Fortaleza","Palmeiras","Internacional","Fluminense",
          "Cruzeiro","Grêmio","São Paulo","Vasco da Gama","Atlético-MG",
          "Santos","Bragantino","Flamengo","Atlhetico-PR","Bahia",
          "Goiás","Corinthians","Cuiabá","Coritiba","América-MG")

for time in Tabela:
    print(time, end="|")
print(" ")

print(f"Os Primeiros 5 colocados são:{Tabela[:5]}")
print(f"Os Ultimos 4 colcados são {Tabela[-4:]}")
print(f"Times em ordem alfabética:{sorted(Tabela)}")
print(f"O São Paulo está na {Tabela.index('São Paulo')+1}ª Posição")
'''
for time in Tabela:
    if time[0] == "A":
        print(time)
print(5 * "-=")
for time in Tabela:
    if time[0] == "B":
        print(time)
print(5 * "-=")
for time in Tabela:
    if time[0] == "C":
        print(time)
print(5 * "-=")
for time in Tabela:
    if time[0] == "F":
        print(time)
print(5 * "-=")
for time in Tabela:
    if time[0] == "G":
        print(time)
print(5 * "-=")
for time in Tabela:
    if time[0] == "S":
        print(time)
print(5 * "-=")
for time in Tabela:
    if time[0] == "V":
        print(time)
print(5 * "-=")

for p,time in enumerate(Tabela):
    if p == 7:
        print(f"O {time} está na {p + 1}ª Posição")'''