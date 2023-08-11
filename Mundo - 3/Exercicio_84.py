NP = []
Pessoas = []
c = Pesado = Leve = 0
while True:
    # Contador.
    c += 1

    # Cadastro_de_Nome_é_Peso.
    print(30 * "=")
    NP.append(str(input("Nome:")))
    NP.append(int(input("Peso:")))

    # Maior_Peso_é_Menor_Peso.
    if len(Pessoas) == 0:
        Pesado = Leve = NP[1]
    else:
        if NP[1] > Pesado:
            Pesado = NP[1]
        if NP[1] < Leve:
            Leve = NP[1]
    # Criando_uma_Ligação_de_forma_que_não_altere_a_lista_Pessoas.
    Pessoas.append(NP[:])

    # Limpando_NP_para_não_haver_repetição_de_informação_já_que_a_variavel_está_fora_do_Loop
    NP.clear()

    # Encerramento_ou_Continuação_de_Execução.
    pergunta = str(input("Quer continuar digite [S/N]:")).upper()[0]
    if pergunta in "N":
        break
    elif pergunta in "S":
        continue

print(30 * "=")
print(f"Foram cadastradas {c} Pessoas")
print(f"O maior peso é {Pesado} as pessoas mais pesadas são", end=" ")
for p in Pessoas:
    if p[1] == Pesado:
        print(f"{p[0]}", end=" ")
print()
print(f"O menor peso é {Leve} as pessoas mais leves são", end=" ")
for p in Pessoas:
    if p[1] == Leve:
        print(f"{p[0]}", end=" ")
print()

print(Pessoas)
"""
    # Maior_Peso.
    if pesado < Peso:
        pesado = Peso

    # Menor_Peso.
    if c == 1:
        leve = Peso
    if leve > Peso:
        leve = Peso

    # Pessoa_mais_pesada.
    Pe = []
    for p, x in Pessoas:
        if x > 70:
            Pe.append(p)

    # Pessoa_mais_leve
    Le = []
    for p, x in Pessoas:
        if x <= 70:
            Le.append(p)

   
"""