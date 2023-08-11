contador1 = 0
contador2 = 0
for x in range(0, 7):
    x = int(input("Digite a idade de 7 Pessoas:"))
    if 2023 - x < 21:
        contador1 += 1
    elif 2023 - x >= 21:
        contador2 += 1
print(f"{contador2} Ja passaram ou estão na maioridade")
print(f"{contador1} Não são maiores de idade")