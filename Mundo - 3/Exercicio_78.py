Num = []
for n in range(0,5,1):
    Num.append(int(input(f"Digite o número na posição [{n+1}]:")))
    if n == 0:
        maior = menor = Num[n]
    else:
        if Num[n] > maior:
            maior = Num[n]
        if Num[n] < menor:
            menor = Num[n]
print(f"A lista de números:{Num}")
print(f"O maior número é {maior} nas posições", end='...')
for a, p in enumerate(Num):
    if p == maior:
        print(f"{a+1}...",end='')
print()

print(f"O menor número é {menor} nas posições", end='...')
for a, p in enumerate(Num):
    if p == menor:
        print(f"{a+1}...",end='')
print()

#print(f"O número maior é {max(Num)}")
#print(f"O número menor é {min(Num)}")