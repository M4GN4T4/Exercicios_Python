d = float(input("Digite a distancia da viagem:"))
if d <= 200:
    print(f"A taxa a ser paga:{d * 0.50} Reais")
else:
    print(f"A taxa a ser paga:{d * 0.45} Reais")