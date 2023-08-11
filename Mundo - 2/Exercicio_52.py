n = int(input("Digite um número inteiro qualquer:"))
q = 0
for num in range(1, n + 1):
    if n % num == 0:
        q += 1
        #Garante a coloração para os números divisiveis
        print('\033[32m', end='')
    else:
        # Garante a coloração para os não divisiveis
        print('\033[31m', end='')
    #Para que os números saiam um do lado do outro
    print(f"{num}", end='')
print(f"\n\033[mEsté número {n} foi divisivel {q} vezes")
if q == 2:
    print("Ele é um número primo")
else:
    print("Ele não e um número primo")