s = float(input("Digite o seu salário:"))
if s > 1250:
    print(f"O seu aumento foi de {s * 0.10:.2f} Totalizando:{(s * 0.10) + s:.2f}")
elif s <= 1250:
    print(f"O seu aumento foi de {s * 0.15:.2f} Totalizando:{(s * 0.15)+ s:.2f}")
