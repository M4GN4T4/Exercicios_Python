L_Aluno = []
lista_P = []
while True:
    L_Aluno.append(str(input("Nome:")))
    for _ in range(1, 3):
        L_Aluno.append(int(input(f"Nota {_}º:")))
    lista_P.append(L_Aluno[:])
    L_Aluno.clear()
    op = str(input("Quer continuar ? [S/N]:"))[0]
    if op in "Nn":
        break
print(16 * "-=")
print(f"{'No.':<4}{'Nome':<10}{'Media':>8}")
print(32 * "-")
for a, n in enumerate(lista_P):
    print(f"{a:<4}{n[0]:<10}{(n[1]+ n[2]) / 2:>8.1f}")
while True:
    mn = int(input("Mostrar notas de qual aluno ? (999 interrompe):"))
    if mn == 999:
        break
    else:
        for a, n in enumerate(lista_P):
            if a == mn:
                print(f"Notas de {n[0]} são [{n[1]}, {n[2]}]")