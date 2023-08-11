Num = []
Par = []
Imp = []
while True:
    n = int(input("Digite um número:"))
    Num.append(n)
    op = str(input("Quer continuar [S/N]"))
    if op in "Nn":
        break
    if n % 2 == 0:
        Par.append(n)
    else:
        Imp.append(n)
print(f"Os números presentes na lista {Num}")
print(f"Os números pares presentes na lista {Par}")
print(f"Os números Ímpares presentes na lista {Imp}")