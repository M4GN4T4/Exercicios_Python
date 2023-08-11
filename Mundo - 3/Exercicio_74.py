from random import randint 

Num =(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f"Os valores sorteados:", end=" ")
for n  in Num:
    print(f"{n}", end=" ")
print(f" ")
print(f"Menor valor:{min(Num)}")
print(f"Maior valor:{max(Num)}")



"""
Num = []
while True:
    ale = random.randint(0,1000)
    Num.append((ale))
    if len(Num) == 5:
        break
p = (Num)
print(p)
print(f"Menor valor:{min(p)}")
print(f"Maior valor:{max(p)}")
"""