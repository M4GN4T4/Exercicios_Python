Cadastro = dict()
Pessoas = []
p = " "
t = 0
while p not in "N":
    p = " "
    Cadastro['Nome'] = str(input("Nome:"))
    Cadastro['Idade'] = int(input("Idade:"))
    t += Cadastro['Idade']
    Sexo = " "
    while Sexo not in "MF":
        Sexo = str(input("Sexo [M/F]:")).upper()[0]
        if Sexo in "MF":
            Cadastro['Sexo'] = Sexo
        else:
            print("Erro!--[Responda apenas com [M] ou [F]]--Erro!")
    Pessoas.append(Cadastro.copy())
    Cadastro.clear()
    while p not in "SN":
        p = str(input("Quer Continuar [S/N]:")).upper()[0]
        if p == "N":
            break
        else:
            if p not in "SN":
                print("Erro!--[Responda apenas com [S] ou [N]]--Erro!") 
print(30 *"=")
Media = t / len(Pessoas)
print(f"A)Ao todo temos {len(Pessoas)}")
print(f"B)A Média de idade é de {Media}")
print(f"As mulheres cadastradas foram", end="")
for c in Pessoas:
    if c['Sexo'] == "F":
        print(f"[{c['Nome']}", end="]")
print()
print(f"D)Lista de pessoas que estão acima da média:")
for p in Pessoas:
    if p['Idade'] > Media:
        print(f"    {p}")
