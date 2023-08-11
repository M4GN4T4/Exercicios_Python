#import random
from random import choice
a1 = str(input("Primeiro Aluno:"))
a2 = str(input("Segundo Aluno:"))
a3 = str(input("Terceiro Aluno:"))
a4 = str(input("Quarto Aluno:"))
Lista = [a1, a2, a3, a4]
Escolhido = choice(Lista)
#Lista = ["João", "Pedro", "Maria", "Miguel"]
#Escolhido = random.choice(Lista)
print(f"E o escolhido para apagar o quadro foi {Escolhido}")