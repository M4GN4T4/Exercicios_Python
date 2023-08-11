c = c2 = c3 = 0
while True:
    idade = int(input("Digite sua idade:"))
    sexo = str(input("Digite seu Sexo[M/F]:")).upper().strip()[0]
    if sexo in"MF":
        if idade > 18:
            c += 1
        elif sexo == "M":
            c2 += 1
        elif sexo == 'F' and idade < 20:
            c3 += 1
    opcao = str(input("Quer continuar [S/N]")).upper().strip()[0]
    if opcao == "N":
        break
print(f"A o total existem {c} pessoas com mais de 18 anos.")
print(f"Foram cadastrados um total de {c2} homens.")
print(f"A o total existem {c3} mulheres com menos de 20 anos.")