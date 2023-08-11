import random 
print("Escolha entre Pedra,Papel,Tesoura")
o = ["Pedra", "Papel", "Tesoura"]
Computador = random.choice(o)
e = str(input("Qual será o escolhido:")).lower().capitalize()
print(f"O Computador escolheu {Computador}")
if Computador == "Pedra":
    if e == "Pedra":print("Pedra com Pedra:Empate")
    elif e == "Papel":print("Papel vence de Pedra:Vencedor")
    elif e == "Tesoura":print("tesoura perde de Pedra:Perdeu")
elif Computador == "Papel":
    if e == "Papel":print("Papel com Papel:Empate")
    elif e == "Pedra":print("Papel vence de Pedra:Perdeu")
    elif e == "Tesoura":print("Papel perde de Tesoura:Vencedor")
elif Computador == "Tesoura":
    if e == "Tesoura":print("Tesoura com Tesoura:Empate")
    elif e == "Papel":print("Tesoura vence de Papel:Perdeu")
    elif e == "Pedra":print("Tesoura perde de Pedra:Venceu")