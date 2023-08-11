Num = []
while True:
    n = int(input("Digite o número:"))
    Num.append(n)
    if str(input("Quer continuar[S/N]:")) in "Nn":
        break
Num.sort(reverse=True)
print(f"Foram digitados [{len(Num)}] números")
print(Num)
if 5 in Num:
    print(f"O valor 5 faz parte da lista")
else:
    print(f"O valor 5 não está na lista")
