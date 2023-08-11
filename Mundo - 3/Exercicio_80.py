Num = []
for n in range(0,5):
    up = int(input("Digite um número:"))
    if n == 0 or up > Num[-1]:
        Num.append(up)
    else:
        po = 0
        while po < len(Num):
            if up <= Num[po]:
                Num.insert(po, up)
                print(f"Adicionado na posição {po} da Lista...")
                break
            po += 1
print(f"Os valores digitados em ordem foram:{Num}")