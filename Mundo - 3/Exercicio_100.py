import random
import time
s = []
def sorteia(list):
    print("Sorteando 5 valores da lista:", end=' ')
    for _ in range(1, 6, 1):
        g = random.randint(0, 10)
        list.append(g)
        time.sleep(0.5) 
        print(g, end=' ', flush=True)
        
    print("PRONTO!")

      
def somaPar(lst):
    a = 0
    for _ in lst:
        if _ % 2 == 0:
            a += _
    print(f"Somando so valores pares {s}, temos {a}")

sorteia(s)
somaPar(s)