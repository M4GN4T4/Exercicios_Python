import random
import time
qjs = int(input("Quantos jogos deseja sortear:"))
P = []
Jogos = []
total = 0
while total <= qjs:
    c = 0
    while True:
        a = random.randint(1, 60)
        if a not in P:
            P.append(a)
            c += 1
        if c >= 6:
            break
    P.sort()
    Jogos.append(P[:])
    P.clear()
    total += 1
for i, j in enumerate(Jogos):
    print(f"Jogo {i+1}º:{j}")
    time.sleep(0.3)


# import random
# import time
# qjs = int(input("Quantos jogos deseja sortear:"))
# c = 0
# while c != qjs:
 #   c += 1
  #  P = []
   # for _ in range(1, 7):
    #    while len(P) != 6:
     #       a = random.randint(1, 60)
      #      if a not in P:
       #         P.append(a)
    # P.sort()
    # time.sleep(0.5)
    # print(f"Jogo {c}º:{P}")
