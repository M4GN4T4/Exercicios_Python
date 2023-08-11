import random
contador = 0
n = int(input('Adivinhe o número escolhido entre 1 e 10:'))
a = random.randint(1, 10)
print(a)
while n != a:
    n = int(input("Digite Novamente até acertar:"))
    contador += 1
if n == a:
    print(f"Você finalmente acertou o número escolhido foi {a}\n {contador} Tentativas")