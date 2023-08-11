import random
n = int(input('Adivinhe o número escolhido entre 1 e 5:'))
a = random.randint(1, 5)
#Lista = [1, 2, 3, 4, 5]
#a = random.choice(Lista)
if a == n:
    print(f"Você adivinhou corretamente o número escolhido foi {a}")

else:
    print(f"Você errou o número escolhido foi {a} tente novamente")
print(a)