Num =(int(input("Digite um número:")),
      int(input("Digite um número:")),
      int(input("Digite um número:")),
      int(input("Digite um número:")))
c = 0

print(f"O valor 9 apareceu {Num.count(9)}")
print(f"Os números pares são:",end='|')
for n in Num:
    if n % 2 == 0:
        print(n,end='|')
print("")
print(f"O primeiro (3) Apareceu na posição:{Num.index(3)+1}ª")
'''for n,p in enumerate(Num):
    if p == 3:
        print(f"O primeiro (3) Apareceu na posição:{n+1}ª")
'''