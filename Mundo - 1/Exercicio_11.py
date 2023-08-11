#import math
from math import hypot
c1 = float(input("Insira o cateto Oposto:"))
c2 = float(input("Insira o cateto Adjacente:"))
print(f"A Hipotenusa é {hypot(c1,c2):.2f}")
#print(f"A Hipotenusa é {math.hypot(c1,c2):.2f}")
#print(f"A Hipotenusa é {((c1 ** 2) + (c2 ** 2))** (1 / 2):.2f}")